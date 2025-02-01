from pyvis.network import Network

# Создаем интерактивный граф
net = Network(notebook=True, height="600px", width="100%", bgcolor="#ffffff", font_color="black")

# Определяем таблицы базы данных
tables = {
    "Rooms": ["id", "home_type", "address", "has_tv", "has_internet", "price"],
    "Users": ["id", "name", "email", "password", "phone_number"],
    "Reservations": ["id", "user_id", "room_id", "start_date", "end_date", "price"],
    "Reviews": ["id", "reservation_id", "rating"]
}

# Определяем связи между таблицами (foreign keys)
relations = [
    ("Reservations", "Rooms"),  # Reservations.room_id -> Rooms.id
    ("Reservations", "Users"),  # Reservations.user_id -> Users.id
    ("Reviews", "Reservations") # Reviews.reservation_id -> Reservations.id
]

# Добавляем таблицы как узлы графа
for table in tables.keys():
    net.add_node(table, label=table, shape="box", color="#A9CCE3", font={'size': 20})

# Добавляем связи между таблицами как рёбра
for relation in relations:
    net.add_edge(relation[0], relation[1], color="#2E86C1")

# Сохраняем и открываем интерактивный HTML-файл
net.show("database_schema.html")

print("Готово! Откройте файл 'database_schema.html' в браузере.")
