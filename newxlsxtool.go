package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"reflect"
	"strconv"
	"strings"
	"text/template"

	//"github.com/360EntSecGroup-Skylar/excelize/v2"
	//"github.com/tidwall/sjson"
	"github.com/tealeg/xlsx"
	"runtime"
	"sync"
	//"github.com/Jeffail/gabs"
	"archive/zip"
	"bytes"
	"compress/flate"
	"encoding/json"
	"io"
	"unicode"
)

type svrDef struct {
	CS   []svrData
	PKGN string
}

type svrData struct {
	Name  string
	Array bool
	SC    []svrCore
}

type svrCore struct {
	Name    string
	Comment string
	Type    string
}

var (
	dir = flag.String("idir", ".", "xlsx dir")

	mapSrc      = flag.String("mapSrc", "./map/", "地图编辑器配置路径")
	clientojson = flag.String("clientojson", "cli.json", "json output")
	serverojson = flag.String("serverojson", "svr.json", "json output")

	clientitemp = flag.String("clientitemp", "", "input template for json struct")
	clientotemp = flag.String("clientotemp", "", "output template for json struct")

	serveritemp = flag.String("serveritemp", "", "input template for json struct")
	serverotemp = flag.String("serverotemp", "", "output template for json struct")

	pkgn = flag.String("pkgn", "excel", "golang package name")

	sheetlist = make(map[string]string)
	climap    = make(map[string]interface{})
	svrmap    = make(map[string]interface{})

	clisd svrDef
	svrsd svrDef

	mlock sync.Mutex
	wg    sync.WaitGroup //定义一个同步等待的组

	errnames = make(map[string]bool)
	errlock sync.Mutex
)

func CheckIsHidden(file os.FileInfo) bool {
	fa := reflect.ValueOf(file.Sys()).Elem().FieldByName("FileAttributes").Uint()
	bytefa := []byte(strconv.FormatUint(fa, 2))
	if bytefa[len(bytefa)-2] == '1' {
		return true
	}
	return false
}

/**
 * 获取文件列表。只获取一级目录下的。
 * @param	dirPath		目录
 * @param	suffix		过滤文本
 * @return	文件列表，错误
 */
func ListDir(dirPath string, suffix string) (files []string, err error) {
	files = make([]string, 0, 100)
	dir, err := ioutil.ReadDir(dirPath)
	if err != nil {
		return nil, err
	}
	pathSep := string(os.PathSeparator)
	suffix = strings.ToUpper(suffix)
	for _, fi := range dir {
		if fi.IsDir() {
			continue
		}
		if CheckIsHidden(fi) {
			continue
		}
		if strings.HasSuffix(strings.ToUpper(fi.Name()), suffix) {
			files = append(files, dirPath+pathSep+fi.Name())
		}
	}
	return files, nil
}

func strEncode(content string) string {
	bf := bytes.NewBuffer([]byte{})
	jsonEncoder := json.NewEncoder(bf)
	jsonEncoder.SetEscapeHTML(false)
	jsonEncoder.Encode(content)
	return bf.String()
}

