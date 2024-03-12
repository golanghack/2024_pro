package usemath

import (
	"io"
	"time"
)

func SecondHand(w io.Writer,t time.Time) Point {
	p := SecondHandPoint(t)
	p = Point{p.X * secondHandLen, p.Y * secondHandLen}
	p = Point{p.X, -p.Y}
	p = Point{p.X + clockCenterX, p.Y + clockCenterY}
	return p 
}