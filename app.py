from tkinter import Label, Button, Entry, Scrollbar, Listbox, END, ttk, StringVar, OptionMenu
from tkinter import messagebox
from task import *


class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        self.tasks = load_tasks()
        # self.labels = load_labels()
        master.title("Task Manager")

        # self.load_labels()
        # self.load_tasks()

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

        # self.label_project = ttk.Label(master, text="Project:", style='TLabel')
        # self.label_project.grid(row=5, column=0)

        # self.project_var = StringVar(master)
        # self.project_var.set("")
        # self.project_menu = OptionMenu(master, self.project_var, "Project1", "Project2",
        #                                "Project3")  # Здесь нужно использовать динамические данные
        # self.project_menu.grid(row=5, column=1)

        self.btn_add_task = ttk.Button(master, text="Добавить задачу", style='TButton', command=self.add_task)
        self.btn_add_task.grid(row=5, columnspan=4, pady=10)

        self.label_label = ttk.Label(master, text="Label:", style='TLabel')
        self.label_label.grid(row=6, column=0, pady=(10, 0))

        self.entry_label = ttk.Entry(master)
        self.entry_label.grid(row=6, column=1, pady=(10, 0))

        self.btn_add_label = ttk.Button(master, text="Добавить метку", style='TButton', command=self.add_label)
        self.btn_add_label.grid(row=6, column=2, pady=(10, 0))

        self.btn_show_tasks = ttk.Button(master, text="Отобразить по метке", style='TButton',
                                         command=self.show_category_tasks)
        self.btn_show_tasks.grid(row=7, column=2, pady=10)

        self.btn_show_tasks = ttk.Button(master, text="Отобразить все задачи", style='TButton',
                                         command=self.show_tasks)
        self.btn_show_tasks.grid(row=8, column=2, pady=(10, 0))



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
        self.task_list.grid(row=9, columnspan=4)

        self.scrollbar = Scrollbar(master)
        self.scrollbar.grid(row=9, column=4, sticky="ns")

        self.task_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_list.yview)

        self.btn_update_task = Button(master, text="Обновить выбранную задачу", command=self.update_selected_task)
        self.btn_update_task.grid(row=10, columnspan=2)

        self.btn_delete_task = Button(master, text="Удалить выбранную задачу", command=self.delete_selected_task)
        self.btn_delete_task.grid(row=11, columnspan=2)

        self.btn_export = Button(master, text="Экспортировать задачи", command=self.export_data)
        self.btn_export.grid(row=12, columnspan=2)

        self.btn_export = Button(master, text="Импортировать задачи", command=self.import_data)
        self.btn_export.grid(row=13, columnspan=2)

        # self.listbox_label = Listbox(master, selectmode='SINGLE')
        # self.listbox_label.grid(row=13, column=0, columnspan=4, pady=(10, 0))
        # for label in self.labels:
        #     self.listbox_label.insert(END, f"{label}")
        # self.listbox_label.bind("<<ListboxSelect>>", self.on_select_label)

        # Загрузка задач и отображение в списке
        tasks_load = load_tasks()
        tasks_1 = sort_tasks_by_priority(tasks_load)
        # tasks = categorize_tasks_by_project(tasks_1)
        special_tag = 'Метки:'
        for task in tasks_1:
            if special_tag in list(task.keys()):
                print('видит')
                self.task_list.insert(END,
                                     f"{task['заголовок']} - {task['описание']} - {task['срок_выполнения']} "
                                     f"- {task['приоритет']} - Метки:{task['Метки:']}")
            else:
                self.task_list.insert(END,
                                      f"{task['заголовок']} - {task['описание']} - {task['срок_выполнения']} "
                                      f"- {task['приоритет']}")

    def save_labels(self, label, index):
        print('индекс: ', index)
        if index:
            save_label(index[0], label)
            # self.task_list.delete(selected_index[0])

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
        add_task(title, description, deadline, priority.lower())
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

    def import_data(self):
        import_from_txt()


    # def add_label(self):
    #     # Функция добавления метки к задаче
    #     selected_task_index = self.task_list.curselection()
    #     if selected_task_index:
    #         label = self.entry_label.get()
    #         if label:
    #             task = self.tasks[selected_task_index[0]]
    #             if 'метки' in task:
    #                 task['метки'].append(label)
    #             else:
    #                 task['метки'] = [label]
    #             self.task_list.delete(selected_task_index[0])
    #             self.task_list.insert(selected_task_index[0], f"{task['заголовок']} - "
    #                                                           f"{task['описание']} - {task['срок_выполнения']} "
    #                                                           f"- {task['приоритет']}"
    #                                                           f" - Метки: {', '.join(task['метки'])}")
    #             self.entry_label.delete(0, 'end')
    #         else:
    #             messagebox.showwarning("Warning", "Введите метку!")
    #     else:
    #         messagebox.showwarning("Warning", "Выберите задачу для добавления метки!")

    # def load_tasks(self):
    #     try:
    #         with open('tasks.json', 'r') as file:
    #             self.tasks = json.load(file)
    #     except FileNotFoundError:
    #         self.tasks = []
    #
    # def save_tasks(self):
    #     with open('tasks.json', 'w') as file:
    #         json.dump(self.tasks, file)

    # def load_labels(self):
    #     try:
    #         with open('labels.json', 'r') as file:
    #             self.labels = json.load(file)
    #     except FileNotFoundError:
    #         self.labels = []

    def add_label(self):
        # Функция добавления метки к задаче
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            label = self.entry_label.get()
            # print(selected_task_index[0])
            # print(label)
            self.save_labels(label, selected_task_index)
            if label:
                task = self.tasks[selected_task_index[0]]
                if 'метки' in task:
                    task['метки'].append(label)
                else:
                    task['метки'] = [label]
                self.task_list.delete(selected_task_index[0])
                self.task_list.insert(selected_task_index[0],
                                      f"{task['заголовок']} - {task['описание']} - {task['срок_выполнения']}"
                                      f" - {task['приоритет']} - Метки: {', '.join(task['метки'])}")

                self.entry_label.delete(0, 'end')

            else:
                messagebox.showwarning("Warning", "Введите метку!")
        else:
            messagebox.showwarning("Warning", "Выберите задачу для добавления метки!")

    # def save_labels(self):
    #     with open('labels.json', 'w') as file:
    #         json.dump(self.labels, file)

    # def add_label(self):
    #     selected_task_index = self.task_list.curselection()
    #     if selected_task_index:
    #         label = self.entry_label.get()
    #         if label:
    #             task = self.tasks[selected_task_index[0]]
    #             if 'метки' in task:
    #                 task['метки'].append(label)
    #             else:
    #                 task['метки'] = [label]
    #             self.task_list.delete(selected_task_index[0])
    #             self.task_list.insert(selected_task_index[0],
    #                                   f"{task['заголовок']} - {task['описание']} - {task['срок_выполнения']} "
    #                                   f"- {task['приоритет']} - Метки: {', '.join(task['метки'])}")
    #             self.entry_label.delete(0, 'end')
    #
    #             if label not in self.labels:
    #                 self.labels.append(label)  # Добавление новой метки в список меток
    #                 self.save_labels()  # Сохранение меток
    #             self.save_tasks()  # Сохранение меток в информации о задачах
    #         else:
    #             messagebox.showwarning("Warning", "Enter a label!")
    #     else:
    #         messagebox.showwarning("Warning", "Select a task to add a label!")

    def show_category_tasks(self):
        label = self.entry_label.get()
        if label:
            labeled_tasks = [task for task in self.tasks if task.get('Метки:') and label in task['Метки:']]
            self.task_list.delete(0, END)
            for task in labeled_tasks:
                self.task_list.insert(END,
                                      f"{task['заголовок']} - {task['описание']} - "
                                      f"{task['срок_выполнения']} - {task['приоритет']} "
                                      f"- Метки: {''.join(task['Метки:'])}")
        else:
            messagebox.showwarning("Warning", "Введите метку для отображения задач!")

    def show_tasks(self):
        tasks_load = load_tasks()
        tasks_1 = sort_tasks_by_priority(tasks_load)
        # print(self.task_list)
        # for extra_task in tasks_1:
        #     print('extra tSK ',extra_task)
        #     print(extra_task.index())
        #     self.task_list.delete(extra_task.index(), END)
        # # tasks = categorize_tasks_by_project(tasks_1)
        self.task_list.delete(0, END)
        special_tag = 'Метки:'
        for task in tasks_1:
            if special_tag in list(task.keys()):
                print('видит')
                self.task_list.insert(END,
                                      f"{task['заголовок']} - {task['описание']} - {task['срок_выполнения']} "
                                      f"- {task['приоритет']} - Метки:{task['Метки:']}")
            else:
                self.task_list.insert(END,
                                      f"{task['заголовок']} - {task['описание']} - {task['срок_выполнения']} "
                                      f"- {task['приоритет']}")

    # def load_labels(self):
    #     try:
    #         with open('labels.json', 'r') as file:
    #             self.labels = json.load(file)
    #     except FileNotFoundError:
    #         self.labels = []

    # def save_labels(self):
    #     with open('labels.json', 'w') as file:
    #         json.dump(self.labels, file)

    # def show_category_tasks(self):
        # project = self.project_var.get()
        # if project == "Select Project":
        #     messagebox.showwarning("Warning", "")
        #     return

    # def on_select_label(self, event):
    #     # Функция вызывается при выборе метки из списка
    #     index = self.listbox_label.curselection()
    #     if index:
    #         label = self.labels[index[0]]
    #         labeled_tasks = [task for task in self.tasks if task.get('метки') and label in task['метки']]
    #         self.task_list.delete(0, END)
    #         for task in labeled_tasks:
    #             self.task_list.insert(END,
    #                                   f"{task['заголовок']} - {task['описание']} - {task['срок_выполнения']} "
    #                                   f"- {task['приоритет']} - Метки: {', '.join(task['метки'])}")
