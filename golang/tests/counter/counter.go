package counter

import "sync"

type Counter struct {
	mu    sync.Mutex
	value int
}
