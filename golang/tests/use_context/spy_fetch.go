package usecontext

import "time"

func (s *SpyStore) SpyFetch() string {
	time.Sleep(100 * time.Millisecond)
	return s.response
}