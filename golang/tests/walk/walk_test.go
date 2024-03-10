package walk

import (
	"reflect"
	"testing"
)

func TestWalk(t *testing.T) {
	cases := []struct {
		Name          string
		Input         interface{}
		ExpectedCalls []string
	}{
		{
			"struct with one string field",
			struct {
				Name string
			}{"One"},
			[]string{"One"},
		},
		{
			"struct with two string fields",
			struct {
				Name string
				City string
			}{
				"One", "Madrid",
			},
			[]string{"One", "Madrid"},
		},
		{
			"struct with non string field",
			struct {
				Name string
				Age  int
			}{
				"One", 33,
			},
			[]string{"One"},
		},
	}
	for _, test := range cases {
		t.Run(test.Name, func(t *testing.T) {
			var got []string
			Walk(test.Input, func(input string) {
				got = append(got, input)
			})
			if !reflect.DeepEqual(got, test.ExpectedCalls) {
				t.Errorf("got %v, want %v", got, test.ExpectedCalls)
			}
		})
	}
}
