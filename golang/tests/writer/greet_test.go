package main

import (
	"bytes"
	"testing"
)

func TestGreet(t *testing.T) {
	buffer := bytes.Buffer{}
	Greet(&buffer, "One")

	got := buffer.String()
	want := "Hello, One"

	if got != want {
		t.Errorf("got %q want %q", got, want)
	}
}