class Test():
    def __init__(self):
        self.public = "публичный атрибут"
        self._protected = "защищенный атрибут"
        self.__private = "приватный атрибут"

    def get_private(self):
        return self.__private

    def set_private(self, value):
        self.__private = value





test = Test()
print(test.public)
print(test._protected)
print(test.get_private())

test.set_private("значение приватного атрибута")
print(test.get_private())



class Test2():
    def public_func(self):
        print("Публичный метод")

    def _protected_func(self):
        print("Защищённый метод")

    def __private_func(self):
        print("Приватный метод")

    def test_private(self):
        self.__private_func()

test = Test2()
test.public_func()
test._protected_func()
test.test_private()