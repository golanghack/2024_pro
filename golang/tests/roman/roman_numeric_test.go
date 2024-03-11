package roman

import "testing"

func TestRomanNumeric(t *testing.T) {
	cases := []struct {
		Description string
		Arabic      int
		Want        string
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
	for _, test := range cases {
		t.Run(test.Description, func(t *testing.T) {
			got := ConverterToRoman(test.Arabic)

			if got != test.Want {
				t.Errorf("got %q want %q", got, test.Want)
			}
		})
	}

}
