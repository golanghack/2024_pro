package main

import (
	"testing"
	"time"
)

func TestConfigureableSleeper(t *testing.T) {
	sleepTime := 5 * time.Second

	spyTime := &SpyTime{}
	sleeper := ConfigurableSleeper{sleepTime, spyTime.Sleep}
	sleeper.Sleep()

	if spyTime.durationSlepts != sleepTime {
		t.Errorf("should have slept for %v  but slept for %v", sleepTime, spyTime)
	}
}