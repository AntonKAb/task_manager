from tkinter import Tk
from app import TaskManagerApp


def start_prog():
    root = Tk()
    ap = TaskManagerApp(root)
    root.mainloop()


if __name__ == '__main__':
    print('hellow')
    # Запуск графического интерфейса
    start_prog()

