package counter

import (
	"sync"
	"testing"
)

func TestCounter(t *testing.T) {
	t.Run("increment counter 2 times leaves if at 3", func(t *testing.T) {
		counter := NewCounter()
		counter.Inc()
		counter.Inc()
		counter.Inc()

		AssertCount(t, counter, 3)
	})
	t.Run("if runs safety concurrently", func(t *testing.T) {
		wantedCounts := 1000
		counter := NewCounter()

		var wg sync.WaitGroup
		wg.Add(wantedCounts)

		for i := 0; i < wantedCounts; i++ {
			go func() {
				counter.Inc()
				wg.Done()
			}()
		}
		wg.Wait()
		AssertCount(t, counter, wantedCounts)
	})
}
