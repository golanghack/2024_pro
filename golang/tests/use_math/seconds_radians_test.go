package usemath

import (
	"math"
	"testing"
	"time"
)

func TestSecondsRadians(t *testing.T) {
	cases := []struct {
		time time.Time 
		angle float64
	}{
		{SimpleTime(0, 0, 30), math.Pi},
		{SimpleTime(0, 0, 0), 0},
		{SimpleTime(0, 0, 45), (math.Pi / 2) * 3},
		{SimpleTime(0, 0, 7), (math.Pi / 30) * 7},
	}

	for _, c := range cases {
		t.Run(TestName(c.time), func(t *testing.T) {
			got := SecondsToRadians(c.time)
			if got != c.angle {
				t.Fatalf("wanted %v radians, but got %v", c.angle, got)
			}
		})
	}
}