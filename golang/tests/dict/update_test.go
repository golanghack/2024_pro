package dict

import "testing"
func TestUpdate(t *testing.T) {
	t.Run("exists word", func(t *testing.T) {
		word := "test"
		definition := "test value"
		dict := Dict{word: definition}
		newDefinition := "new definition"

		err := dict.Update(word, newDefinition)

		AssertError(t, err, nil)
		AssertDefinition(t, dict, word, newDefinition)
	})
	t.Run("new word", func(t *testing.T) {
		word := "test"
		definition := "test value"
		dict := Dict{}

		err := dict.Update(word, definition)

		AssertError(t, err, ErrDoesNotExists)
	})
}