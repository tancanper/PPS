package main

import (
	"fmt"
)

func CelsiusAFahrenheit(celsius float64) float64 {
	return (celsius * 9 / 5) + 32
}

func FahrenheitACelsius(fahrenheit float64) float64 {
	return (fahrenheit - 32) * 5 / 9
}

func main() {
	var opcion int
	fmt.Println("Conversor")
	fmt.Println("1. Celsius a Fahrenheit")
	fmt.Println("2. Fahrenheit a Celsius")
	fmt.Print("Selecciona una opción (1/2): ")
	fmt.Scan(&opcion)

	switch opcion {
	case 1:
		var celsius float64
		fmt.Print("Introduce la temperatura en Celsius: ")
		fmt.Scan(&celsius)
		fahrenheit := CelsiusAFahrenheit(celsius)
		fmt.Printf("%.2f °C es igual a %.2f °F\n", celsius, fahrenheit)
	case 2:
		var fahrenheit float64
		fmt.Print("Introduce la temperatura en Fahrenheit: ")
		fmt.Scan(&fahrenheit)
		celsius := FahrenheitACelsius(fahrenheit)
		fmt.Printf("%.2f °F es igual a %.2f °C\n", fahrenheit, celsius)
	default:
		fmt.Println("Opción no válida.")
	}
}
