
class Hero():
    def __init__(self, name, health = 100, attack_power = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит "
              f"{self.attack_power} ущерба --- У {other.name} осталось "
              f"{other.health} здоровья")

    def is_alive(self):
        return self.health > 0

class Game():
    def __init__(self):
        self.player = Hero("Игрок")
        self.computer = Hero("Компьютер")

    def start(self):
        print("MORTAL KOMBAT BEGIN")
        while self.player.is_alive() and self.computer.is_alive():
            if self.player.is_alive():
                self.player.attack (self.computer)

            if self.computer.is_alive():
                self.computer.attack(self.player)

        if self.player.is_alive():
            print(f"Победил {self.player.name}")
        else:
            print(f"Победил {self.computer.name}")

game = Game()
game.start()

