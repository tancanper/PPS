package main

import (
	"fmt"
)

func CelsiusToFahrenheit(celsius float64) float64 {
	return (celsius * 9 / 5) + 32
}

func FahrenheitToCelsius(fahrenheit float64) float64 {
	return (fahrenheit - 32) * 5 / 9
}

func main() {
	var choice int
	fmt.Println("Conversor")
	fmt.Println("1. Celsius a Fahrenheit")
	fmt.Println("2. Fahrenheit a Celsius")
	fmt.Print("Selecciona una opción (1/2): ")
	fmt.Scan(&choice)

	switch choice {
	case 1:
		var celsius float64
		fmt.Print("Introduce la temperatura en Celsius: ")
		fmt.Scan(&celsius)
		fahrenheit := CelsiusToFahrenheit(celsius)
		fmt.Printf("%.2f °C es igual a %.2f °F\n", celsius, fahrenheit)
	case 2:
		var fahrenheit float64
		fmt.Print("Introduce la temperatura en Fahrenheit: ")
		fmt.Scan(&fahrenheit)
		celsius := FahrenheitToCelsius(fahrenheit)
		fmt.Printf("%.2f °F es igual a %.2f °C\n", fahrenheit, celsius)
	default:
		fmt.Println("Opción no válida.")
	}
}
