package main

import "fmt"

func main() {
	sum := 0

	num1 := 10
	num2 := 25

	sum = add(num1, num2)

	fmt.Println("The Sum of num1 and num2  = ", sum)
}

func add(x, y int) int {
	return x + y
}
