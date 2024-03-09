package main

import "time"

type SpyTime struct {
	durationSlepts time.Duration
}

func (s *SpyTime) Sleep(duration time.Duration) {
	s.durationSlepts = duration
}