func str2value(sheet *xlsx.Sheet, rowline, column int, tttt, xxxx string) interface{} {
	_tmp := strings.Split(tttt, "&")
	tttt = _tmp[0]
	valueLen := 0
	if len(_tmp) == 2 {
		valueLen, _ = strconv.Atoi(_tmp[1])
	}

	if tttt == "int" {
		jvi, err := strconv.ParseInt(xxxx, 10, 64)
		if err != nil {
			panic(err)
		}
		return jvi
	} else if tttt == "string" {
		return json.RawMessage(`"` + xxxx + `"`)
	} else if tttt == "mapint" {
		mm := make(map[string]int64)
		if 0 != len(xxxx) {
			kk := strings.Split(xxxx, "$")

			for _, v := range kk {

				if 0 != len(v) {
					kv := strings.Split(v, "@")
					if len(kv) != 2 {
						panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
					}
					vvv, _ := strconv.ParseInt(kv[1], 10, 64)
					mm[kv[0]] = vvv
				}

			}
		}
		return mm
	} else if tttt == "mapstring" {
		mm := make(map[string]json.RawMessage)
		if 0 != len(xxxx) {
			kk := strings.Split(xxxx, "$")

			for _, v := range kk {

				if 0 != len(v) {
					kv := strings.Split(v, "@")
					if len(kv) != 2 {
						panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
					}
					mm[kv[0]] = json.RawMessage(`"` + kv[1] + `"`)
				}

			}
		}
		return mm
	} else if tttt == "mapint1" {
		mm := make(map[string][]int64)
		if 0 != len(xxxx) {
			kk := strings.Split(xxxx, "$")

			for _, v := range kk {

				if 0 != len(v) {
					kv := strings.Split(v, "@")
					if len(kv) != 2 {
						panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
					}

					jvi := make([]int64, 0)
					if 0 != len(kv[1]) {
						jvs := strings.Split(kv[1], "_")
						if valueLen != 0 && len(jvs) != valueLen {
							panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
						}

						for _, v := range jvs {
							jv, _ := strconv.ParseInt(v, 10, 64)
							jvi = append(jvi, jv)
						}
					}
					mm[kv[0]] = jvi
				}

			}
		}
		return mm
	} else if tttt == "mapstring1" {
		mm := make(map[string][]json.RawMessage)
		if 0 != len(xxxx) {
			kk := strings.Split(xxxx, "$")

			for _, v := range kk {

				if 0 != len(v) {
					kv := strings.Split(v, "@")
					if len(kv) != 2 {
						panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
					}

					jvi := make([]json.RawMessage, 0)
					if 0 != len(kv[1]) {
						jvs1 := strings.Split(kv[1], "_")
						if valueLen != 0 && len(jvs1) != valueLen {
							panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
						}
						for _, v1 := range jvs1 {
							jvi = append(jvi, json.RawMessage(`"` + v1 + `"`))
						}
					}
					mm[kv[0]] = jvi
				}

			}
		}
		return mm
	} else if tttt == "mapint2" {
		mm := make(map[string][][]int64)
		if 0 != len(xxxx) {
			kk := strings.Split(xxxx, "$")

			for _, v := range kk {

				if 0 != len(v) {
					kv := strings.Split(v, "@")
					if len(kv) != 2 {
						panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
					}

					jvi := make([][]int64, 0)
					if 0 != len(kv[1]) {
						jvs := strings.Split(kv[1], ";")

						for _, v := range jvs {

							jvi1 := make([]int64, 0)

							if 0 != len(v) {
								jvs1 := strings.Split(v, "_")
								if valueLen != 0 && len(jvs1) != valueLen {
									panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
								}

								for _, v1 := range jvs1 {

									jv, _ := strconv.ParseInt(v1, 10, 64)
									jvi1 = append(jvi1, jv)
								}
							}

							jvi = append(jvi, jvi1)
						}
					}
					mm[kv[0]] = jvi
				}

			}
		}
		return mm
	} else if tttt == "mapstring2" {
		mm := make(map[string][][]json.RawMessage)
		if 0 != len(xxxx) {
			kk := strings.Split(xxxx, "$")

			for _, v := range kk {

				if 0 != len(v) {
					kv := strings.Split(v, "@")
					if len(kv) != 2 {
						panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
					}

					jvi := make([][]json.RawMessage, 0)
					if 0 != len(kv[1]) {
						jvs := strings.Split(kv[1], ";")

						for _, v := range jvs {

							jvi1 := make([]json.RawMessage, 0)

							if 0 != len(v) {
								jvs1 := strings.Split(v, "_")
								if valueLen != 0 && len(jvs1) != valueLen {
									panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
								}

								for _, v1 := range jvs1 {
									jvi1 = append(jvi1, json.RawMessage(`"` + v1 + `"`))
								}
							}

							jvi = append(jvi, jvi1)
						}
					}
					mm[kv[0]] = jvi
				}

			}
		}
		return mm
	} else if tttt == "mapint3" {
		mm := make(map[string][][][]int64)
		if 0 != len(xxxx) {
			kk := strings.Split(xxxx, "$")

			for _, v := range kk {

				if 0 != len(v) {
					kv := strings.Split(v, "@")
					if len(kv) != 2 {
						panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
					}

					jvi := make([][][]int64, 0)
					if 0 != len(kv[1]) {
						jvs := strings.Split(kv[1], "#")

						for _, v := range jvs {

							jvi1 := make([][]int64, 0)

							if 0 != len(v) {
								jvs1 := strings.Split(v, ";")

								for _, v1 := range jvs1 {

									jvi2 := make([]int64, 0)

									if 0 != len(v1) {
										jvs2 := strings.Split(v1, "_")
										if valueLen != 0 && len(jvs2) != valueLen {
											panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
										}

										for _, v2 := range jvs2 {

											jv, _ := strconv.ParseInt(v2, 10, 64)
											jvi2 = append(jvi2, jv)
										}
									}

									jvi1 = append(jvi1, jvi2)
								}
							}

							jvi = append(jvi, jvi1)
						}
					}

					mm[kv[0]] = jvi
				}

			}
		}
		return mm
	} else if tttt == "mapstring3" {
		mm := make(map[string][][][]json.RawMessage)
		if 0 != len(xxxx) {
			kk := strings.Split(xxxx, "$")

			for _, v := range kk {

				if 0 != len(v) {
					kv := strings.Split(v, "@")
					if len(kv) != 2 {
						panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
					}

					jvi := make([][][]json.RawMessage, 0)
					if 0 != len(kv[1]) {
						jvs := strings.Split(kv[1], "#")

						for _, v := range jvs {

							jvi1 := make([][]json.RawMessage, 0)

							if 0 != len(v) {
								jvs1 := strings.Split(v, ";")

								for _, v1 := range jvs1 {

									jvi2 := make([]json.RawMessage, 0)

									if 0 != len(v1) {
										jvs2 := strings.Split(v1, "_")
										if valueLen != 0 && len(jvs2) != valueLen {
											panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
										}

										for _, v2 := range jvs2 {
											jvi2 = append(jvi2, json.RawMessage(`"` + v2 + `"`))
										}
									}

									jvi1 = append(jvi1, jvi2)
								}
							}

							jvi = append(jvi, jvi1)
						}
					}

					mm[kv[0]] = jvi
				}

			}
		}
		return mm
	} else if tttt == "arrayint1" {
		jvi := make([]int64, 0)
		if 0 != len(xxxx) {
			jvs := strings.Split(xxxx, "_")
			if valueLen != 0 && len(jvs) != valueLen {
				panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
			}

			for _, v := range jvs {
				jv, _ := strconv.ParseInt(v, 10, 64)
				jvi = append(jvi, jv)
			}
		}

		return jvi
	} else if tttt == "arraystring1" {
		jvi := make([]json.RawMessage, 0)
		if 0 != len(xxxx) {
			jvs1 := strings.Split(xxxx, "_")
			if valueLen != 0 && len(jvs1) != valueLen {
				panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
			}
			for _, v1 := range jvs1 {
				jvi = append(jvi, json.RawMessage(`"` + v1 + `"`))
			}
		}
		return jvi
	} else if tttt == "arrayint2" {
		jvi := make([][]int64, 0)
		if 0 != len(xxxx) {
			jvs := strings.Split(xxxx, ";")

			for _, v := range jvs {

				jvi1 := make([]int64, 0)

				if 0 != len(v) {
					jvs1 := strings.Split(v, "_")
					if valueLen != 0 && len(jvs1) != valueLen {
						panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
					}

					for _, v1 := range jvs1 {

						jv, _ := strconv.ParseInt(v1, 10, 64)
						jvi1 = append(jvi1, jv)
					}
				}

				jvi = append(jvi, jvi1)
			}
		}

		return jvi
	} else if tttt == "arraystring2" {
		jvi := make([][]json.RawMessage, 0)
		if 0 != len(xxxx) {
			jvs := strings.Split(xxxx, ";")

			for _, v := range jvs {

				jvi1 := make([]json.RawMessage, 0)

				if 0 != len(v) {
					jvs1 := strings.Split(v, "_")
					if valueLen != 0 && len(jvs1) != valueLen {
						panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
					}

					for _, v1 := range jvs1 {
						jvi1 = append(jvi1, json.RawMessage(`"` + v1 + `"`))
					}
				}

				jvi = append(jvi, jvi1)
			}
		}

		return jvi
	} else if tttt == "arrayint3" {
		jvi := make([][][]int64, 0)
		if 0 != len(xxxx) {
			jvs := strings.Split(xxxx, "#")

			for _, v := range jvs {

				jvi1 := make([][]int64, 0)

				if 0 != len(v) {
					jvs1 := strings.Split(v, ";")

					for _, v1 := range jvs1 {

						jvi2 := make([]int64, 0)

						if 0 != len(v1) {
							jvs2 := strings.Split(v1, "_")
							if valueLen != 0 && len(jvs2) != valueLen {
								panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
							}

							for _, v2 := range jvs2 {

								jv, _ := strconv.ParseInt(v2, 10, 64)
								jvi2 = append(jvi2, jv)
							}
						}

						jvi1 = append(jvi1, jvi2)
					}
				}

				jvi = append(jvi, jvi1)
			}
		}

		return jvi
	} else if tttt == "arraystring3" {
		jvi := make([][][]json.RawMessage, 0)
		if 0 != len(xxxx) {
			jvs := strings.Split(xxxx, "#")

			for _, v := range jvs {

				jvi1 := make([][]json.RawMessage, 0)

				if 0 != len(v) {
					jvs1 := strings.Split(v, ";")

					for _, v1 := range jvs1 {

						jvi2 := make([]json.RawMessage, 0)

						if 0 != len(v1) {
							jvs2 := strings.Split(v1, "_")
							if valueLen != 0 && len(jvs2) != valueLen {
								panic(fmt.Sprintf("%s  row:%d  col:%d  %s", sheet.Name, rowline, column, xxxx))
							}

							for _, v2 := range jvs2 {
								jvi2 = append(jvi2, json.RawMessage(`"` + v2 + `"`))
							}
						}

						jvi1 = append(jvi1, jvi2)
					}
				}

				jvi = append(jvi, jvi1)
			}
		}

		return jvi
	}

	key := fmt.Sprintf("%s-%s", sheet.Name, tttt)
	errlock.Lock()
	_, ok := errnames[key]
	if !ok{
		errnames[key] = true
		panic(fmt.Sprintf("%s  %s", sheet.Name, tttt))
	}
	errlock.Unlock()
	return nil
}

