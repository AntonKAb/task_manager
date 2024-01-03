from tkinter import Label, Button, Entry, Scrollbar, Listbox, END, ttk, StringVar, OptionMenu
from tkinter import messagebox
from task import *


class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        master.title("Task Manager")

        self.label = ttk.Label(master, text="Task Manager", style='TLabel')
        self.label.grid(row=0, columnspan=4, pady=(10, 100))

        self.label_title = ttk.Label(master, text="Заголовок:", style='TLabel')
        self.label_title.grid(row=1, column=0, padx=10)
        self.entry_title = ttk.Entry(master)
        self.entry_title.grid(row=1, column=1, columnspan=3)

        self.label_description = ttk.Label(master, text="Описание:", style='TLabel')
        self.label_description.grid(row=2, column=0, padx=10)
        self.entry_description = ttk.Entry(master)
        self.entry_description.grid(row=2, column=1, columnspan=3)

        self.label_deadline = ttk.Label(master, text="Срок выполнения (YYYY-MM-DD):", style='TLabel')
        self.label_deadline.grid(row=3, column=0, padx=10)
        self.entry_deadline = ttk.Entry(master)
        self.entry_deadline.grid(row=3, column=1, columnspan=3)

        self.label_priority = ttk.Label(master, text="Приоритет:", style='TLabel')
        self.label_priority.grid(row=4, column=0, padx=10)
        self.priority_var = StringVar(master)
        self.priority_var.set("Приоритет:")
        self.priority_menu = OptionMenu(master, self.priority_var, "Низкий", "Средний", "Высокий")
        self.priority_menu.grid(row=4, column=1, columnspan=3)

        self.btn_add_task = ttk.Button(master, text="Добавить задачу", style='TButton', command=self.add_task)
        self.btn_add_task.grid(row=5, columnspan=4, pady=10)

        # self.label_title = Label(master, text="Заголовок:")
        # self.label_title.grid(row=1, column=0)
        # self.entry_title = Entry(master)
        # self.entry_title.grid(row=1, column=1)
        #
        # self.label_description = Label(master, text="Описание:")
        # self.label_description.grid(row=2, column=0)
        # self.entry_description = Entry(master)
        # self.entry_description.grid(row=2, column=1)
        #
        # self.label_deadline = Label(master, text="Срок выполнения:")
        # self.label_deadline.grid(row=3, column=0)
        # self.entry_deadline = Entry(master)
        # self.entry_deadline.grid(row=3, column=1)
        #
        # self.label_priority = Label(master, text="Приоритет:")
        # self.label_priority.grid(row=4, column=0)
        # self.entry_priority = Entry(master)
        # self.entry_priority.grid(row=4, column=1)
        #
        # self.btn_add_task = Button(master, text="Добавить задачу", command=self.add_task)
        # self.btn_add_task.grid(row=5, columnspan=2)

        self.task_list = Listbox(master, width=70, height=10)
        self.task_list.grid(row=6, columnspan=4)

        self.scrollbar = Scrollbar(master)
        self.scrollbar.grid(row=6, column=4, sticky="ns")

        self.task_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_list.yview)

        self.btn_update_task = Button(master, text="Обновить выбранную задачу", command=self.update_selected_task)
        self.btn_update_task.grid(row=7, columnspan=2)

        self.btn_delete_task = Button(master, text="Удалить выбранную задачу", command=self.delete_selected_task)
        self.btn_delete_task.grid(row=8, columnspan=2)

        self.btn_export = Button(master, text="Экспортировать задачи", command=self.export_data)
        self.btn_export.grid(row=9, columnspan=2)

        # Загрузка задач и отображение в списке
        tasks = load_tasks()
        for task in tasks:
            self.task_list.insert(END,
                                  f"{task['заголовок']} - {task['описание']} - {task['срок_выполнения']} "
                                  f"- {task['приоритет']}")

    def add_task(self):
        title = self.entry_title.get()
        description = self.entry_description.get()
        deadline = self.entry_deadline.get()
        priority = self.priority_var.get()
        if not (title and deadline and priority != "Выбрать"):
            messagebox.showwarning("Warning", "Заполните все поля и выберите приоритет!")
            return
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Warning", "Неправильный формат даты! Пожалуйста используйте YYYY-MM-DD формат.")
            return
        add_task(title, description, deadline, priority.lower())  # Convert priority to lowercase
        self.entry_title.delete(0, 'end')
        self.entry_description.delete(0, 'end')
        self.entry_deadline.delete(0, 'end')
        self.priority_var.set("Выберите приоритет")

        self.task_list.insert(END, f"{title} - {description} - {deadline} - {priority}")

    def update_selected_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            title = self.entry_title.get()
            description = self.entry_description.get()
            deadline = self.entry_deadline.get()
            priority = self.priority_var.get()
            update_task(selected_index[0] + 1, title, description, deadline, priority)
            self.task_list.delete(selected_index[0])
            self.task_list.insert(selected_index[0], f"{title} - {description} - {deadline} - {priority}")

    def delete_selected_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            delete_task(selected_index[0] + 1)
            self.task_list.delete(selected_index[0])

    def export_data(self):
        export_to_txt()






