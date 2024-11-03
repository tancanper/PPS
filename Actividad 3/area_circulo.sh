#!/bin/bash

#Calculo del área de un círculo

read -p "Introduce el radio del círculo: " radio

#Calcular el área del círculo
area=$(echo "3.1416 * $radio * $radio" | bc)

echo "El área del círculo es: $area"
