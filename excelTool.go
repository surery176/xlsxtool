package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"github.com/xuri/excelize/v2"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"runtime"
	"strconv"
	"strings"
	"sync"
)

type SheetHead struct {
	Name  string
	Type  string
	Desc  string
	Check string

	IsCli bool
	IsSvr bool
}

type SheetTable struct {
	FileName  string
	SheetName string
	Head      []*SheetHead
	Rows      [][]interface{}

	IsCli bool
	IsSvr bool
}

var workDir = flag.String("idir", ".", "xlsx dir")
var cJsonDir = flag.String("idir", "./clientJson/", "client json out dir")
var sJsonDir = flag.String("idir", "./serverJson/", "server json out dir")
var cTempDir = flag.String("idir", "./clientTemplate/", "client template out dir")
var sTempDir = flag.String("idir", "./serverTemplate/", "server template out dir")

var wg sync.WaitGroup //定义一个同步等待的组
var sheetlist = make(map[string]*SheetTable)
var mlock sync.Mutex

func handleOneCell(fs string, sheetName string, line int, row string, sheetHead *SheetHead) interface{} {
	switch sheetHead.Type {
	case "int":
		if row == "" {
			return int64(0)
		}
		ret, err := strconv.ParseInt(row, 10, 64)
		if err != nil {
			panic(fmt.Sprintf("配置表错误：%v %v %v %v %v", fs, sheetName, line, sheetHead.Type, row))
		}
		return ret
	case "string":
		return json.RawMessage(`"` + row + `"`)
	case "mapint":
		ret := make(map[string]int64)
		if row == "" {
			return ret
		}
		for _, v := range strings.Split(row, "|") {
			kv := strings.Split(v, ":")
			if len(kv) != 2 {
				panic(fmt.Sprintf("配置表错误：%v %v %v %v %v", fs, sheetName, line, sheetHead.Type, row))
			}
			mapkey := kv[0]
			mapvalue, err := strconv.ParseInt(kv[1], 10, 64)
			if err != nil {
				panic(fmt.Sprintf("配置表错误：%v %v %v %v %v", fs, sheetName, line, sheetHead.Type, row))
			}
			ret[mapkey] = mapvalue
		}
		return ret
	case "mapstring":
		ret := make(map[string]json.RawMessage)
		if row == "" {
			return ret
		}
		for _, v := range strings.Split(row, "|") {
			kv := strings.Split(v, ":")
			if len(kv) != 2 {
				panic(fmt.Sprintf("配置表错误：%v %v %v %v %v", fs, sheetName, line, sheetHead.Type, row))
			}
			mapkey := kv[0]
			mapvalue := json.RawMessage(`"` + kv[1] + `"`)

			ret[mapkey] = mapvalue
		}
		return ret
	case "arrayint":
		ret := make([]int64, 0)
		if row == "" {
			return ret
		}
		for _, v := range strings.Split(row, "|") {
			value, err := strconv.ParseInt(v, 10, 64)
			if err != nil {
				panic(fmt.Sprintf("配置表错误：%v %v %v %v %v", fs, sheetName, line, sheetHead.Type, row))
			}
			ret = append(ret, value)
		}
		return ret
	case "arraystring":
		ret := make([]json.RawMessage, 0)
		if row == "" {
			return ret
		}
		for _, v := range strings.Split(row, "|") {
			ret = append(ret, json.RawMessage(`"`+v+`"`))
		}
		return ret
	}
	return nil
}

func handleOneRow(fs string, sheetName string, line int, row []string, sheetTable *SheetTable) {
	rowCell := make([]interface{}, 0)
	for i, sheetHead := range sheetTable.Head {
		value := ""
		if len(row) >= i+1 {
			value = row[i]
		}

		cellValue := handleOneCell(fs, sheetName, line, value, sheetHead)
		rowCell = append(rowCell, cellValue)
	}
	sheetTable.Rows = append(sheetTable.Rows, rowCell)
}

