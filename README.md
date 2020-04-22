请使用 newxlsxtool新版导表工具

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
        类型后面带&client 只前端需要用到，服务器不导出到json配置
        类型后面带&server 只服务器需要用到，前端不导出到json配置
		
		数组类型的字段后面再带 &n n为数字，可以强制检查数字长度一定为n，防止配错
		
		arrayint2tomap     py模板特用，客户端还是2维数组，py转换成 {int:int}
		arraystring2tomap   py模板特用，客户端还是2维数组，py转换成 {string:string}

表第3行：字段名，英文命名
表第4行开始为数据

1维数组用 _分割    例如  1_2_3
2维数组用 _;分割   例如  1_2_3;1_2_3
3维数组用 _;#分割 例如  1_2_3;1_2_3#1_2_3;1_2_3

map模式。key与value之间分隔符用_ key与key之间用;，如类型：mapint 数据key_3;key_3

- 常见模板见template文件夹