func handleRows(sheet *xlsx.Sheet, isArray bool) (cliresp interface{}, cliSC []svrCore, svrresp interface{}, svrSC []svrCore) {

	clinames := make(map[string]bool)
	svrnames := make(map[string]bool)

	descRow := sheet.Rows[0]
	typeRow := sheet.Rows[1]
	nameRow := sheet.Rows[2]

	if isArray {
		cliretval := make([]map[string]interface{}, 0)
		svrretval := make([]map[string]interface{}, 0)

		for rowline := 3; rowline < len(sheet.Rows); rowline++ {

			currRow := sheet.Rows[rowline]
			if len(currRow.Cells) == 0 {
				continue
			}
			currRowKey := currRow.Cells[0].Value
			if len(currRowKey) == 0 {
				continue
			}

			cliretval1 := make(map[string]interface{})
			svrretval1 := make(map[string]interface{})

			for i, c := range currRow.Cells {
				v := c.Value
				v = strings.Replace(v, "\n", "", -1)
				v = strings.Replace(v, "\"", "'", -1)
				v = strings.Trim(v, " ")
				//超出的字段不用
				if len(nameRow.Cells) <= i || len(typeRow.Cells) <= i {
					//fmt.Println(i, cindex, c.Value, rindex)
					continue
				}

				valueType := typeRow.Cells[i].Value
				valueType = strings.Replace(valueType, " ", "", -1)
				valueName := nameRow.Cells[i].Value
				valueName = strings.Replace(valueName, " ", "", -1)
				valueDesc := ""
				if len(descRow.Cells) > i {
					valueDesc = descRow.Cells[i].Value
				}
				valueDesc = strings.Replace(valueDesc, " ", "", -1)
				//值为空
				if 0 == len(valueType) || 0 == len(valueName) {
					continue
				}
				//分开客户端服务器
				isSvr := 1
				isCli := 1
				if strings.Contains(valueType, "&client") {
					isSvr = 0
				} else if strings.Contains(valueType, "&server") {
					isCli = 0
				}
				valueType = strings.Replace(valueType, "&client", "", -1)
				valueType = strings.Replace(valueType, "&server", "", -1)
				valueType = strings.Replace(valueType, "&key", "", -1)

				if 1 == isSvr {
					_, ok := svrnames[valueName]
					if !ok {
						svrnames[valueName] = false

						var sc svrCore
						sc.Name = valueName
						sc.Type = valueType
						sc.Comment = valueDesc
						svrSC = append(svrSC, sc)
					}
				}

				if 1 == isCli {
					_, ok := clinames[valueName]
					if !ok {
						clinames[valueName] = false

						var sc svrCore
						sc.Name = valueName
						sc.Type = valueType
						sc.Comment = valueDesc
						cliSC = append(cliSC, sc)
					}
				}

				//值为空
				if 0 == len(v) {
					continue
				}

				setval := str2value(sheet, rowline, i+1, valueType, v)
				if setval == nil || (reflect.ValueOf(setval).Kind() == reflect.Ptr && reflect.ValueOf(setval).IsNil()) {
					continue
				}

				if 1 == isSvr {
					svrretval1[valueName] = setval
				}

				if 1 == isCli {
					cliretval1[valueName] = setval
				}
			}
			svrretval = append(svrretval, svrretval1)
			cliretval = append(cliretval, cliretval1)
		}
		svrresp = svrretval
		cliresp = cliretval
		return
	} else {
		cliretval := make(map[string]interface{})
		svrretval := make(map[string]interface{})

		for rowline := 3; rowline < len(sheet.Rows); rowline++ {

			currRow := sheet.Rows[rowline]
			if len(currRow.Cells) == 0 {
				continue
			}

			currRowKey := currRow.Cells[0].Value
			if len(currRowKey) == 0 {
				continue
			}

			cliretval1 := make(map[string]interface{})
			svrretval1 := make(map[string]interface{})

			for i, c := range currRow.Cells {
				v := c.Value
				v = strings.Replace(v, "\n", "", -1)
				v = strings.Replace(v, "\"", "'", -1)
				v = strings.Trim(v, " ")
				//超出的字段不用
				if len(nameRow.Cells) <= i || len(typeRow.Cells) <= i {
					//fmt.Println(i, cindex, c.Value, rindex)
					continue
				}

				valueType := typeRow.Cells[i].Value
				valueType = strings.Replace(valueType, " ", "", -1)
				valueName := nameRow.Cells[i].Value
				valueName = strings.Replace(valueName, " ", "", -1)
				valueDesc := ""
				if len(descRow.Cells) > i {
					valueDesc = descRow.Cells[i].Value
				}
				valueDesc = strings.Replace(valueDesc, " ", "", -1)
				//值为空
				if 0 == len(valueType) || 0 == len(valueName) {
					continue
				}

				//分开客户端服务器
				isSvr := 1
				isCli := 1
				if strings.Contains(valueType, "&client") {
					isSvr = 0
				} else if strings.Contains(valueType, "&server") {
					isCli = 0
				}
				valueType = strings.Replace(valueType, "&client", "", -1)
				valueType = strings.Replace(valueType, "&server", "", -1)
				valueType = strings.Replace(valueType, "&key", "", -1)

				if 1 == isSvr {
					_, ok := svrnames[valueName]
					if !ok {
						svrnames[valueName] = false

						var sc svrCore
						sc.Name = valueName
						sc.Type = valueType
						sc.Comment = valueDesc
						svrSC = append(svrSC, sc)
					}
				}

				if 1 == isCli {
					_, ok := clinames[valueName]
					if !ok {
						clinames[valueName] = false

						var sc svrCore
						sc.Name = valueName
						sc.Type = valueType
						sc.Comment = valueDesc
						cliSC = append(cliSC, sc)
					}
				}

				//值为空
				if 0 == len(v) {
					continue
				}

				setval := str2value(sheet, rowline, i+1, valueType, v)
				if setval == nil || (reflect.ValueOf(setval).Kind() == reflect.Ptr && reflect.ValueOf(setval).IsNil()) {
					continue
				}

				if 1 == isSvr {
					svrretval1[valueName] = setval
				}

				if 1 == isCli {
					cliretval1[valueName] = setval
				}
			}
			svrretval[currRowKey] = svrretval1
			cliretval[currRowKey] = cliretval1
		}
		svrresp = svrretval
		cliresp = cliretval
		return
	}
}

