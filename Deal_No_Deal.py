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

def run():
    player1 = input(titulo)
    personal = input(f"{portafolios} Elige un portafolio, {player1}: ")
    print(personal)

if __name__ == "__main__":
    run()
