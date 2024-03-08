package dict

import "testing"

func TestSearch(t *testing.T) {
	dict := Dict{"test": "test value"}

	t.Run("known word", func(t *testing.T) {
		got, _ := dict.Search("test")
		want := "test value"

		AssertStrings(t, got, want)
	})

	t.Run("unknown word", func(t *testing.T) {
		_, got := dict.Search("unknown")

		AssertError(t, got, ErrNotFound)
	})
}