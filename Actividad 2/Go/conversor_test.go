package main

import "testing"

func TestCelsiusAFahrenheit(t *testing.T) {
	resultado := CelsiusAFahrenheit(0)
	valor := 32.0
	if resultado != valor {
		t.Errorf("CelsiusAFahrenheit(0) = %v; want %v", resultado, valor)
	}
}

func TestFahrenheitACelsius(t *testing.T) {
	resultado := FahrenheitACelsius(32)
	valor := 0.0
	if resultado != valor {
		t.Errorf("FahrenheitACelsius(32) = %v; want %v", resultado, valor)
	}
}

// Test que fallará
func TestFallo(t *testing.T) {
	resultado := CelsiusAFahrenheit(100)
	valor := 200.0 // Intencionalmente incorrecto
	if resultado == valor {
		t.Errorf("CelsiusToFahrenheit(100) = %v; want a different value", resultado)
	}
}
