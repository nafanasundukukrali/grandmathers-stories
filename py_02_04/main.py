"""
Программа для нахождения треугольнику, в который входит одинаковое
количество точек из первого и второго множества
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import re
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MainWindow(tk.Tk):
    """
    Главное окно с вводом точек
    """

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.set_standard_geometry(600, 500)
        self.title("Нахождение треугольника с равным количеством точек первого и второго множества внутри")

        # Два фрейма с полями для двух множеств
        self.two_array_field = TwoArrayFrame(self)
        self.two_array_field.pack(side=tk.TOP)

        clear_all_button = tk.Button(self, text="Отчистить оба множества", command=self.clear_all)
        clear_all_button.pack(side=tk.BOTTOM, fill=tk.X)

        get_triangle = tk.Button(self, text="Найти искомый треугольник", command=self.find_triangle)
        get_triangle.pack(side=tk.BOTTOM, fill=tk.X)

        self.mainloop()

    def set_standard_geometry(self, w=600, h=400):
        """
        Функция для установки геометрических параметров окна. По умолчанию ширина 600, высота 400. Позиционирование
        по центру.
        """
        self.geometry(f'{w}x{h}+{self.winfo_screenwidth() // 2 - w // 2}'
                      f'+{self.winfo_screenheight() // 2 - h // 2 - 50}')

    def clear_all(self):
        """
        Функция для отчистки всех точек из множеств
        """
        self.two_array_field.second_array.list_box.delete(*self.two_array_field.second_array.list_box.get_children())
        self.two_array_field.first_array.list_box.delete(*self.two_array_field.first_array.list_box.get_children())

    def find_triangle(self):
        """
        Функция для поиска и построения искомого треугольника
        """
        # Проверка, что первое множество не пустое
        if not self.two_array_field.first_array.list_box.get_children():
            messagebox.showerror("Ошибка определения треугольника", "Первое множество пустое")
            return
        # Получение множество точек первого множества
        children_array_1 = self.two_array_field.first_array.list_box.get_children('')
        first = []

        for elem in children_array_1:
            first.append(self.two_array_field.first_array.list_box.item(elem, 'values')[0])

        first_x,  first_y = self.prepare_co_ords(first)

        # Получение множества точек второго множества
        children_array_2 = self.two_array_field.second_array.list_box.get_children('')
        second = []

        for elem in children_array_2:
            second.append(self.two_array_field.second_array.list_box.item(elem, 'values')[0])

        second_x, second_y = self.prepare_co_ords(second)

        # Проверка, что точек в первом множестве больше 3
        if len(first_x) < 3:
            messagebox.showerror('Ошибка определения треугольника', 'Невозможно найти хотя бы один треугольника,'
                                                                    'так как количество вершин меньше 3.')
            return

        # Получение окна с графиком
        ResultWindow(self, first_x, first_y, second_x, second_y)

    def prepare_co_ords(self, list_):
        """
        Функция для подготовки координат к дальнейшей работе
        """
        result_x = []
        result_y = []

        for elem in list_:
            x, y = re.findall(r'[+-]*[0-9]+,*[0-9]*', elem)
            result_x.append(float(x.replace(',', '.')))
            result_y.append(float(y.replace(',', '.')))

        return result_x, result_y


class TwoArrayFrame(tk.Frame):
    """
    Фрейм для работы с двумя фреймами двух множеств
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.second_array = OneArrayInputFrame(self, "Второе множество точек", "red")
        self.first_array = OneArrayInputFrame(self, "Первое множество точек", "pink")


