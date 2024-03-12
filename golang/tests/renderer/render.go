package renderer

import (
	"embed"
	"io"
)

//go:embed templates/*
var postTemplates embed.FS

func (r *PostRenderer) Render (w io.Writer, p Post) error {
	if err := r.templ.ExecuteTemplate(w, "blog.gohtml", p); err != nil {
		return err
	}
	return nil 
}