//func handleSheet(v, fs string, xlsx *excelize.File) {
func handleSheet(v, fs string, xlsx *xlsx.Sheet) {
	defer func() {
		runtime.GC()
		wg.Done() //减去一个计数
	}()

	if !strings.Contains(v, "@") {
		return
	}

	isSvr := 1
	isCli := 1
	if strings.Contains(v, "$") {
		isSvr = 0
	} else if strings.Contains(v, "#") {
		isCli = 0
	}

	isArray := false
	if strings.Contains(v, "%") {
		isArray = true
	}

	//rows,err := xlsx.GetRows(v)
	//if err!=nil{
	//	panic(err)
	//}
	if len(xlsx.Rows) < 3 {
		log.Fatalln(".xlsx有问题，行数不对", fs, v)
	}

	v = strings.Replace(v, "@", "", -1)
	v = strings.Replace(v, "#", "", -1)
	v = strings.Replace(v, "$", "", -1)
	v = strings.Replace(v, "%", "", -1)

	if len(v) == 0 {
		log.Fatalln("Sheet名字错误", fs, v)
	}

	mlock.Lock()
	fs1, ok := sheetlist[v]
	if ok {
		log.Fatalln("Sheet名字已经存在", fs, v, fs1)
	}
	sheetlist[v] = fs
	mlock.Unlock()

	log.Println(fs, v)

	clival, clisc, svrval, svrsc := handleRows(xlsx, isArray)

	mlock.Lock()
	if 1 == isCli {
		clidata := svrData{}
		clidata.Name = v
		clidata.Array = isArray
		clidata.SC = clisc
		clisd.CS = append(clisd.CS, clidata)
		climap[v] = clival
	}
	if 1 == isSvr {
		svrdata := svrData{}
		svrdata.Name = v
		svrdata.Array = isArray
		svrdata.SC = svrsc
		svrsd.CS = append(svrsd.CS, svrdata)
		svrmap[v] = svrval
	}
	mlock.Unlock()
}

