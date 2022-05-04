class Animal:
    def __init__(self, name:str): # self es la instancia (this en c++)
        self.name = name          # __init__ es como un constructor
    def __repr__(self):           # todo es public por default
        return f"Animal(name='{self.name}')"
    def eat(self, food):
        print(f"{self.name} is eating {food}")

charlie = Animal("Charlie")
charlie.eat("an apple")

class Dog(Animal):
    def __repr__(self): # override de __repr__ de Animal
        return f"Dog(name='{self.name}')"
    def bark(self, times:int = 2):
        print(f"{self.name} is barking: {times*'Wuff! '}")
doggy = Dog('Doggy')
doggy.bark(times = 5)
doggy.bark()