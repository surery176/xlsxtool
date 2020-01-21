表名@表示要导出配置表
%代表这个表是List模式，否则代表Map模式
@# 只导出服务器表
@$ 只导出前端表
@  导出前端、后端表

表第1行：字段描述注释
表第2行：类型
        int             数值,前端对应number,服务器go对应int；
		string          字符串，前后端都对应string
        arrayint1       1维数组，数值类型。前端对应Array<number>,服务器对应[]int
        arrayint2       2维数组，数值类型。前端对应Array<Array<number>>,服务器对应[][]int
        arrayint3       3维数组，数值类型。前端对应<Array<Array<string>>>,服务器对应[][][]int
        arraystring1    1维数组，字符串类型。前端对应Array<string>,服务器对应[]string
        arraystring2    2维数组，字符串类型。前端对应Array<Array<string>>,服务器对应[][]string
        arraystring3    3维数组，字符串类型。前端对应<Array<Array<string>>>,服务器对应[][][]string
		mapint          整数字典，数值类型。前端对应Map<string, number>,服务器对应 map[string]int
		mapstring       字符串字典，字符串类型。前端对应Map<string, string>,服务器对应 map[string]string
		mapint1         1维字典，数值类型。前端对应Map<string, Array<number>>,服务器对应 map[string][]int
        mapint2         2维字典，数值类型。前端对应Map<string, Array<Array<number>>>,服务器对应 map[string][][]int
        mapint3         3维字典，数值类型。前端对应Map<string, <Array<Array<string>>>>,服务器对应 map[string][][][]int
        mapstring1      1维字典，字符串类型。前端对应Map<string, Array<string>>,服务器对应 map[string][]string
        mapstring2      2维字典，字符串类型。前端对应Map<string, Array<Array<string>>>,服务器对应 map[string][][]string
        mapstring3      3维字典，字符串类型。前端对应Map<string, <Array<Array<string>>>>,服务器对应 map[string][][][]string
        类型后面带&client 只前端需要用到，服务器不导出到json配置
        类型后面带&server 只服务器需要用到，前端不导出到json配置

表第3行：字段名，英文命名
表第4行开始为数据

1维数组用 _分割    例如  1_2_3
2维数组用 _;分割   例如  1_2_3;1_2_3
3维数组用 _;#分割 例如  1_2_3;1_2_3#1_2_3;1_2_3

map模式。key与value之间分隔符用@ key与key之间用$，如类型：mapint1 数据keyA@1_2_3$keyA@1_2_3

- 常见模板见template文件夹

导表参数
main.exe -idir D:\\work\\xy\\挂机类\\内网开发配置表 -clientojson D:\\work\\gitRepository\\esj\\out\\cli.json -client
itemp D:\\work\\gitRepository\\esj\\template\\template_xy.ts -clientotemp D:\\work\\gitRepository\\esj\\out\\cli.ts -pkgn packname -serverojson D:\\work\\gitRepository\\esj\\out\\svr.json -serveritemp D:\\work\\gitRepository\\esj\\template\\template.py -serverotemp D:\\work\\gitRepository\\esj\\out\\svr.py -mapSrc D:\\work\\xy\\挂机类\\内网开发配置表\\map
\\