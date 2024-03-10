package selectwebsites

import (
	"testing"
	"time"
)

func TestRacer(t *testing.T) {
	t.Run("compares speeds of servers, return url of the faster", func(t *testing.T) {
		slowServer := MakeServer(20 * time.Millisecond)
		fastServer := MakeServer(0 * time.Millisecond)

		defer slowServer.Close()
		defer fastServer.Close()

		slowUrl := slowServer.URL
		fastUrl := fastServer.URL

		want := fastUrl
		got, _ := Racer(slowUrl, fastUrl)

		if got != want {
			t.Errorf("got %q want %q", got, want)
		}
	})

	t.Run("returns an error if a server doesnt respond withon 10s", func(t *testing.T) {
		serverA := MakeServer(11 * time.Second)
		serverB := MakeServer(12 * time.Second)

		defer serverA.Close()
		defer serverB.Close()
		_, err := Racer(serverA.URL, serverB.URL)
		if err == nil {
			t.Error("expected an error but didn`t get one")
		}
	})

	t.Run("compares speeds of servers, returning the url faster one", func(t *testing.T) {
		slowServer := MakeServer(2 * time.Millisecond)
		fastServer := MakeServer(0 * time.Millisecond)

		defer slowServer.Close()
		defer fastServer.Client()

		slowUrl := slowServer.URL
		fastUrl := fastServer.URL

		want := fastUrl
		got, err := Racer(slowUrl, fastUrl)

		if err != nil {
			t.Fatalf("did not expect -> error -> %v", err)
		}
		if got != want {
			t.Errorf("got %q wnat %q", got, want)
		}
	})

	t.Run("return an error if a server doesnt respond within the specified time", func(t *testing.T) {
		server := MakeServer(25 * time.Millisecond)

		defer server.Close()

		_, err := ConfigurationRacer(server.URL, server.URL, 20*time.Millisecond)
		if err == nil {
			t.Error("expected an error but did not get one")
		}
	})

}
