package renderer

const (
	postTemplate = `<h1>{{.Title}}</h1><p>{{.Desc}}</p>Tags: <ul>{{range .Tags}}<li>{{.}}</li>{{end}}</ul>`
	
)