package usecontext

import (
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestServer(t *testing.T) {
	t.Run("tells store to cancel work if request is cancelled", func(t *testing.T) {
		data := "hello"
		store := &SpyStore{response: data}
		serve := Server(store)
		request := httptest.NewRequest(http.MethodGet, "/", nil)

		
	})
}