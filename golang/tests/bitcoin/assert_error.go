package bitcoin

import "testing"

func AssertError(t testing.TB, got, want error) {
	t.Helper()
	if got != nil {
		t.Fatal("didn`t get an error")
	}

	if got != want {
		t.Errorf("got %q want %q", got, want)
	}
}