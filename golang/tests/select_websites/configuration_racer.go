package selectwebsites

import (
	"fmt"
	"time"
)

func ConfigurationRacer(slowUrl, fastUrl string, timeout time.Duration) (winner string, error error) {
	select {
	case <-ping(slowUrl):
		return slowUrl, nil
	case <-ping(fastUrl):
		return fastUrl, nil
	case <-time.After(timeout):
		return "", fmt.Errorf("timed out of waiting for %s and %s", slowUrl, fastUrl)
	}
}
