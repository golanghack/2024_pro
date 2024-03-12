package blogposts

import (
	"io/fs"
)

type Post struct {
	Title string
}

func NewPostFromFS(filesystem fs.FS) ([]Post, error) {
	dir, err:= fs.ReadDir(filesystem, ".")
	if err != nil {
		return nil, err
	}
	var posts []Post
	for _, f := range dir {
		post, err := GetPost(filesystem, f)
		if err != nil {
			return nil, err 
		}
		posts = append(posts, post)
	}
	return posts, nil
}