func handleFile(fs string) {
	xlsxFile, err := xlsx.OpenFile(fs)
	if err != nil {
		fmt.Println(err)
		return
	}

	for _, sheet := range xlsxFile.Sheets {
		wg.Add(1) //添加一个计数
		go handleSheet(sheet.Name, fs, sheet)
	}

}

func Ucfirst(str string) string {
	for i, v := range str {
		return string(unicode.ToUpper(v)) + str[i+1:]
	}
	return ""
}

func CreatTemplate(itemp, otemp string, sd svrDef) {

	funcMap := template.FuncMap{
		"ToUpper": Ucfirst,
	}

	if itemp != "" && otemp != "" {
		b, err := ioutil.ReadFile(itemp)
		if err != nil {
			log.Fatalln("ioutil.ReadFile", err)
			return
		}

		sd.PKGN = *pkgn

		of, err := os.Create(otemp)
		if err != nil {
			log.Fatalln("os.Create", err)
			return
		}

		tmpl, err := template.New("name").Funcs(funcMap).Parse(string(b))
		if err != nil {
			log.Fatalln("template.New err:", err)
			return
		}

		err = tmpl.Execute(of, sd)
		if err != nil {
			log.Fatalln("tmpl.Execute err:", err)
			return
		}
	}
}

func getZipBuffer() bytes.Buffer {

	// 声明buffer
	var buf bytes.Buffer
	// 初始化writer
	w := zip.NewWriter(&buf)
	// 设置压缩级别，不指定则默认
	w.RegisterCompressor(zip.Deflate, func(out io.Writer) (io.WriteCloser, error) {
		return flate.NewWriter(out, flate.BestCompression)
	})

	for k, v := range climap {
		// 根据文件名称，writer创建文件
		f, err := w.Create(k + ".json")
		if err != nil {
			fmt.Println(err)
		}
		// 创建的文件写入内容
		if k != "_mapEditConf" {
			val, _ := json.Marshal(v)
			_, err = f.Write(val)
		} else {
			_, err = f.Write(v.([]byte))
		}
		if err != nil {
			fmt.Println(err)
		}
	}

	// 关闭writer.使用defer更舒适
	err := w.Close()
	if err != nil {
		fmt.Println(err)
	}

	return buf
}

