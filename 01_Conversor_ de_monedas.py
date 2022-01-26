#Conversor de Lempiras a Dolares
Lempiras = input("Cuantos Lempiras tienes?: ")
Lempiras = float(Lempiras)
valor_dolar = 24
dolares = Lempiras / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print(f"Tienes ${dolares} USD")

#Converson de Dolares a Lempiras
Dolares = input("Cuantos dólares tienes?: ")
Dolares = float(Dolares)
valor_lempira = 24
lempiras = Dolares * valor_lempira
lempiras = round(lempiras, 2)
lempiras = str(lempiras)
print(f"Tienes L.{lempiras} lempiras")