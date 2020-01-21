package {{.PKGN}}

// ConfigData json格式
type ConfigData struct {
{{range $i, $v := .CS}}
	// {{$v.Name}} {{$v.Name}}
	{{- if $v.Array}}
	{{$v.Name}} []*{{$v.Name}}ConfigType
	{{- else}}
	{{$v.Name}} map[string] *{{$v.Name}}ConfigType
	{{- end}}
{{end}}
}

{{- range $i, $v := .CS}}

// {{$v.Name}}ConfigType {{$v.Name}}ConfigType
type {{$v.Name}}ConfigType struct{
{{range $ii, $vv := $v.SC}}
	// {{$vv.Name}} {{$vv.Comment}}
	{{- if eq $vv.Type "int"}}
	{{$vv.Name}} int64
	{{- else if eq $vv.Type "arrayint1"}}
	{{$vv.Name}} []int64
	{{- else if eq $vv.Type "arrayint2"}}
	{{$vv.Name}} [][]int64
	{{- else if eq $vv.Type "arrayint3"}}
	{{$vv.Name}} [][][]int64
	{{- else if eq $vv.Type "string"}}
	{{$vv.Name}} string
	{{- else if eq $vv.Type "arraystring1"}}
	{{$vv.Name}} []string
	{{- else if eq $vv.Type "arraystring2"}}
	{{$vv.Name}} [][]string
	{{- else if eq $vv.Type "arraystring3"}}
	{{$vv.Name}} [][][]string
	{{- else if eq $vv.Type "mapint"}}
	{{$vv.Name}} map[string]int64
	{{- else if eq $vv.Type "mapint1"}}
	{{$vv.Name}} map[string][]int64
	{{- else if eq $vv.Type "mapint2"}}
	{{$vv.Name}} map[string][][]int64
	{{- else if eq $vv.Type "mapint3"}}
	{{$vv.Name}} map[string][][][]int64
	{{- else if eq $vv.Type "mapstring"}}
	{{$vv.Name}} map[string]string
	{{- else if eq $vv.Type "mapstring1"}}
	{{$vv.Name}} map[string][]string
	{{- else if eq $vv.Type "mapstring2"}}
	{{$vv.Name}} map[string][][]string
	{{- else if eq $vv.Type "mapstring3"}}
	{{$vv.Name}} map[string][][][]string
	{{- end}}
{{end}}
}
{{- end}}