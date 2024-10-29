# README de Pruebas Unitarias

Este documento proporciona información sobre las pruebas unitarias implementadas para el proyecto de conversión de temperaturas en Python.

## Descripción de las Pruebas

Las pruebas unitarias se han implementado para verificar que las funciones de conversión de temperaturas funcionan correctamente. Se han creado tres pruebas:

1. **Conversión de Celsius a Fahrenheit**: Verifica que la conversión de 0 grados Celsius produzca 32 grados Fahrenheit.
2. **Conversión de Fahrenheit a Celsius**: Verifica que la conversión de 32 grados Fahrenheit produzca 0 grados Celsius.
3. **Conversión de Fahrenheit a Celsius (Fallo intencionado)**: Verifica incorrectamente que la conversión de 100 grados Fahrenheit produzca 37 grados Celsius para demostrar cómo manejar un fallo en la prueba.

## Estructura de las Pruebas

Las pruebas están organizadas en un archivo llamado `conversor_test.py`. A continuación se muestra la estructura de las pruebas:

## Ejecución de las priebas

1. Abre la terminal y navega hasta el directorio donde se encuentran los archivos conversor.py y test_conversor.py.
2. Ejecuta el siguiente comando:
```bash
python test_conversor.py
