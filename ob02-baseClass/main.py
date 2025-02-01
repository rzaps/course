class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f"{self.name} летит")

    def eat(self):
        print(f"{self.name} ест")

    def sing(self):
        print(f"{self.name} поет чирик: {self.voice}")

    def info(self):
        print(f"Имя птицы: {self.name}")
        print(f"Цвет птицы: {self.color}")
        print(f"Голос птицы: {self.voice}")


class Pigeon(Bird):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def sing(self):
        print(f"{self.name} поет: {self.voice}")


    def walk(self):
        print(f"{self.name} гуляет")


bird1 = Pigeon("Гоша", "курлык", "серый", "крошки")
bird2 = Bird("Маша", "чирик", "коричневый")


bird1.sing()
bird1.info()
bird1.walk()


