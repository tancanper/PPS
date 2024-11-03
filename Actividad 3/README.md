# Cálculo del Área de un Círculo

Este es un script sencillo en Bash que permite calcular el área de un círculo dado su radio. 

## Descripción

El script solicita al usuario que ingrese el radio del círculo y calcula el área utilizando la fórmula:

A = π * r^2

donde π se aproxima a 3.1416.

## Requisitos

- Un sistema operativo con Bash instalado.
- La herramienta `bc` debe estar instalada para realizar cálculos de precisión.

## Cómo usar

1. Clona o descarga el archivo del script en tu máquina.
2. Abre una terminal y navega hasta el directorio donde se encuentra el script.
3. Asegúrate de que el script tenga permisos de ejecución. Puedes hacer esto con el siguiente comando:

   ```bash
   chmod +x area_circulo.sh
4. Ejecuta el script con el siguiente comando:
   ```bash
   ./area_circulo.sh
# Depuración
Para la depuración del código puedes optar por las siguientes opciones:
   1. Ejecutar el código con el comando:
      ```bash
      bash -x area_circulo.sh
   2. Introducir al inicio del script las siguiente línea:
      ```bash
      set -x
