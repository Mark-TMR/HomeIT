
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " Заправляється!")



class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print("Рухається зі швидкістю " + str(self.speed) + " км/год")



class AnimalCar(Animal, Vehicle):
    def __init__(self, name, speed):
        Animal.__init__(self, name)
        Vehicle.__init__(self, speed)

    def info(self):
        print(self.name + " пересувається на швидкості " + str(self.speed) + " км/год")



й = AnimalCar("Автомобіль", 50)

й.eat()
й.move()
й.info()
