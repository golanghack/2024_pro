package usecontext

func (s *StubStore) Fetch() string {
	return s.response
}