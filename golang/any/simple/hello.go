package main

import (
	"fmt"
)

const (
	engHelloPrefix = "Hello, "
 	spanishHelloPrefix = "Hola, "
	frenchHelloPrefix = "Bomjour, "
 	russionHelloPrefix = "Привет, "

	russian = "Russian"
	spanish = "Spanish"
	french = "French"
)

func Hello(name string, lang string) string {
	if name == "" {
		name = "World"
	} 
	return greetAPrefix(lang) + name
}

func greetAPrefix(language string) (prefix string) {
	switch language {
	case french:
		prefix = frenchHelloPrefix
	case russian:
		prefix = russionHelloPrefix
	case spanish:
		prefix = spanishHelloPrefix
	default:
		prefix = engHelloPrefix
	}
	return
}

func main() {
	fmt.Println(Hello(engHelloPrefix, "World"))
}
