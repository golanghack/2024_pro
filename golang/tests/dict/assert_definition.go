package dict

import "testing"

func AssertDefinition(t testing.TB, dict Dict, word, definition string) {
	t.Helper()

	got, err := dict.Search(word)
	if err != nil {
		t.Fatal("should find added", err)
	}
	AssertStrings(t, got, definition)
}