class OneArrayInputFrame(tk.Frame):
    """
    Класс для фрейма каждого из множеств
    """

    def __init__(self, parent, label, color):
        tk.Frame.__init__(self, parent, width=300, height=420, bg=color)
        self.parent = parent

        name_label = tk.Label(self, text=label)
        name_label.pack(side=tk.TOP)

        # Список с координатами точек
        self.list_box = ttk.Treeview(self)
        self.list_box['columns'] = ['0', '1']
        self.list_box.column(f"#0", width=0)
        self.list_box.column(f"#1", width=100)
        scrollbar = tk.Scrollbar(self.list_box, orient=tk.VERTICAL)
        self.list_box.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.list_box.yview)
        self.list_box.pack_propagate(False)
        self.list_box.pack(side=tk.TOP)
        scrollbar.pack(fill=tk.Y, side=tk.RIGHT)

        # Поле для ввода координат
        enter_text = tk.StringVar()
        enter_label = tk.Label(self, text='Введите координаты в формате (1,4;2)')
        enter_label.pack(side=tk.TOP)
        self.enter_entry = tk.Entry(self, textvariable=enter_text)
        self.enter_entry.pack(side=tk.TOP)

        # Кнопка добавить
        add_button = tk.Button(self, text="Добавить точку", command=self.add_co_ords)
        add_button.pack(side=tk.TOP)

        # Кнопка удалить
        delete_button = tk.Button(self, text="Удалить точку", command=self.delete_co_ords)
        delete_button.pack(side=tk.TOP)

        self.pack_propagate(False)
        self.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def delete_co_ords(self):
        """
        Функция для удаления координат точки
        """

        try:
            item = self.list_box.selection()[0]
        except Exception:
            messagebox.showerror("Ошибка удаления координаты", "Вы не выбрали координату, которую хотите удалить."
                                                               " Нажмите левой кнопкой мыши на неё.")
            return

        self.list_box.delete(item)

    def add_co_ords(self):
        """
        Функция для доавбления координат точки
        """

        if not re.findall(r'\([+-]*[0-9]+,*[0-9]*;[+-]*[0-9]+,*[0-9]*\)', self.enter_entry.get()):
            messagebox.showerror("Ошибка ввода координат точки", "Введённые координаты не соответствуют примеру (1,4;2)"
                                                                 ".")
            return

        children = self.list_box.get_children('')

        for child in children:
            if self.list_box.item(child, 'values')[0] == self.enter_entry.get():
                messagebox.showerror('Ошибка ввода координат', 'Элемент присутствует в списке.')
                return

        self.list_box.insert('', 'end', values=[self.enter_entry.get()])


