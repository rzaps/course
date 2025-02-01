class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} сел есть")
        self.power += 1

    def hit(self):
        print(f"{self.name} бьет")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} гуляет")
        self.endurance -= 6

    def info(self):
        print(f"Имя воина {self.name}")
        print(f"Цвет волос воина {self.hair_color}")
        print(f"Сила воина {self.power}")
        print(f"Выносливость воина {self.endurance}")

warrior1 = Warrior("Петр", 76, 54, "русый")
warrior2 = Warrior("Алексей", 58, 73, "блонд")
print(warrior1.name)
print(warrior1.power)
print(warrior1.endurance)
print(warrior1.hair_color)

warrior1.sleep()
warrior1.eat()
warrior1.hit()
warrior1.walk()
warrior1.info()