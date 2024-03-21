package main

import (
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestGetPlayers(t *testing.T) {
	request, _ := http.NewRequest(http.MethodGet, "/play/Pepper", nil)
	response := httptest.NewRecorder()

	PlayServer(response, request)

	got := response.Body.String()
	want := "20"

	if got != want {
		t.Errorf("got %q, want %q", got, want)
	}
}