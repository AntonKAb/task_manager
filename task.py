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


# Обновление задачи
def update_task(index, title, description, deadline, priority):
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


# Удаление задачи
def delete_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        save_tasks(tasks)
        print("Задача удалена!")
    else:
        print("Ошибка: Неверный номер задачи")


# Сортировка задач по приоритету
def sort_tasks_by_priority(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x['приоритет'], reverse=True)
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
    label = 'Метки:'
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            # print(task)
            if label in list(task.keys()):
                file.write(f"{task['заголовок']} - {task['описание']} - "
                           f"{task['срок_выполнения']} - {task['приоритет']} - Метки: {task['Метки:']}\n")
            else:
                file.write(f"{task['заголовок']} - {task['описание']} - "
                           f"{task['срок_выполнения']} - {task['приоритет']}\n")
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


def save_label(index, point):
    tasks = load_tasks()
    if 0 <= index <= len(tasks):
        tasks[index]['Метки:'] = point
        save_tasks(tasks)
        print("Метка добавлена!")
    else:
        print("Ошибка: Метка не сохранена")
