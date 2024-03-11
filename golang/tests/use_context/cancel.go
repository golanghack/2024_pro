package usecontext

func (s *SpyStore) Cancel() {
	s.cancelled = true
}