package main

import "fmt"

func main() {
	fmt.Println("Starting textio server")
	// Single line comments starts with "//"
	costPerMessage := 0.02
	numMessages := 4

	totalCost := costPerMessage * float64(numMessages)
	fmt.Println(totalCost)
}
