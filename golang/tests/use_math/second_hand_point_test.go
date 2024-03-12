package usemath

import (
	"testing"
	"time"
)

func TestSecondHandPoint(t *testing.T) {
	cases := []struct {
		time time.Time 
		point Point
	}{
		{SimpleTime(0, 0, 30), Point{0, -1}},
		{SimpleTime(0, 0, 45), Point{-1, 0}},
	}
	for _, c := range cases {
		t.Run(TestName(c.time), func(t *testing.T) {
			got := SecondHandPoint(c.time)
			if !RouthlyEqualPoint(got, c.point) {
				t.Fatalf("wanted %v Point, but got %v", c.point, got)
			}
		})
	}
}