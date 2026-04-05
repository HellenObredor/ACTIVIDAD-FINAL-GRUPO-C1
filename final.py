#Sainner Solano y Hellen Pimienta

from abc import ABC, abstractmethod

class Shinobi(ABC):
    def __init__(self, nombre, clan):
        self.nombre = nombre
        self.clan = clan
        
    @abstractmethod
    def atacar(self):
            pass
        
    @abstractmethod
    def __str__(self):
            pass
        
class Jutsu:
    def usarJutsu(self):
        print("Usando jutsu...")
                
class Destreza:
    def usarDestreza(self):
        print("Usando destreza...")

class Jonin(Shinobi, Jutsu, Destreza):
    def __init__(self, nombre, clan, nivelChakra):
        super().__init__(nombre, clan)
        self._nivelChakra = nivelChakra
        
    @property
    def nivelChakra(self):
        return self._nivelChakra
    
    @nivelChakra.setter
    def nivelChakra(self, valor):
        if valor > 0 and valor <= 1000:
            self._nivelChakra = valor
        else:
            print("Este ninja realmente existe?.")

    def atacar(self):
        print(f"{self.nombre} ataca con un jutsu poderoso!")
        
    def __str__(self):
        return f"Jonin: {self.nombre}, Clan: {self.clan}, Nivel de Chakra: {self.nivelChakra}"
    
    def entrenar(self):
        self._nivelChakra += 50
        print(f"{self.nombre} ha entrenado. Chakra actual: {self._nivelChakra}")

    def estadoChakra(self):
        if self._nivelChakra > 700:
            return "Chakra alto "
        elif self._nivelChakra > 300:
            return "Chakra medio "
        else:
            return "Chakra bajo "
        
    def invocarBestia(self):
        if self._nivelChakra >= 600:
            print(f"{self.nombre} invoca una bestia poderosa ")
        else:
            print(f"{self.nombre} no tiene suficiente chakra para invocar una bestia ")
    
    
def main():

    n1 = Jonin("Naruto", "Uzumaki", 500)
    n2 = Jonin("Sasuke", "Uchiha", 450)
    n3 = Jonin("Kakashi", "Hatake", 400)
    n4 = Jonin("Itachi", "Uchiha", 600)
    n5 = Jonin("Gaara", "Sabaku", 550)

    jonins = [n1, n2, n3, n4, n5]

    print("-" * 40)
    print("POLIMORFISMO EN ACCIÓN")
    print("-" * 40)

    for ninja in jonins:
        print(ninja)
        ninja.atacar()
        ninja.usarJutsu()
        ninja.usarDestreza()
        print(ninja.estadoChakra())
        ninja.entrenar()
        ninja.invocarBestia()
        print("-" * 40)

    print("\nENCAPSULAMIENTO PARA TODOS LOS NINJAS")
    print("=" * 50)

    for ninja in jonins:
        print(f"\nNINJA: {ninja.nombre}")
        print("-" * 50)
    
        print(f"Chakra actual: {ninja.nivelChakra}")
    
        ninja.nivelChakra += 100
        print(f"Chakra después de entrenamiento: {ninja.nivelChakra}")
    
        print("Intento de chakra inválido (-50)")
        ninja.nivelChakra = -50
    
        print(f"Chakra final válido: {ninja.nivelChakra}")
        print("=" * 50)

if __name__ == "__main__":
    main()