package main

import "fmt"

func main() {
	fmt.Println("Starting textio server")
	// Single line comments starts with "//"
	costPerMessage := 0.02
	numMessages := 4

	totalCost := costPerMessage * float64(numMessages)
	fmt.Println(totalCost)

	var uName string = "Sandeep"
	var pwd string = "mvSTwe$321"

	fmt.Println("Auth", uName+pwd)

	// Go is strongly typed, which means that accidental type
	// changes in the future will not happen.

}
