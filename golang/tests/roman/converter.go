package roman

import (
	"strings"
)

func ConverterToRoman(arabic int) string {
	var result strings.Builder

	for _, numeral := range AllRomanNumerical {
		for arabic >= numeral.Value {
			result.WriteString(numeral.Symbol)
			arabic -= numeral.Value
		}
	}
	return result.String()
}

func ConverterToArabic(roman string) int {
	var arabic = 0
	for _, numeral := range AllRomanNumerical {
		for strings.HasPrefix(roman, numeral.Symbol) {
			arabic += numeral.Value
			roman = strings.TrimPrefix(roman, numeral.Symbol)
		}
	}
	return arabic
}
