// ConfigData json格式
class ConfigData {
{{range $i, $v := .CS}}
	// {{$v.Name}} {{$v.Name}}
	{{- if $v.Array}}
	{{$v.Name}}: Array<{{$v.Name}}ConfigType> 
	{{- else}}
	{{$v.Name}}: Map<string, {{$v.Name}}ConfigType>
	{{- end}}
{{end}}
}

{{- range $i, $v := .CS}}

// {{$v.Name}}ConfigType {{$v.Name}}ConfigType
class {{$v.Name}}ConfigType {
{{range $ii, $vv := $v.SC}}
	// {{$vv.Name}} {{$vv.Comment}}
	{{- if eq $vv.Type "int"}}
	{{$vv.Name}}: number
	{{- else if eq $vv.Type "arrayint1"}}
	{{$vv.Name}}: Array<number>
	{{- else if eq $vv.Type "arrayint2"}}
	{{$vv.Name}}: Array<Array<number>>
	{{- else if eq $vv.Type "arrayint3"}}
	{{$vv.Name}}: Array<Array<Array<number>>>
	{{- else if eq $vv.Type "string"}}
	{{$vv.Name}}: string
	{{- else if eq $vv.Type "arraystring1"}}
	{{$vv.Name}}: Array<string>
	{{- else if eq $vv.Type "arraystring2"}}
	{{$vv.Name}}: Array<Array<string>>
	{{- else if eq $vv.Type "arraystring3"}}
	{{$vv.Name}}: Array<Array<Array<string>>>
	{{- else if eq $vv.Type "mapint"}}
	{{$vv.Name}}: Map<string, number>
	{{- else if eq $vv.Type "mapint1"}}
	{{$vv.Name}}: Map<string, Array<number>>
	{{- else if eq $vv.Type "mapint2"}}
	{{$vv.Name}}: Map<string, Array<Array<number>>>
	{{- else if eq $vv.Type "mapint3"}}
	{{$vv.Name}}: Map<string, Array<Array<Array<number>>>>
	{{- else if eq $vv.Type "mapstring"}}
	{{$vv.Name}}: Map<string, string>
	{{- else if eq $vv.Type "mapstring1"}}
	{{$vv.Name}}: Map<string, Array<string>>
	{{- else if eq $vv.Type "mapstring2"}}
	{{$vv.Name}}: Map<string, Array<Array<string>>>>
	{{- else if eq $vv.Type "mapstring3"}}
	{{$vv.Name}}: Map<string, Array<Array<Array<string>>>>
	{{- end}}
{{end}}
}
{{- end}}