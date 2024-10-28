def menu():
    print("Conversor")
    print("1. Celcius a Fahrenheit")
    print("2. Fahrenheit a Celcius")

def celciusafahrenheit():
    #Conversor de celius a fahrenheit
    c = float(input("Introduce los grados celcius: "))
    t = (c * 9/5) + 32
    print(f"{c} ºC equivalen a {t} ºF")

def fahrenheitacelcius():
    #Conversor de fahrenheit a celius
    f = float(input("Introduce los grados fahrenheit: "))
    t = (f - 32) * 5/9
    print(f"{f} ºF equivalen a {t} ºC")

def codigo():
    menu()

    opcion = input("Elige una opción: ")
    
    if opcion == '1':
        celciusafahrenheit()
    elif opcion == '2':
        fahrenheitacelcius()
    else:
        print("Opción no válida.")
        
codigo()
