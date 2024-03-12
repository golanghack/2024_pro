package usemath

import (
	"math"
	"time"
)

func SecondHandPoint(t time.Time) Point {
	angle := SecondsToRadians(t)
	x := math.Sin(angle)
	y := math.Cos(angle)

	return Point{x, y}
}