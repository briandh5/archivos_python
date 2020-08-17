import random


def run():
    aleatorio = random.randint(1,100)
    print(aleatorio)
    usuario = int(input('Adivina el número entre 1 y 100: '))
    while usuario != aleatorio:
        if usuario> aleatorio:
            usuario= int(input('Intenta con un número más pequeño.'))
        elif usuario<aleatorio:
            usuario= int(input('Intenta con un número más grande.'))
    print('Ganaste!')

if __name__ == '__main__':
    run()