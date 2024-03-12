package blogposts_test

import (
	"errors"
	"io/fs"
)

type StubFailFS struct {

}

func (s StubFailFS) Open(name string) (fs.File, error) {
	return nil, errors.New("fail")
}