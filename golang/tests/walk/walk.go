package walk

import "reflect"

func Walk(x interface{}, fn func(input string)) {
	value := reflect.ValueOf(x)
	for i := 0; i < value.NumField(); i++ {
		field := value.Field(i)
		fn(field.String())
	}
}
