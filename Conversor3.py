#---------------------------------------------------------------------------------------------
#primera revision de una funcion

def imprimir_mensaje():
    print("Mensaje Especial: ")
    print("Estoy aprendiendo a usar funciones!")

imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()

#---------------------------------------------------------------------------------------------
#creando funciones con opciones

def conversacion(mensaje):
    print("Hola")
    print("Como Estás?")
    print(mensaje)
    print("Adios")

opcion = int(input("Elige una opcion (1, 2, 3): "))
if opcion == 1:
    conversacion("Elegiste la opción 1")
elif opcion == 2:
    conversacion("Elegiste la opción 2")
elif opcion ==3:
    conversacion("Elegiste la opción 3")
else:
    print("Elige una opción valida")

#---------------------------------------------------------------------------------------------
#creando el conversor de monedas con funciones (Modularizando nuestro conversos de monedas)

def suma(a,b):
    print("Se suman dos numeros: ")
    resultado = a + b
    return resultado

sumatoria = suma (1,4)
print(sumatoria)

#---------------------------------------------------------------------------------------------
#creando el conversor de monedas

def conversor(tipo_moneda, valor_dolar):
    moneda = float(input(f"Cuantos {tipo_moneda} tienes?: "))
    dolares = moneda / valor_dolar
    dolares = round(dolares, 2)
    print(f"tienes ${dolares} USD")

menu = """
Bienvenido al conversor de monedas 💰

1 - Lempiras
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """
opcion = int(input(menu))

if opcion == 1:
    #Conversor de Lempiras a Dolares
    conversor("Lempiras", 25)
elif opcion == 2:
    #Conversor de Pesos Argentinos a Dolares
    conversor("Pesos Argentinos", 65)
elif opcion == 3:
    #Conversor de Pesos Mexicanos a Dolares
    conversor("Pesos Mexicanos", 24)
else:
    print("Porfavor, ingresa una opción valida")