

{{- range $i, $v := .CS}}

# {{$v.Name}}
class Res{{$v.Name | ToUpper}}(object):
	RES_TABLE = "{{$v.Name}}"
	__slots__ = ({{range $ii, $vv := $v.SC}}"{{$vv.Name}}",{{end}})

    def __init__(self):
		{{range $ii, $vv := $v.SC}}
			# {{$vv.Name}} {{$vv.Comment}}
			{{- if eq $vv.Type "int"}}
			self.{{$vv.Name}} = 0
			{{- else if eq $vv.Type "arrayint1"}}
			self.{{$vv.Name}} = []
			{{- else if eq $vv.Type "arrayint2"}}
			self.{{$vv.Name}} = []
			{{- else if eq $vv.Type "arrayint3"}}
			self.{{$vv.Name}} = []
			{{- else if eq $vv.Type "string"}}
			self.{{$vv.Name}} = ""
			{{- else if eq $vv.Type "arraystring1"}}
			self.{{$vv.Name}} = []
			{{- else if eq $vv.Type "arraystring2"}}
			self.{{$vv.Name}} = []
			{{- else if eq $vv.Type "arraystring3"}}
			self.{{$vv.Name}} = []
			{{- else if eq $vv.Type "mapint"}}
			self.{{$vv.Name}} = {}
			{{- else if eq $vv.Type "mapint1"}}
			self.{{$vv.Name}} = {}
			{{- else if eq $vv.Type "mapint2"}}
			self.{{$vv.Name}} = {}
			{{- else if eq $vv.Type "mapint3"}}
			self.{{$vv.Name}} = {}
			{{- else if eq $vv.Type "mapstring"}}
			self.{{$vv.Name}} = {}
			{{- else if eq $vv.Type "mapstring1"}}
			self.{{$vv.Name}} = {}
			{{- else if eq $vv.Type "mapstring2"}}
			self.{{$vv.Name}} = {}
			{{- else if eq $vv.Type "mapstring3"}}
			self.{{$vv.Name}} = {}
			{{end}}
		{{end}}

    def load_from_json(self, data):
		{{range $ii, $vv := $v.SC}}
			# {{$vv.Name}} {{$vv.Comment}}
			{{- if eq $vv.Type "int"}}
			self.{{$vv.Name}} = data.get("{{$vv.Name}}",0)
			{{- else if eq $vv.Type "arrayint1"}}
			self.{{$vv.Name}} = data.get("{{$vv.Name}}",[])
			{{- else if eq $vv.Type "arrayint2"}}
			self.{{$vv.Name}} = data.get("{{$vv.Name}}",[])
			{{- else if eq $vv.Type "arrayint3"}}
			self.{{$vv.Name}} = data.get("{{$vv.Name}}",[])
			{{- else if eq $vv.Type "string"}}
			self.{{$vv.Name}} = data.get("{{$vv.Name}}","")
			{{- else if eq $vv.Type "arraystring1"}}
			self.{{$vv.Name}} = data.get("{{$vv.Name}}",[])
			{{- else if eq $vv.Type "arraystring2"}}
			self.{{$vv.Name}} = data.get("{{$vv.Name}}",[])
			{{- else if eq $vv.Type "arraystring3"}}
			self.{{$vv.Name}} = data.get("{{$vv.Name}}",[])
			{{- else if eq $vv.Type "mapint"}}
			self.{{$vv.Name}} = data.get("{{$vv.Name}}",{})
			{{- else if eq $vv.Type "mapint1"}}
			self.{{$vv.Name}} = data.get("{{$vv.Name}}",{})
			{{- else if eq $vv.Type "mapint2"}}
			self.{{$vv.Name}} = data.get("{{$vv.Name}}",{})
			{{- else if eq $vv.Type "mapint3"}}
			self.{{$vv.Name}} = data.get("{{$vv.Name}}",{})
			{{- else if eq $vv.Type "mapstring"}}
			self.{{$vv.Name}} = data.get("{{$vv.Name}}",{})
			{{- else if eq $vv.Type "mapstring1"}}
			self.{{$vv.Name}} = data.get("{{$vv.Name}}",{})
			{{- else if eq $vv.Type "mapstring2"}}
			self.{{$vv.Name}} = data.get("{{$vv.Name}}",{})
			{{- else if eq $vv.Type "mapstring3"}}
			self.{{$vv.Name}} = data.get("{{$vv.Name}}",{})
			{{end}}
		{{end}}

{{- end}}