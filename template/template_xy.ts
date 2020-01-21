// ConfigData json格式
interface ConfigInterface {
{{range $i, $v := .CS}}
	{{$v.Name}}: MapDic<I{{$v.Name|ToUpper}}Conf>;
{{end}}
	_mapEditConf: MapDic<any>;
}

{{- range $i, $v := .CS}}

interface I{{$v.Name|ToUpper}}Conf {
{{range $ii, $vv := $v.SC}}
	/** {{$vv.Comment}} */
	{{- if eq $vv.Type "int"}}
	{{$vv.Name}}: number;
	{{- else if eq $vv.Type "arrayint1"}}
	{{$vv.Name}}: Array<number>;
	{{- else if eq $vv.Type "arrayint2"}}
	{{$vv.Name}}: Array<Array<number>>;
	{{- else if eq $vv.Type "arrayint3"}}
	{{$vv.Name}}: Array<Array<Array<number>>>;
	{{- else if eq $vv.Type "string"}}
	{{$vv.Name}}: string;
	{{- else if eq $vv.Type "arraystring1"}}
	{{$vv.Name}}: Array<string>;
	{{- else if eq $vv.Type "arraystring2"}}
	{{$vv.Name}}: Array<Array<string>>;
	{{- else if eq $vv.Type "arraystring3"}}
	{{$vv.Name}}: Array<Array<Array<string>>>;
	{{- else if eq $vv.Type "mapint"}}
	{{$vv.Name}}: Map<string, number>;
	{{- else if eq $vv.Type "mapint1"}}
	{{$vv.Name}}: Map<string, Array<number>>;
	{{- else if eq $vv.Type "mapint2"}}
	{{$vv.Name}}: Map<string, Array<Array<number>>>;
	{{- else if eq $vv.Type "mapint3"}}
	{{$vv.Name}}: Map<string, Array<Array<Array<number>>>>;
	{{- else if eq $vv.Type "mapstring"}}
	{{$vv.Name}}: Map<string, string>;
	{{- else if eq $vv.Type "mapstring1"}}
	{{$vv.Name}}: Map<string, Array<string>>;
	{{- else if eq $vv.Type "mapstring2"}}
	{{$vv.Name}}: Map<string, Array<Array<string>>>>;
	{{- else if eq $vv.Type "mapstring3"}}
	{{$vv.Name}}: Map<string, Array<Array<Array<string>>>>;
	{{- end}}
{{end}}
}
{{- end}}