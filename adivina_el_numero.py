import random
import sys

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un numero del 1 al 100: "))
    vidas = 10
    while numero_elegido != numero_aleatorio:
        if vidas == 0:
            print("Perdiste, mas suerte para la proxima")
            sys.exit(0)
            break
        vidas -= 1
        if numero_elegido < numero_aleatorio:
            print(f"Busca un numero mas grande, te quedan {vidas} vidas")
        else:
            print(f"Busca un numero mas pequeno, te quedan {vidas} vidas")
        numero_elegido = int(input("Elige otro numero: "))
    print("Felicidades, Ganaste")

if __name__ == "__main__":
    run()