func GetFileName(file string) string {
	file = strings.Replace(file, "\\", "/", -1)
	i := strings.LastIndex(file, "/")
	if i == -1 {
		i = strings.LastIndex(file, "\\")
	}
	i++
	e := strings.LastIndex(file, ".")
	if i == -1 {
		i = 0
	}
	if e != -1 {
		return file[i:e]
	}
	return ""
}

func setMapJson() {
	tmpbuf := new(bytes.Buffer)
	tmpbuf.WriteString("{")

	files, _ := ListDir(*mapSrc, ".json")

	i := 0
	for _, file := range files {
		mapJson, err := ioutil.ReadFile(file)
		if err != nil {
			fmt.Println("地图配置表错误：", file)
		} else {
			if i > 0 {
				tmpbuf.WriteString(",")
			}
			i++
			tmpbuf.WriteString(fmt.Sprintf("\"%s\":%s", GetFileName(file), string(mapJson)))
		}
	}
	tmpbuf.WriteString("}")
	climap["_mapEditConf"] = tmpbuf.Bytes()
}

func CreateFileDir(file string) {
	dir := GetFileDir(file)
	if !IsExist(dir) {
		os.MkdirAll(dir, os.ModePerm)
	}
}
func IsExist(file string) bool {
	_, err := os.Stat(file)
	return !os.IsNotExist(err)
}

