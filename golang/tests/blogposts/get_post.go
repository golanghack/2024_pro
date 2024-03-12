package blogposts

import (
	"io/fs"
)

func GetPost(filesystem fs.FS, filename string) (Post, error) {
	postFile, err := filesystem.Open(filename)
	if err != nil {
		return Post{}, err
	}
	defer postFile.Close()

	return NewPost(postFile)
}