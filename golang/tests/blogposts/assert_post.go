package blogposts_test

import (
	"reflect"
	"testing"

	blogposts "github.com/golanghack/2024_pro/tree/main/golang/tests/blogposts"
)

func assertPost(t *testing.T, got blogposts.Post, want blogposts.Post) {
	t.Helper()
	if !reflect.DeepEqual(got, want) {
		t.Errorf("got %v, want %v", got, want)
	}
}

