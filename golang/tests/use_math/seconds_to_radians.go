package usemath

import (
	"math"
	"time"
)

func SecondsToRadians(t time.Time) float64 {
	return (math.Pi / (30 / (float64(t.Second()))))
}