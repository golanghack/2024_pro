package renderer

import "html/template"

func NewPostRenderer() (*PostRenderer, error) {
	templ, err := template.ParseFS(postTemplates, "templates/*.gohtml")
	if err != nil {
		return nil, err 
	}
	return &PostRenderer{templ: templ}, nil
}