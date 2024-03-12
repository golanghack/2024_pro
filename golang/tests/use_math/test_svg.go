package usemath

import (
	"bytes"
	"encoding/xml"
	"testing"
	"time"
)

func TestSVGWriterAtMidnight(t *testing.T) {
	tm := time.Date(1337, time.January, 1, 0, 0, 0,0, time.UTC)
	b := bytes.Buffer{}
	SVGWriter(&b, tm)
	svg := Svg{}
	xml.Unmarshal(b.Bytes(), &svg)

	x2 := "150"
	y2 := "60"

	for _, line := range svg.Line {
		if line.X2 == x2 && line.Y2 == y2 {
			return
		}
	}
	t.Errorf("Expected to find the second hand with x2 of %+v and y2 of %+v in the svg out %v", x2, y2, b.String() )
}