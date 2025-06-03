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

def hacer_hablar(animal):
    animal.hablar()

animales = [Perro("Max"), Gato("Mishi"), Perro("Bobby")]

for a in animales:
    hacer_hablar(a)
