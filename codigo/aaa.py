print("Conversor")
print("1. Celcius a Fahrenheit")
print("2. Fahrenheit a Celcius")

opcion = int(input("Elige una opción: "))

if opcion == 1:
    c = float(input("Introduce los grados celcius: "))
    g = (c * 9/5) + 32
    print(f"{c} ºC equivalen a {g} ºF")
elif opcion == 2:
    f = float(input("Introduce los grados fahrenheit: "))
    g = (f - 32) * 5/9
    print(f"{f} ºF equivalen a {g} ºC")
else:
    print("Error.")
