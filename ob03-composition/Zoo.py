import json

# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Звук животного"

    def eat(self):
        return f"{self.name} ест."

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, возраст: {self.age}"


# Подклассы Animal
class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        return "Чик-чирик!"

    def fly(self):
        return f"{self.name} летает с размахом крыльев {self.wingspan} см."


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Ррр!"

    def run(self):
        return f"{self.name} бежит."


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        return "Шшш!"

    def crawl(self):
        return f"{self.name} ползёт."


# Классы для сотрудников
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        return f"{self.name} кормит {animal.name}."

    def __str__(self):
        return f"Смотритель зоопарка: {self.name}"


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        return f"{self.name} лечит {animal.name}."

    def __str__(self):
        return f"Ветеринар: {self.name}"


# Класс Zoo с композицией
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Сотрудник {staff_member.name} добавлен в зоопарк.")

    def show_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(animal)

    def show_staff(self):
        print("Сотрудники зоопарка:")
        for staff_member in self.staff:
            print(staff_member)

    def save_to_file(self, filename):
        data = {
            "name": self.name,
            "animals": [{"type": animal.__class__.__name__, "name": animal.name, "age": animal.age} for animal in self.animals],
            "staff": [{"type": staff.__class__.__name__, "name": staff.name} for staff in self.staff]
        }
        with open(filename, "w") as file:
            json.dump(data, file)
        print(f"Информация о зоопарке сохранена в файл {filename}.")

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
        self.name = data["name"]
        self.animals = []
        self.staff = []

        for animal_data in data["animals"]:
            if animal_data["type"] == "Bird":
                animal = Bird(animal_data["name"], animal_data["age"], wingspan=30)
            elif animal_data["type"] == "Mammal":
                animal = Mammal(animal_data["name"], animal_data["age"], fur_color="коричневый")
            elif animal_data["type"] == "Reptile":
                animal = Reptile(animal_data["name"], animal_data["age"], scale_type="крупные")
            else:
                animal = Animal(animal_data["name"], animal_data["age"])
            self.animals.append(animal)

        for staff_data in data["staff"]:
            if staff_data["type"] == "ZooKeeper":
                staff = ZooKeeper(staff_data["name"])
            elif staff_data["type"] == "Veterinarian":
                staff = Veterinarian(staff_data["name"])
            else:
                staff = None
            if staff:
                self.staff.append(staff)

        print(f"Информация о зоопарке загружена из файла {filename}.")


# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} говорит: {animal.make_sound()}")


# Пример использования
zoo = Zoo("Мой зоопарк")

# Добавляем животных
bird = Bird("Кеша", 2, 30)
mammal = Mammal("Барсик", 5, "серый")
reptile = Reptile("Гоша", 3, "мелкие")

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

# Добавляем сотрудников
keeper = ZooKeeper("Иван")
vet = Veterinarian("Мария")

zoo.add_staff(keeper)
zoo.add_staff(vet)

# Демонстрация полиморфизма
animal_sound(zoo.animals)

# Сохраняем информацию о зоопарке в файл
zoo.save_to_file("zoo_data.json")

# Загружаем информацию о зоопарке из файла
new_zoo = Zoo("Новый зоопарк")
new_zoo.load_from_file("zoo_data.json")

# Показываем загруженные данные
new_zoo.show_animals()
new_zoo.show_staff()