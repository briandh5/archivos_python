class Celular:
    def __init__(self, marca, capacidad, modelo):
        self.marca = marca
        self.capacidad = capacidad
        self.modelo = modelo
    def prender_wifi(self, marca, modelo):
        print("Prendiendo el wifi de {} {}.".format(marca, modelo))
    def apagar_wifi(self, marca, modelo):
        print("Apagando el wifi de {} {}.".format(marca, modelo))


if __name__ == "__main__":
    tel1 = Celular("Huawei", 32, "Y9")
    tel2 = Celular("Xiaomi", 128, "Pocophone")
    
    tel1.prender_wifi(tel1.marca, tel1.modelo)
    tel2.apagar_wifi(tel2.marca, tel2.modelo)