func GetFileDir(file string) string {
	i := strings.LastIndex(file, "/")
	if i == -1 {
		i = strings.LastIndex(file, "\\")
	}
	if i != -1 {
		return file[:i]
	}
	return file
}

func main() {

	flag.Parse()

	fs, err := ListDir(*dir, ".xlsx")
	if err != nil {
		log.Fatalln(err, *dir)
		return
	}

	if len(fs) == 0 {
		log.Fatalln("未找到xlsx文件", *dir)
		return
	}

	for _, v := range fs {
		handleFile(v)
	}

	wg.Wait() //阻塞直到所有任务完成
	svrstr, _ := json.Marshal(svrmap)
	CreateFileDir(*serverojson)
	err = ioutil.WriteFile(*serverojson, svrstr, os.ModePerm)
	if err != nil {
		panic(err)
	}

	// 写zip文件数据流
	setMapJson()
	buf := getZipBuffer()
	CreateFileDir(*clientojson)
	err = ioutil.WriteFile(*clientojson, buf.Bytes(), os.ModePerm)
	if err != nil {
		panic(err)
	}

	CreateFileDir(*clientotemp)
	CreateFileDir(*serverotemp)
	CreatTemplate(*clientitemp, *clientotemp, clisd)
	CreatTemplate(*serveritemp, *serverotemp, svrsd)

}
