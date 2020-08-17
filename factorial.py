def factorial(num):
    """
    Calcular factorial de num
    num es mayor a cero
    returns n!
    """
    if num == 1:
        return num
    return num * (factorial(num-1))

def run():
    number = int(input("Escribe un entero positivo para sacar su factorial: "))
    print(f' El factorial de {number} es {factorial(number)}')

if __name__ == "__main__":
    run()