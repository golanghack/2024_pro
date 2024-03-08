package dict

import "testing"

func TestDelete(t *testing.T) {
	word := "test"
	dict := Dict{word: "test"}
	dict.Delete(word)

	_,err := dict.Search(word)
	if err != ErrNotFound {
		t.Errorf("Expected %q to be deleted", word)
	}
}