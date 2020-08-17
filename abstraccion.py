class Television:

    def __init__(self):
        pass

    def mutear(self, volumen=0):
        self._bajar_volumen(volumen)
        self._bajar_brillo()
        self._agregar_imagen_mute()

    def _bajar_volumen(self, volumen):
        print(f"Bajando el volumen al maximo: {volumen}")
    
    def _bajar_brillo(self):
        print("Bajando el brillo")

    def _agregar_imagen_mute(self):
        print("Imagen de mute añadida")

if __name__ == "__main__":
    tele = Television()
    tele.mutear()
