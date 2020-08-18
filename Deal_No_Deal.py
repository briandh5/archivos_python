titulo = """Deal or no deal
Estás listo para el millón de dólares?:
Como te llamas?
Nombre: """
portafolios = """1  2  3  4  5
6  7  8  9 10
11 12  13  14  15
16  17  18 19  20 
21  22  23  24  25 26
"""
premios = [0.1, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
acomodo = []

import random

def run():
    player1 = input(titulo)
    personal = int(input(f"{portafolios} Elige un portafolio, {player1}: "))
    if personal in range(1, 27):    
        indice_portafolio = personal-1
        #personal = int(personal) - 1
        print(premios)
        for i in range(0,26):
            azar = random.choice(premios)
            premios.remove(azar)
            acomodo.append(azar)
            print(acomodo[i])
        print(f"Su portafolios es el numero {personal} y contiene {acomodo[indice_portafolio]} dolares")
    else:
        print("Elija bien")
        run()

def juego():
    pass

if __name__ == "__main__":
    run()
