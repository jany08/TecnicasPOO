from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def conducir(self):
        pass

class Coche(Vehiculo):
    def encender(self):
        print("El coche está encendido.")

    def conducir(self):
        print("Conduciendo el coche por la carretera.")

mi_coche = Coche()
mi_coche.encender()
mi_coche.conducir()
