package usemath

import (
	"io"
	"time"
	"clockface"
)

func SVGWriter(w io.Writer, t time.Time) {
	io.WriteString(w, clockface.svgStart)
	io.WriteString(w, clockface.bezel)
	SecondHand(w, t)
	io.WriteString(w, clockface.svgEnd)
}