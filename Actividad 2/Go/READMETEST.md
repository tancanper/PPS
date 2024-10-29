# README - Pruebas Unitarias para el Conversor de Temperaturas

Este documento describe las pruebas unitarias implementadas para el programa de conversión de temperaturas en Go. Asegura que las funciones de conversión funcionen correctamente y valida que el programa maneje adecuadamente los casos esperados e inesperados.

## Descripción de las Pruebas

Las pruebas unitarias están diseñadas para validar el comportamiento de las funciones `CelsiusAFahrenheit` y `FahrenheitACelsius`. Se utilizan tres pruebas para evaluar los siguientes escenarios:

- Conversión correcta de 0 °C a 32 °F.
- Conversión correcta de 32 °F a 0 °C.
- Un caso de prueba que está diseñado para fallar intencionalmente, verificando que el sistema maneje correctamente errores.

## Ejecutar las Pruebas

Para ejecutar las pruebas unitarias, sigue estos pasos:

1. **Instala Go**: Asegúrate de que Go esté instalado en tu máquina.

2. **Abre la Terminal**: Navega al directorio donde se encuentra el archivo `conversor_test.go` utilizando la terminal.

3. **Ejecuta las Pruebas**: Utiliza el siguiente comando para ejecutar todas las pruebas unitarias:

   ```bash
   go test
   ```

4. **Ver Resultados**: Después de ejecutar el comando, la terminal mostrará el resultado de las pruebas. Verás información sobre si las pruebas pasaron o fallaron.


