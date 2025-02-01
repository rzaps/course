# class Bird():
#     def __init__(self, name):
#         self.name = name
#
#     def fly(self):
#         print(f"Птица {self.name} летает")
#
# class Pinguin(Bird):
#     pass
#
#
#
# p = Pinguin("Пингвин")
#
# p.fly()


class Bird():

    def fly(self):
        print(f"Птица летает")


class Duck(Bird):

    def fly(self):
        print(f"Утка летает")

def fly_in_the_sky(animal):
    animal.fly()

b = Bird()
d = Duck()

fly_in_the_sky(b)
fly_in_the_sky(d)