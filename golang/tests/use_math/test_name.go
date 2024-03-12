package usemath

import "time"

func TestName(t time.Time) string {
	return t.Format("15:04:05")
}