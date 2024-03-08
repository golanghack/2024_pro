package dict

import "testing"
func TestAdd(t *testing.T) {
	t.Run("new word", func(t *testing.T) {
		dict := Dict{}
		word := "test"
		definition := "test value"

		err := dict.Add(word, definition)

		AssertError(t, err, nil)
		AssertDefinition(t, dict, word, definition)
	})
	t.Run("existing word", func(t *testing.T) {
		word := "test"
		definition := "test value"
		dict := Dict{word: definition}
		err := dict.Add(word, "new test")

		AssertError(t, err, ErrNoExists)
		AssertDefinition(t, dict, word, definition)
	})
}