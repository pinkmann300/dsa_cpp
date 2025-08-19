package main

import "fmt"

func main() {
	fmt.Println("Starting textio server")
	// Single line comments starts with "//"
	var costPerMessage float64 = 0.02
	numMessages := 4

	totalCost := costPerMessage * float64(numMessages)
	fmt.Println(totalCost)

	var uName string = "Sandeep"
	var pwd string = "mvSTwe$321"

	fmt.Println("Auth", uName+pwd)

	// Go is strongly typed, which means that accidental type
	// changes in the future will not happen.

	// Variable representation :
	// var <name> <type>

	// := means go will infer the type itself.

	congrats := "Happy birthday"
	fmt.Println(congrats)

	penniesPerText := 2
	fmt.Printf("type %T\n", penniesPerText)

	averageOpenRate, displayMessages := 0.02, "hello Sandeep"
	fmt.Printf("av %T\n", averageOpenRate)
	fmt.Printf("display msgs %T\n", displayMessages)

	accountAge := 2.6
	accountAgeDisp := int(accountAge)

	fmt.Println(accountAgeDisp)
}
