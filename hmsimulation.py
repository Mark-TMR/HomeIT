import random

class House:
    def __init__(self, food=30, mess=10):
        self.food = food
        self.mess = mess


class Auto:
    def __init__(self, fuel=50, strength=100):
        self.fuel = fuel
        self.strength = strength

    def drive(self):
        if self.fuel > 10 and self.strength > 0:
            self.fuel -= 10
            self.strength -= 5
            print("Машина їде 🚗")
            return True
        else:
            print("Машина не може їхати ❌")
            return False


class Job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Human:
    def __init__(self, name="Human", home=None, job=None, car=None, money=100, satiety=50, gladness=50):
        self.name = name
        self.home = home
        self.job = job
        self.car = car
        self.money = money
        self.satiety = satiety
        self.gladness = gladness

    def eat(self):
        if self.home.food > 0:
            self.satiety += 20
            self.home.food -= 10
            print(self.name, "поїв 🍞")
        else:
            print("Немає їжі, треба купити 🛒")
            self.shopping("food")

    def work(self):
        if self.car.drive():
            self.money += self.job.salary
            self.satiety -= 10
            self.gladness -= 5
            print(self.name, "попрацював як", self.job.name, "💼")
        else:
            print("Не зміг поїхати на роботу 😢")

    def chill(self):
        self.gladness += 15
        self.satiety -= 5
        print(self.name, "відпочиває 😎")

    def clean_home(self):
        self.home.mess -= 10
        self.gladness -= 3
        print(self.name, "прибрав вдома 🧹")

    def shopping(self, item):
        if item == "food":
            self.home.food += 20
            self.money -= 20
            print(self.name, "купив їжу 🥖")
        elif item == "fuel":
            self.car.fuel += 30
            self.money -= 25
            print(self.name, "заправив машину ⛽")

    def live_a_day(self, day):
        print("\nДень", day, "життя", self.name)
        print("💰:", self.money, "🍗:", self.satiety, "😊:", self.gladness)

        if self.satiety < 20:
            self.eat()
        elif self.money < 30:
            self.work()
        elif self.gladness < 30:
            self.chill()
        elif self.home.mess > 40:
            self.clean_home()
        else:
            random.choice([self.eat, self.work, self.chill])()



alex = Human(
    name="Alex",
    home=House(),
    job=Job("Програміст", 100),
    car=Auto()
)


for day in range(1, 11):
    alex.live_a_day(day)

