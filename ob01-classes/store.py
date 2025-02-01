# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать класс `Store`, который можно будет использовать для создания различных магазинов.
# # Шаги:
# # 1. Создай класс `Store`:
# # -Атрибуты класса:
# # - `name`: название магазина.
# # - `address`: адрес магазина.
# # - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
# # - Методы класса:
# # - `__init__ - конструктор, который инициализирует название и адрес,
# а также пустой словарь  для `items`.
# # -  метод для добавления товара в ассортимент.
# # - метод для удаления товара из ассортимента.
# # - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# # - метод для обновления цены товара.

# # 2. Создай несколько объектов класса `Store`:
# # Создай не менее трех различных магазинов с разными названиями, адресами и
# добавь в каждый из  них несколько товаров.

# # 3. Протестировать методы:
# # Выбери один из созданных магазинов и протестируй все его методы: добавь
# товар, обнови цену,  убери товар и запрашивай цену.

class Store():

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items [item_name] = price
        print(f"Товар {item_name} добавлен в {self.name}")  #les

    def delete_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} удален из {self.name}")  # les

    def price(self, item_name):
        price = self.items.get(item_name)
        print(f"Цена товара {item_name}: {price}")

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара {item_name} изменена в {self.name}")
        else:
            print(f"Товар {item_name} не найден в {self.name}")


store1 = Store("Морской", "ул. Морская, 9")
store2 = Store("Зеленый", "ул. Зеленая, 28")
store3 = Store("Юг", "ул. Южная, 17")

store1.add_item("apples", 0.7)
store1.add_item("orange", 1.2)
store1.add_item("banana", 2.8)
store1.add_item("egg", 3.2)
store1.add_item("water", 0.8)

print(store1.items)

store1.delete_item("egg")

print(store1.items)

store1.price("banana")

store1.update_price("water", "90")

store1.price("water")




# store2.add_item("apples", 0.7)
# store2.add_item("orange", 1.2)
# store2.add_item("banana", 2.8)
# store2.add_item("egg", 3.2)
# store2.add_item("water", 0.8)
#
# store3.add_item("apples", 0.7)
# store3.add_item("orange", 1.2)
# store3.add_item("banana", 2.8)
# store3.add_item("egg", 3.2)
# store3.add_item("water", 0.8)
