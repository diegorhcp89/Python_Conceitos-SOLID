class Animal:
    def comer(self):
        print("O Animal está comendo")

    def andar(self):
        print("O Animal está andando na jaula")

class Felino(Animal):
    def lamber(self):
        print("O Felino está lambendo seu pelo")

class Leao(Felino):
    def rugir(self):
        print("O leao esta rugindo alto !!!")

class Pessoa:
    def observa(self, animal: Animal):
        animal.comer()

renatinho = Pessoa()
animal = Animal()
felino = Felino()

renatinho.observa(animal)
#animal.comer()
#felino.comer()