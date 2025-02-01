# #Разработай систему управления учетными записями пользователей для
# небольшой компании. Компания разделяет сотрудников на обычных работников  и
# администраторов. У каждого сотрудника есть уникальный идентификатор (ID),
# имя и уровень доступа. Администраторы, помимо обычных данных пользователей,
# имеют дополнительный уровень доступа и могут добавлять или удалять
# пользователя из системы.
# # Требования:
# # 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
# # 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`.
# Добавь дополнительный атрибут уровня доступа, специфичный для
# администраторов ('admin'). Класс должен также содержать методы `add_user`
# и `remove_user`, которые позволяют добавлять и удалять пользователей из
# списка (представь, что это просто список экземпляров `User`).
# # 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого
# доступа и модификации снаружи. Предоставь доступ к необходимым атрибутам
# через методы (например, get и set методы).

class User():
    user_list = []

    def __init__(self, ID, name):
        self.__ID = ID
        self._name = name
        self.__access_level = "user"

    def get_ID(self):
        return self.__ID

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self._name = name


class Admin(User):

    def __init__(self, ID, name, access_level="admin"):
        super().__init__(ID, name)
        self.__access_level = "admin"


    def add_user(self, user):
        User.user_list.append(user)
        print(f"Добавлен пользователь: {user.get_name}")

    def remove_user(self, user):
        User.user_list.remove(user)
        print(f"Пользователь {user.get_name} удален")


admin = Admin(0, "Denis")
user1 = User (1, "Max")
user2 = User(2, "Alex")
user3 = User(3, "Maria")

print(user1.get_ID())
print(user1.get_name())
print(user1.get_access_level())

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

for user in User.user_list:
    print(f"ID: {user.get_ID()}, name: {user.get_name()}, access: "
          f"{user.get_access_level()}")

admin.remove_user(user2)

for user in User.user_list:
    print(f"ID: {user.get_ID()}, name: {user.get_name()}, access: "
          f"{user.get_access_level()}")