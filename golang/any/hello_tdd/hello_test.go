package main

import "testing"

func assertCorrectmessage(t testing.TB, got, want string) {
	t.Helper()
	if got != want {
		t.Errorf("got %q want %q", got, want)
	}
}


func TestHelloFunction(t *testing.T) {
	t.Run("say hello to people", func(t *testing.T) {
		got := Hello("Linda", "")
		want := "Hello, Linda"
		assertCorrectmessage(t, got, want)
	})

	t.Run("say 'Hello, World' when an empty string supplied", func(t *testing.T) {
		got := Hello("", "")
		want := "Hello, World"
		assertCorrectmessage(t, got, want)
	})

	t.Run("in Spanish", func(t *testing.T) {
		got := Hello("Elodie", "Spanish")
		want := "Hola, Elodie"
		assertCorrectmessage(t, got, want)
	})
	t.Run("in French", func(t *testing.T) {
		got := Hello("Lui", "French") 
		want := "Bomjour, Lui"
		assertCorrectmessage(t, got, want)
	})
	t.Run("in Russian", func(t *testing.T) {
		got := Hello("Boris", "Russian")
		want := "Привет, Boris"
		assertCorrectmessage(t, got, want)
	})
}