class ResultWindow:
    """
    Окошко с графиком
    """

    def __init__(self, master, first_x, first_y, second_x, second_y):

        self.first_np_x = first_x
        self.first_np_y = first_y
        self.second_np_x = second_x
        self.second_np_y = second_y

        # Функция для поиска координат искомого треугольника
        result_triangle = self.get_triangle_co_ords()
        if not result_triangle:
            messagebox.showerror(title='Ошибка поиска треугольника', message='Треугольник в котором находится '
                                                                             'одинаковое количество точек обоих '
                                                                             'множеств не существует')
            return

        # Инициализация окошка и подготовка входных данных к работе
        self.window = tk.Toplevel(master)
        self.set_standard_geometry(700, 700)
        self.first_np_x = np.array(first_x)
        self.first_np_y = np.array(first_y)
        self.second_np_x = np.array(second_x)
        self.second_np_y = np.array(second_y)

        # Отрисовка всех полученных фигур
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.tick_params(axis='both', which='major', labelsize=6)
        t2 = plt.Polygon(result_triangle, color='g', label="Искомый треугольник")
        plt.gca().add_patch(t2)
        ax.scatter(x=self.first_np_x, y=self.first_np_y, marker='o', c='tab:pink', label='Первое множество')
        ax.scatter(x=self.second_np_x, y=self.second_np_y, marker='o', c='r', label='Второе множество')
        plt.legend()
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

        self.window.mainloop()

    def get_triangle_co_ords(self):
        """
        Функция для поиск координат интересующего треугольника
        """

        result_co_ords = []
        i = 0

        while (not result_co_ords) and i < len(self.first_np_x):
            j = i + 1

            while (not result_co_ords) and j < len(self.first_np_x):
                k = j + 1

                while (not result_co_ords) and k < len(self.first_np_x):
                    # Проверка, что из данных точек собирается треугольник
                    if self.check_if_triangle(self.first_np_x[i], self.first_np_y[i],
                                              self.first_np_x[j], self.first_np_y[j],
                                              self.first_np_x[k], self.first_np_y[k]):
                        dot_counter_first = 0
                        dot_counter_second = 0

                        # Подсчёт количества точек первого множества, которое уходит в треугольник
                        for t in range(len(self.first_np_x)):
                            if self.check_if_in_triangle(self.first_np_x[i], self.first_np_y[i],
                                                         self.first_np_x[j], self.first_np_y[j],
                                                         self.first_np_x[k], self.first_np_y[k],
                                                         self.first_np_x[t], self.first_np_y[t]):
                                dot_counter_first += 1

                        # Подсчёт количества точек второго множества, которое входит в треугольник
                        for t in range(len(self.second_np_x)):
                            if self.check_if_in_triangle(self.first_np_x[i], self.first_np_y[i],
                                                         self.first_np_x[j], self.first_np_y[j],
                                                         self.first_np_x[k], self.first_np_y[k],
                                                         self.second_np_x[t], self.second_np_y[t]):
                                dot_counter_second += 1

                        # Добавление треугольника в список
                        co_ords = self.sort_co_ords([self.first_np_x[i], self.first_np_y[i]],
                                                    [self.first_np_x[j], self.first_np_y[j]],
                                                    [self.first_np_x[k], self.first_np_y[k]])
                        if dot_counter_first and dot_counter_first == dot_counter_second \
                                and co_ords not in result_co_ords:
                            for t in range(3):
                                result_co_ords.append(co_ords[t])

                    k += 1

                j += 1

            i += 1

        return result_co_ords

    @staticmethod
    def sort_co_ords(xy_1, xy_2, xy_3):
        # Функция для сортировки координат треугольника в порядке возрастания
        if xy_1[0] > xy_2[0]:
            buf_x = xy_1[0]
            buf_y = xy_1[1]
            xy_1[0] = xy_2[0]
            xy_1[1] = xy_2[1]
            xy_2[0] = buf_x
            xy_2[1] = buf_y
        if xy_2[0] > xy_3[0]:
            buf_x = xy_2[0]
            buf_y = xy_2[1]
            xy_1[0] = xy_3[0]
            xy_1[1] = xy_3[1]
            xy_3[0] = buf_x
            xy_3[1] = buf_y
        if xy_1[0] > xy_2[0]:
            buf_x = xy_1[0]
            buf_y = xy_1[1]
            xy_1[0] = xy_2[0]
            xy_1[1] = xy_2[1]
            xy_2[0] = buf_x
            xy_2[1] = buf_y

        return [xy_1, xy_2, xy_3]


    @staticmethod
    def check_if_in_triangle(x1, y1, x2, y2, x3, y3, x, y):
        # Функция для проверки, что точка находится внутри треугольника
        a = (x1 - x) * (y2 - y1) - (x2 - x1) * (y1 - y)
        b = (x2 - x) * (y3 - y2) - (x3 - x2) * (y2 - y)
        c = (x3 - x) * (y1 - y3) - (x1 - x3) * (y3 - y)

        return (a > 0 and b > 0 and c > 0) or (a < 0 and b < 0 and c < 0)

    @staticmethod
    def check_if_triangle(x1, y1, x2, y2, x3, y3):
        # Проверка, что три точки образуют треугольник
        return not (((y1-y2)*(x1-x3) - (y1-y3)*(x1-x2)) < 10**(-8))

    def set_standard_geometry(self, w=600, h=400):
        """
        Функция для установки геометрических параметров окна. По умолчанию ширина 600, высота 400. Позиционирование
        по центру.
        """
        self.window.geometry(f'{w}x{h}+{self.window.winfo_screenwidth() // 2 - w // 2}'
                             f'+{self.window.winfo_screenheight() // 2 - h // 2 - 50}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MainWindow()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
