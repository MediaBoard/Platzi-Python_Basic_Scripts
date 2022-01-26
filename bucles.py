#---------------------------------------------------------------------------------------------
#Creando Bucles en Python


contador = int(input("Ingresa un numero: "))
print(f"2 elevado a {contador} es igual a: "+str(2**contador))


#Definiendo el ciclo While

def run():
    LIMITE = 1000
    contador = 0
    potencia_2 = 2 ** contador
    while potencia_2 < LIMITE:
        print(f"2 elevado a {contador} es igual a: {potencia_2}")
        contador += 1
        potencia_2 = 2 ** contador


if __name__ == "__main__":
    run()


#---------------------------------------------------------------------------------------------
#Definiendo el ciclo FOR

#de esta forma se resolveria con un ciclo while

def run():
    contador = 0
    while contador < 1001:
        print(f"{contador}")
        contador += 1


if __name__ == "__main__":
    run()


#de esta forma se resuelve en el ciclo FOR

for contador in range(1001):
    print(contador)


#---------------------------------------------------------------------------------------------