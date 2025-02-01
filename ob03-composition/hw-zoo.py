# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2.Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и
# переопределите методы, если требуется (например, различный звук для
# `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для
# каждого  животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет
# содержать  информацию о животных и сотрудниках. Должны быть методы для
# добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()`  для
# `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу,  такие как
# сохранение информации о зоопарке в файл и возможность её загрузки,  чтобы у
# вашего зоопарка было "постоянное состояние" между запусками программы.

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("чик-чирик")

class Mammal(Animal):
    def make_sound(self):
        print("му")

class Reptile(Animal):
    def make_sound(self):
        print("шшш")


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f"кормит {animal.name}")

class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f"лечит {animal.name}")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


zoo1 = Zoo()
bird1 = Bird("Воробей", 3)
mammal1 = Mammal("Корова", 5)
reptile1 = Reptile("Удав", 2)

zookeeper = ZooKeeper("Вася", "Зоолог")
veterinarian = Veterinarian("Ваня", "Ветеринар")


zoo1.add_animal(mammal1)
zoo1.add_animal(reptile1)
zoo1.add_animal(bird1)

zoo1.add_employee(zookeeper)
zoo1.add_employee(veterinarian)

for animal in zoo1.animals:
    print(f"{animal.name} - {animal.age} лет")
    animal_sound([animal])

for employee in zoo1.employees:
    print(f"{employee.name} - {employee.position}")


with open("zoo.txt", "w", encoding="utf-8") as file:
    file.write("Животные:\n")
    for animal in zoo1.animals:
        file.write(f"{animal.name} - {animal.age} лет\n")

    file.write("\nСотрудники:\n")
    for employee in zoo1.employees:
        file.write(f"{employee.name} - {employee.position}\n")

