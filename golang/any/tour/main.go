package main

import "fmt"

func add(x int, y int) int {
	return x + y
}

func main() {
	var a int = 34
	var b int = 56

	fmt.Println(add(a, b))
}