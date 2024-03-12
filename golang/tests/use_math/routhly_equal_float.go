package usemath

import "math"

func RouthlyEqualFloat(a, b float64) bool {
	const equalThreshold = 1e-7
	return math.Abs(a - b) < equalThreshold
}