func handleRows(fs string, sheetName string, rows [][]string) *SheetTable {
	descRow := rows[0]
	typeRow := rows[1]
	nameRow := rows[2]
	checkRow := rows[3]

	if len(typeRow) != len(nameRow) {
		panic(fmt.Sprintf("表头长度错误：%v %v len(typeRow)%v != len(nameRow)%v", fs, sheetName, len(typeRow), len(nameRow)))
	}

	oneTable := &SheetTable{}
	oneTable.FileName = fs
	oneTable.SheetName = sheetName
	//表头解析
	for i := 0; i < len(nameRow); i++ {
		valueDesc := ""
		if len(descRow) >= i+1 {
			valueDesc = strings.Replace(descRow[i], " ", "", -1)
		}

		valueType := ""
		if len(typeRow) >= i+1 {
			valueType = strings.Replace(typeRow[i], " ", "", -1)
		}

		valueName := ""
		if len(nameRow) >= i+1 {
			valueName = strings.Replace(nameRow[i], " ", "", -1)
		}

		valueCheck := ""
		if len(checkRow) >= i+1 {
			valueCheck = strings.Replace(checkRow[i], " ", "", -1)
		}

		//分开客户端服务器
		IsSvr := true
		IsCli := true
		if strings.HasPrefix(valueType, "$") {
			IsSvr = false
		} else if strings.HasPrefix(valueType, "#") {
			IsCli = false
		}
		valueType = strings.Replace(valueType, "$", "", -1)
		valueType = strings.Replace(valueType, "#", "", -1)

		oneHead := &SheetHead{}
		oneHead.Desc = valueDesc
		oneHead.Type = valueType
		oneHead.Name = valueName
		oneHead.Check = valueCheck
		oneHead.IsCli = IsCli
		oneHead.IsSvr = IsSvr

		oneTable.Head = append(oneTable.Head, oneHead)
	}

	for rowline := 4; rowline < len(rows); rowline++ {
		handleOneRow(fs, sheetName, rowline, rows[rowline], oneTable)
	}

	return oneTable
}

func handleSheet(fs string, xlsx *excelize.File, sheetName string, _tmpWg *sync.WaitGroup) {
	defer func() {
		_tmpWg.Done() //减去一个计数
	}()

	if !strings.HasPrefix(sheetName, "@") {
		return
	}

	IsSvr := true
	IsCli := true
	if strings.Index(sheetName, "$") == 1 {
		IsSvr = false
	} else if strings.Index(sheetName, "#") == 1 {
		IsCli = false
	}

	rows, err := xlsx.GetRows(sheetName)
	if err != nil {
		panic(err)
	}

	if len(rows) < 4 {
		panic(fmt.Sprintf(".xlsx有问题，行数不对 %v %v", fs, sheetName))
	}

	sheetName = strings.Replace(sheetName, "@", "", -1)
	sheetName = strings.Replace(sheetName, "#", "", -1)
	sheetName = strings.Replace(sheetName, "$", "", -1)

	if len(sheetName) == 0 {
		panic(fmt.Sprintf("Sheet名字错误: %v %v", fs, sheetName))
	}

	mlock.Lock()
	sheetTable, ok := sheetlist[sheetName]
	if ok {
		panic(fmt.Sprintf("Sheet名字已经存在: %v %v %v", fs, sheetName, sheetTable.FileName))
	}
	mlock.Unlock()

	log.Println(fs, sheetName)
	sheetTable = handleRows(fs, sheetName, rows)
	sheetTable.IsCli = IsCli
	sheetTable.IsSvr = IsSvr

	mlock.Lock()
	sheetlist[sheetName] = sheetTable
	mlock.Unlock()
}

func handleFile(fs string) {
	xlsxFile, err := excelize.OpenFile(fs)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer func() {
		// Close the spreadsheet.
		if err := xlsxFile.Close(); err != nil {
			fmt.Println(err)
		}
		runtime.GC()
		wg.Done() //减去一个计数
	}()

	var _tmpWg sync.WaitGroup
	for _, sheetName := range xlsxFile.GetSheetList() {
		_tmpWg.Add(1) //添加一个计数
		go handleSheet(fs, xlsxFile, sheetName, &_tmpWg)
	}
	_tmpWg.Wait() //阻塞直到所有任务完成
}

/**
 * 获取文件列表。只获取一级目录下的。
 * @param	dirPath		目录
 * @param	suffix		过滤文本
 * @return	文件列表，错误
 */
func ListDir(dirPath string, suffix string) (files []string, err error) {
	files = make([]string, 0)
	dir, err := ioutil.ReadDir(dirPath)
	if err != nil {
		return nil, err
	}
	pathSep := string(os.PathSeparator)
	suffix = strings.ToUpper(suffix)
	for _, fi := range dir {
		absPath := dirPath + pathSep + fi.Name()
		if fi.IsDir() {
			_files, _ := ListDir(absPath, suffix)
			files = append(files, _files...)
			continue
		}
		if strings.HasSuffix(strings.ToUpper(fi.Name()), suffix) {
			files = append(files, absPath)
		}
	}
	return files, nil
}

