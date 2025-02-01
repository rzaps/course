#Менеджер задач
#Задача: Создай класс Task, который позволяет управлять задачами (делами). У
# задачи должны быть атрибуты: описание задачи, срок выполнения и статус  (
# выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
# выполненных задач и вывода списка текущих (не выполненных) задач.


class Task():
    all_tasks = []  # Общий список для хранения всех объектов класса (GPT)

    def __init__(self, description, deadline, status="не выполнена"):
        self.description = description
        self.deadline = deadline
        self.status = status

    #добавление задачи
    def add_task(self):
        Task.all_tasks.append(self)
        print(f"Добавлена задача: {self.description}")

    #вывод задачи в списке
    def list(self):
        print(f"Задача: {self.description} --- Срок: {self.deadline}")


    #изменение статуса задачи
    def ready(self):
        self.status = "выполнена"
        print(f"Задача {self.description} выполнена")



task1 = Task("Помыть посуду", "12.01.24")
task2 = Task("Сходить в магазин", "13.01.25")
task3 = Task("Сходить в кино", "14.01.25")

print("------")

task1.add_task()
task2.add_task()
task3.add_task()

print("-----")

for task in Task.all_tasks:
    if task.status == "не выполнена":
       task.list()

print("-----")

task2.ready()

for task in Task.all_tasks:
    if task.status == "не выполнена":
       task.list()

