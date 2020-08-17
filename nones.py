def impar(limite):
    """Función impares
    Regresa lista de numero impares teniendo como límite el numero ingresado
    Recibe n = un número entero positivo por parte del usuario
    Returns lista de números impares de 1 a n
    """
    if limite >= 0:
        for numero in range(1, limite+1, 2):
            print (numero)
    else:
        print("Número no válido.")

def run():
    impar(int(input("Ingresa un límite para la lista de impares: ")))

if __name__ == "__main__":
    run()