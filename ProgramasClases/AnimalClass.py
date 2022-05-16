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
    def __eq__(self, other): # este metodo sobrecarga el == de object
        if self is other: # si son el mismo puntero, eso se va a ciclar si usa == though
            return True
        if isinstance(other, Animal):
            return self.name == other.name # este == si sirve porque esta usando el == del str
        return False
        
        
doggy = Dog('Doggy')
doggy.bark(times = 5)
doggy.bark()

issubclass(Dog, Animal) #True
issubclass(Animal, Dog) #False
issubclass(Dog, Dog) #True toda clases es subclase de si misma
'''
Para A y B dominio y Codominio igual (A = B)
R es reflexiva is para todo x: x se relaciona a si mismo
matriz reflexiva es una diagonal, porque solo tiene unos o verdaderos (una relacion) en la diagonal

una flecha que se dirige de un nodo a si mismo se llama un lazo

'''

'''
si R es simetrica: para todo x y y x se relacione a y y y a x
'''

'''
si R es transitiva: para todo x y z x relacionado con y y y relacionado con z entonces x relacionado con z
'''

#una subclase es reflexiva simetrica y transitiva

'''

'''

anotherdog = Dog('Doggy')
print(doggy == anotherdog) 

#doggy == anotherdog daria False si no se hace el __eq__ en la clase porque se evaluan los punteros aunque los atributos del objeto son los mismos el path del objeto es diferente
# Toda clase en Python viene de una clase "object" (todos heredan el == de object, que evalua punteros no atributos (diferentes instancias))
