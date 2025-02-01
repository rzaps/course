#Менеджер задач
#Задача: Создай класс Task, который позволяет управлять задачами (делами). У
# задачи должны быть атрибуты: описание задачи, срок выполнения и статус  (
# выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
# выполненных задач и вывода списка текущих (не выполненных) задач.


class Task():

    def __init__(self):
        self.all_tasks = []

    #добавление задачи
    def add_task(self, description, deadline, status="не выполнена"):
        self.all_tasks.append({"description": description, "deadline":
            deadline, "status": status})
        print(f"Добавлена задача: {description}")

    #вывод списка
    def list(self):
        print("Текущие задачи")
        for task in self.all_tasks:
            if task["status"] == "не выполнена":
                print(f"Задача: {task["description"]} - Срок:{task["deadline"]}")


    #изменение статуса задачи
    def complete_tasks(self, description):
        for task in self.all_tasks:
            if task["description"] == description:
                task["status"] = "выполнена"
                print(f"Задача {description} выполнена")
            else:
                print(f"Задача {description} не найдена")


task = Task()

task.add_task("Помыть посуду", "12.01.24")
task.add_task("Сходить в магазин", "13.01.25")
task.add_task("Сходить в кино", "14.01.25")

print("-----")

task.list()

print("-----")

task.complete_tasks("Помыть посуду")

