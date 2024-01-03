import json
from datetime import datetime
import shelve


# Загрузка данных из файла
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks


# Сохранение данных в файл
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)


# Добавление задачи
def add_task(title, description, deadline, priority):
    tasks = load_tasks()
    task = {
        "заголовок": title,
        "описание": description,
        "срок_выполнения": deadline,
        "приоритет": priority
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Новая задача добавлена!")


# Отображение списка задач
# def show_tasks():
#     tasks = load_tasks()
#     for index, task in enumerate(tasks, 1):
#         print(f"{index}. {task['заголовок']} - {task['описание']} - {task['срок_выполнения']} - {task['приоритет']}")


# Обновление задачи
def update_task(index, title, description, deadline, priority): # переписать
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        tasks[index - 1] = {
            "заголовок": title,
            "описание": description,
            "срок_выполнения": deadline,
            "приоритет": priority
        }
        save_tasks(tasks)
        print("Задача обновлена!")
    else:
        print("Ошибка: Неверный номер задачи")
    # pass


# Удаление задачи
def delete_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        save_tasks(tasks)
        print("Задача удалена!")
    else:
        print("Ошибка: Неверный номер задачи")


# Добавим задачу в указанную категорию
# def add_task_to_category(category, task_index):
#     categories = load_categories()
#     if category in categories:
#         categories[category].append(task_index)
#     else:
#         categories[category] = [task_index]
#     save_categories(categories)


# Загрузка категорий из файла
# def load_categories():
#     try:
#         with open('categories.json', 'r') as file:
#             categories = json.load(file)
#     except FileNotFoundError:
#         categories = {}
#     return categories


# Сортировка задач по приоритету
def sort_tasks_by_priority(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x['приоритет'], reverse=True)
    # for task in sorted_tasks:
    #     print(f"{task['заголовок']} - {task['приоритет']}")
    return sorted_tasks


# Сохранение категорий в файл
def save_categories(categories):
    with open('categories.json', 'w') as file:
        json.dump(categories, file, indent=4)


# Экспорт данных
def export_tasks(filename):
    tasks = load_tasks()
    with shelve.open(filename) as shelf:
        shelf['tasks'] = tasks


# Импорт и экспорт данных
def export_to_txt():
    tasks = load_tasks()
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task['заголовок']} - {task['описание']} - {task['срок_выполнения']} - {task['приоритет']}\n")
    print('done')


def import_from_txt():
    with open('tasks.txt', 'r') as file:
        tasks = []
        for line in file:
            task_data = line.split(' - ')
            task = {
                "заголовок": task_data[0],
                "описание": task_data[1],
                "срок_выполнения": task_data[2],
                "приоритет": task_data[3].strip()
            }
            tasks.append(task)
        save_tasks(tasks)



# Примеры использования функций
# add_task("Сходить в спортзал", "Посетить тренировку по бегу", "2023-12-30", "средний")
# add_task_to_category("здоровье", len(load_tasks()))
# show_tasks()
# update_task(2, "Закончить финансовый отчет", "Завершить финансовый отчет по проекту X вовремя", "2023-12-31", "высокий")
# delete_task(1)
# show_tasks()
