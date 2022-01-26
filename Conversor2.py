menu = """
Bienvenido al conversor de monedas 💰

1 - Lempiras
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """
opcion = int(input(menu))

if opcion == 1:
    #Conversor de Lempiras a Dolares
    Lempiras = input("Cuantos Lempiras tienes?: ")
    Lempiras = float(Lempiras)
    valor_dolar = 25
    dolares = Lempiras / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print(f"Tienes ${dolares} USD")
elif opcion == 2:
    #Conversor de Pesos Argentinos a Dolares
    Pesos_AR = input("Cuantos Pesos Argentinos tienes?: ")
    Pesos_AR = float(Pesos_AR)
    valor_dolar = 65
    dolares = Pesos_AR / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print(f"Tienes ${dolares} USD")
elif opcion == 3:
    #Conversor de Pesos Mexicanos a Dolares
    Pesos_MX = input("Cuantos Pesos Mexicanos tienes?: ")
    Pesos_MX = float(Pesos_MX)
    valor_dolar = 24
    dolares = Pesos_MX / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print(f"Tienes ${dolares} USD")
else:
    print("Porfavor, ingresa una opción valida")