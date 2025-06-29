from abc import ABC, abstractmethod #abstract ve interface icin abs dahil edilmeli

class Animal(ABC): # Animal bir abstract
    def __init__(self, tour):
        self.tour = tour

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def todo(self):
        pass

    # @abstractmethod
    # def nino(self):
    #     pass

class Huntable(ABC):
    @abstractmethod
    def hunt(self):
        pass

class Grazeble(ABC):
    @abstractmethod
    def graze(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass

class Runable(ABC):
    @abstractmethod
    def run(self):
        pass

class Dog(Animal, Huntable, Runable):
    def sound(self):
        print("Hav")

    def todo(self):
        print(self.tour," like meat ")

    def hunt(self):
        print(f"{self.tour} huntable ")

    def run(self):
        print(f"{self.tour} runable ")

class Cat(Animal, Huntable, Runable):
    def sound(self):
        print("Meow")

    def todo(self):
        print(self.tour," like yogurt ")

    def hunt(self):
        print(f"{self.tour} huntable ")

    def run(self):
        print(f"{self.tour} runable ")


class Sheep(Animal, Grazeble, Runable):
    def sound(self):
        print("Meow")

    def todo(self):
        print(self.tour, " like yogurt ")

    def graze(self):
        print(f"{self.tour} can graze ")

    def run(self):
        print(f"{self.tour} runable ")

class Fish(Animal, Swimmable, Huntable, Runable):
    def sound(self):
        print("cici")

    def todo(self):
        print(self.tour, " like water ")

    def swim(self):
        print(self.tour, " swim ")

    def hunt(self):
        print(self.tour, " hunt ")

    def run(self):
        print(self.tour, " can run ")

interface_actions = {
    Huntable: lambda obj: obj.hunt(),  # Dog bu interface'i uyguluyor
    Grazeble: lambda obj: obj.graze(),
    Flyable: lambda obj: obj.fly(),
    Swimmable: lambda obj: obj.swim(),
    Runable: lambda obj: obj.run()
}


animals = [Cat("Cat1"),Sheep("Sheep1"),Fish("Fish1"), Cat("Cat2"),Sheep("Sheep2"),
           Dog("Dog1"), Cat("Cat3"),Dog("Dog2"),Cat("Cat4")]

for animal in animals:
    print(f"--- {animal.tour} ---")  # hayvan adı başlık gibi
    animal.sound()
    animal.todo()
    for interface, action in interface_actions.items():
        if isinstance(animal, interface):
            action(animal)
    print()  # satır boşluğu