func CreateFileDir(path string) {
	_, err := os.Stat(path)
	if os.IsExist(err) {
		err = os.Remove(path)
		if err != nil {
			panic(fmt.Sprintf("路径删除失败：%v", path))
		}
	}

	err = os.MkdirAll(path, os.ModePerm)
	if err != nil {
		panic(fmt.Sprintf("路径创建失败：%v", path))
	}
}

//func OutPutProtobuf() {
//	funcMap := template.FuncMap{
//		"ToUpper": Ucfirst,
//	}
//
//	if itemp != "" && otemp != "" {
//		b, err := ioutil.ReadFile(itemp)
//		if err != nil {
//			panic("ioutil.ReadFile", err)
//			return
//		}
//
//		sd.PKGN = *pkgn
//
//		of, err := os.Create(otemp)
//		if err != nil {
//			panic("os.Create", err)
//			return
//		}
//
//		tmpl, err := template.New("name").Funcs(funcMap).Parse(string(b))
//		if err != nil {
//			panic("template.New err:", err)
//			return
//		}
//
//		err = tmpl.Execute(of, sd)
//		if err != nil {
//			panic("tmpl.Execute err:", err)
//			return
//		}
//	}
//}

func OutPutJson(sheetName string, sheetTable *SheetTable) {
	if sheetTable.IsCli {
		cJsonPath := filepath.Join(*cJsonDir, sheetName+".json")
		err := os.MkdirAll(cJsonPath, os.ModePerm)
		if err != nil {
			panic(fmt.Sprintf("文件创建失败：%v", cJsonPath))
		}

		for _, row := range sheetTable.Rows {
			for i, cell := range row {
				head := sheetTable.Head[i]
				head.Name
				switch head.Type {
				case "int":
					cell
				case "string":
					json.RawMessage(`"` + cell + `"`)
				case "intKV":

				case "stringKV":

				case "arrayint":

				case "arraystring":

				}

			}
		}

	}

	if sheetTable.IsSvr {
		sJsonPath := filepath.Join(*sJsonDir, sheetName+".json")
	}
}

func DataCheck(sheetName string, sheetTable *SheetTable) {
	for i, sheetHead := range sheetTable.Head {
		CheckFuncList := strings.Split(sheetHead.Check, "|")
		for _, CheckFuncStr := range CheckFuncList {
			if strings.Index(CheckFuncStr, "unique") == 1 {
				//唯一性检查
				uniqueMap := make(map[interface{}]bool, 0)
				for line, row := range sheetTable.Rows {
					cell := row[i]

					_, ok := uniqueMap[cell]
					if ok {
						panic(fmt.Sprintf("配置表unique错误：%v %v %v %v %v", sheetTable.FileName, sheetTable.SheetName, line+4, sheetHead.Type, row))
					} else {
						uniqueMap[cell] = true
					}
				}
				uniqueMap = nil

			} else if strings.Index(CheckFuncStr, "exist") == 1 {
				//关联性检查
				//for _, row := range sheetTable.Rows {
				//	cell := row[i]
				//}
			}
		}

	}
}

func main() {
	flag.Parse()

	files, err := ListDir(*workDir, ".xlsx")
	if err != nil {
		panic(fmt.Sprintf("%v %v", err, *workDir))
		return
	}

	//加载数据
	for _, v := range files {
		wg.Add(1) //添加一个计数
		go handleFile(v)
	}
	wg.Wait() //阻塞直到所有任务完成

	//数据正确性检查
	for sheetName, sheetTable := range sheetlist {
		wg.Add(1) //添加一个计数
		go DataCheck(sheetName, sheetTable)
	}
	wg.Wait() //阻塞直到所有任务完成

	//生成json配置
	CreateFileDir(*cJsonDir) //客户端json输出目录
	CreateFileDir(*sJsonDir) //服务端json输出目录
	for sheetName, sheetTable := range sheetlist {
		wg.Add(1) //添加一个计数
		go OutPutJson(sheetName, sheetTable)
	}
	wg.Wait() //阻塞直到所有任务完成

	//生成proto
	//CreateFileDir(*cTempDir) //客户端template输出目录
	//CreateFileDir(*sTempDir) //服务端template输出目录
	//for sheetName, sheetTable := range sheetlist {
	//	wg.Add(1) //添加一个计数
	//	go OutPutProtobuf(sheetName, sheetTable)
	//}
	//wg.Wait() //阻塞直到所有任务完成
}
