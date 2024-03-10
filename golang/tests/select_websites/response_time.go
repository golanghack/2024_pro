package selectwebsites

import (
	"net/http"
	"time"
)

func ResponseTime(url string) time.Duration {
	start := time.Now()
	http.Get(url)
	return time.Since(start)
}
