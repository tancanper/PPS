def menu():
    print("Conversor")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")

def celsiusafahrenheit():
    #Conversor de celsius a fahrenheit
    c = float(input("Introduce los grados celsius: "))
    t = (c * 9/5) + 32
    print(f"{c} ºC equivalen a {t} ºF")

def fahrenheitacelsius():
    #Conversor de fahrenheit a celsius
    f = float(input("Introduce los grados fahrenheit: "))
    t = (f - 32) * 5/9
    print(f"{f} ºF equivalen a {t} ºC")

def codigo():
    menu()

    opcion = input("Elige una opción: ")
    
    if opcion == '1':
        celsiusafahrenheit()
    elif opcion == '2':
        fahrenheitacelsius()
    else:
        print("Opción no válida.")
        
codigo()
