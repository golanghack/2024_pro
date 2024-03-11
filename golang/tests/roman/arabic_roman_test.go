package roman

import (
	"fmt"
	"testing"
)

var cases = []struct {
	Description string
	Arabic      int
	Roman       string
}{
	{"1 converted -> I", 1, "I"},
	{"2 converted -> II", 2, "II"},
	{"3 converted -> III", 3, "III"},
	{"4 converted -> IV", 4, "IV"},
	{"5 converted -> V", 5, "V"},
	{"9 converted -> IX", 9, "IX"},
	{"10 converted -> X", 10, "X"},
	{"50 converted -> L", 50, "L"},
	{"100 converted -> C", 100, "C"},
	{"500 converted -> D", 500, "D"},
	{"1000 converted -> M", 1000, "M"},
}

func TestConvertArabicInRoman(t *testing.T) {
	for _, test := range cases {
		t.Run(fmt.Sprintf("%q gets converted to %d", test.Roman, test.Arabic), func(t *testing.T) {
			got := ConverterToArabic(test.Roman)
			if got != test.Arabic {
				t.Errorf("got %d, want %d", got, test.Arabic)
			}
		})
	}
}
