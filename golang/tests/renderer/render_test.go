package renderer_test

import (
	"bytes"
	"github/golanghack/2024_pro/tree/main/golang/tests/renderer"
	"io"
	"testing"

	approvals "github.com/approvals/go-approval-tests"
)

func TestRender(t *testing.T) {
	var (
		aPost = renderer.Post{
			Title: "Hello",
			Body: "Hello world",
			Desc: "Description",
			Tags: []string{"one", "blog"},
		}
	)
	postRenderer, err := renderer.NewPostRenderer()
	if err != nil {
		t.Fatal(err)
	}
	t.Run("it converts a single post into HTM", func(t *testing.T) {
		buf := bytes.Buffer{}
		err := postRenderer.Render(&buf, aPost)
		if err != nil {
			t.Fatal(err)
		}

		approvals.VerifyString(t, buf.String())
	})
}

func BenchmarkRender(b *testing.B) {
	var (
		aPost = renderer.Post{
			Title: "hello",
			Body: "Hello",
			Desc: "Hello blog",
			Tags: []string{"one", "two"},
		}
	)
	postRenderer, err := renderer.NewPostRenderer()
	if err != nil {
		b.Fatal(err)
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		postRenderer.Render(io.Discard, aPost)
	}
}