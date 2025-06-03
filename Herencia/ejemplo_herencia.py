class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} hace un sonido.")

class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau!")

class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Miau!")

perro = Perro("Rex")
gato = Gato("Luna")

perro.hablar()
gato.hablar()
