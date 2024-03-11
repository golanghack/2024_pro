package roman

import (
	"log"
	"testing"
	"testing/quick"
)

func TestPropertiesConversions(t *testing.T) {
	assertion := func(arabic int) bool {
		if arabic < 0 || arabic > 3999 {
			log.Println(arabic)
			return true
		}
		roman := ConverterToRoman(arabic)
		fromRoman := ConverterToArabic(roman)
		return fromRoman == arabic
	}

	if err := quick.Check(assertion, nil); err != nil {
		t.Error("failed checks", err)
	}
}
