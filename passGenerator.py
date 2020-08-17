import random

def password():
    mayusculas = ['A', 'B', 'C', 'D']
    minusculas = ['a', 'b', 'c', 'd']
    numeros = ['1', '2', '3']
    signos = ['%', '$', '/', '(', ')']
    caracteres = mayusculas + minusculas + numeros + signos
    pwd = []

    for i in range(15):
        azar = random.choice(caracteres)
        pwd.append(azar)
        
    pwd = "".join(pwd)
    return pwd



def run():
    pwd = password()
    print('Su nueva contraseña es: ' + pwd)

if __name__ == "__main__":
    run()