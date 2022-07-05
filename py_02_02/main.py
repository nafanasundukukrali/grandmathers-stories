
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as message
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from math import *


def set_standard_geometry(self, w=600, h=400):
    """
    Функция для установки геометрических параметров окна. По умолчанию ширина 600, высота 400. Позиционирование
    по центру.
    """
    self.window.geometry(f'{w}x{h}+{self.window.winfo_screenwidth() // 2 - w // 2}'
                         f'+{self.window.winfo_screenheight() // 2 - h // 2 - 50}')


class ResultWindow:
    def __init__(self, master, function, a, b, h, roots_values, table_data):
        self.window = tk.Toplevel(master)
        self.function = function
        self.a = a
        self.b = b
        self.h = h
        self.roots = roots_values
        self.data_table = table_data
        self.displayed_table = None
        self.table_frame = tk.Frame(self.window, width=900, height=300)
        self.window_preparation()

        self.table_frame.pack(padx=5)

    def start_window(self):
        self.window.grab_set()
        self.window.focus_set()
        self.window.wait_window()

    def prepare_table_data(self):
        columns = ("#1", "#2", "#3", "#4", "#5", "#6")
        self.displayed_table = ttk.Treeview(self.table_frame)

        sb = Scrollbar(
            self.table_frame,
            orient=VERTICAL
        )
        sb.pack(fill=Y, side=RIGHT)

        self.displayed_table.configure(yscrollcommand=sb.set)
        sb.config(command=self.displayed_table.yview)

        self.displayed_table.pack()
        self.displayed_table['columns'] = columns
        self.displayed_table.column("#0", width=0)
        for i in range(1, 7):
            self.displayed_table.column(f"#{i}", width=120)

        self.displayed_table.heading("#1", text="№ корня")
        self.displayed_table.heading("#2", text="[xi;xi+1]")
        self.displayed_table.heading("#3", text="x'")
        self.displayed_table.heading("#4", text="f'")
        self.displayed_table.heading("#5", text="Количество итераций")
        self.displayed_table.heading("#6", text="Код ошибки")
        for i in range(len(self.data_table)):
            self.displayed_table.insert(parent='', index='end', iid=i, text='',
                                        values=[self.data_table[i][0], self.data_table[i][1], self.data_table[i][2],
                                                '{:.3E}'.format(self.data_table[i][3]), self.data_table[i][4],
                                                 self.data_table[i][5]])

    def prepare_picture(self):
        x_values = np.array([self.a + self.h * i for i in range(int(abs(self.b - self.a) / self.h) + 1)])
        y_values = np.array([eval(str(self.function)) for x in x_values])
        roots = []
        y_roots = []
        for x in self.data_table:
            if type(x[2]) == float:
                roots.append(x[2])
                y_roots.append(x[3])
        roots = np.array(roots)
        y_roots = np.array(y_roots)
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.tick_params(axis='both', which='major', labelsize=6)
        ax.scatter(x=roots, y=y_roots, marker='o', c='r', label='Корни')

        ax.plot(x_values, y_values, linewidth=2.0, label='y(x)')
        ax.legend(loc='lower right', fontsize=6)
        ax.set(xlim=(np.amin(x_values), np.amax(x_values)),
               ylim=(np.amin(y_values), np.amax(y_values)))
        ax.set_ylabel("Y", fontsize=7)
        ax.set_xlabel("X", fontsize=7)
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

    def window_preparation(self):
        set_standard_geometry(self, 800, 750)
        self.prepare_table_data()
        self.prepare_picture()


class MainWindow:
    def __init__(self):
        self.tk = tk
        self.window = tk.Tk()
        self.window.title('Метод уточнения корней Брента')
        self.calculations_done = False
        self.roots_values = []
        self.table_data = []

        self.input_function = tk.StringVar()
        self.input_function.trace('w', self.writing)
        self.input_a = tk.StringVar()
        self.input_a.trace('w', self.writing)
        self.input_b = tk.StringVar()
        self.input_b.trace('w', self.writing)
        self.input_epsilon = tk.StringVar(value='Эпсилон')
        self.input_epsilon.trace('w', self.writing)
        self.input_nmax = tk.StringVar(value='Nmax')
        self.input_nmax.trace('w', self.writing)
        self.input_h = tk.StringVar()
        self.input_h.trace('w', self.writing)
        self.all_data_input = False

        self.function = None
        self.a = None
        self.b = None
        self.h = None
        self.nmax = None
        self.epsilon = 1e-8
        self.count_numbers = 8

    def writing(self, *arg):
        self.all_data_input = False

    def prepare_window(self):
        set_standard_geometry(self, 500, 200)

        buttons_frame = tk.Frame(self.window)
        buttons_frame.pack(expand=True)
        buttons_frame.rowconfigure(0, weight=1)
        buttons_frame.rowconfigure(1, weight=1)
        buttons_frame.rowconfigure(2, weight=1)
        buttons_frame.rowconfigure(3, weight=1)
        for _ in range(3):
            buttons_frame.columnconfigure(_, weight=1)

        paddings = {'padx': 10, 'pady': 10}
        input_function_label = tk.Label(buttons_frame, text="Функция:")
        input_function_label.grid(row=0, column=0, **paddings)
        input_function_field = tk.Entry(buttons_frame, textvariable=self.input_function)
        input_function_field.grid(row=1, column=0, **paddings)

        space_function_label = tk.Label(buttons_frame, text="Шаг:")
        space_function_label.grid(row=2, column=0, **paddings)
        space_function_field = tk.Entry(buttons_frame, textvariable=self.input_h)
        space_function_field.grid(row=3, column=0, **paddings)

        start_text = tk.Label(buttons_frame, text="Начало отрезка:")
        start_text.grid(row=0, column=1, **paddings)
        start_field = tk.Entry(buttons_frame, textvariable=self.input_a)
        start_field.grid(row=1, column=1, **paddings)

        end_text = tk.Label(buttons_frame, text="Конец отрезка:")
        end_text.grid(row=2, column=1, **paddings)
        end_field = tk.Entry(buttons_frame, textvariable=self.input_b)
        end_field.grid(row=3, column=1)

        epsilon_field = tk.Entry(buttons_frame, textvariable=self.input_epsilon)
        epsilon_field.grid(row=0, column=2)

        epsilon_field = tk.Entry(buttons_frame, textvariable=self.input_nmax)
        epsilon_field.grid(row=1, column=2)

        get_graph_button = tk.Button(buttons_frame, command=self.get_roots, text='Вычислить корни', width=30,
                                     background='palevioletred', fg='pink', activebackground='palevioletred')
        get_graph_button.grid(row=2, column=2, **paddings)

        get_graph_button = tk.Button(buttons_frame, command=self.get_graph, text='Вывести график и таблицу '
                                                                                 'значений', width=30)
        get_graph_button.grid(row=3, column=2, **paddings)

    def start_window(self):
        self.window.mainloop()

    @staticmethod
    def find_count_numbers(input_epsilon):
        counter = 0
        while abs(input_epsilon) < 1:
            counter += 1
            input_epsilon *= 10
        return counter

    def method_of_bisections(self, a, b, count):
        """
         0 - не вычслен корень
         2 - не вычислен и дальше пойти не может из-за nmax
         1 - вычислен
        :param a:
        :param b:
        :param count:
        :return:
        """
        x = (a + b) / 2
        if eval(self.function.replace('x', 'a')) * eval(self.function.replace('x', 'b')) > 0:
            return 0
        if abs(eval(self.function)) < self.epsilon and round(x, self.count_numbers) not in self.roots_values:
            self.roots_values.append(round(x, self.count_numbers))
            return self.nmax - count + 1
        if abs(b - a) < self.epsilon:
            return 0
        if count - 1 == 0:
            return -1

        res1 = self.method_of_bisections(a, x, count - 1)
        if res1 > 0:
            return res1
        elif res1 == -1:
            return -1
        res2 = self.method_of_bisections(x, b, count - 1)
        if res2 > 0:
            return res2
        elif res2 == -1:
            return -1
        return 0

    def data_checking(self):
        x = 200
        try:
            self.function = self.input_function.get()
            eval(str(self.function))
        except Exception:
            message.showerror('Ошибка', 'Функция введена некорректно')
            return 0
        try:
            self.a = float(self.input_a.get())
        except Exception:
            message.showerror('Ошибка', 'Начало отрезка введен некорректно')
            return 0
        try:
            self.b = float(self.input_b.get())
        except Exception as err:
            print(err)
            message.showerror('Ошибка', 'Конец отрезка введен некорректно')
            return 0
        try:
            self.h = float(self.input_h.get())
        except Exception:
            message.showerror('Ошибка', 'Шаг введен некорректно')
            return 0
        if self.a >= self.b:
            message.showerror('Ошибка', 'Начало отрезка больше или равно концу')
            return 0
        if self.h <= 0:
            message.showerror('Ошибка', 'Шаг меньше или равен 0')
            return 0
        if self.h > abs(self.a - self.b):
            message.showerror('Ошибка', 'Шаг больше отрезка')
            return 0
        if floor(abs(self.a - self.b) / self.h) < 1:
            message.showerror('Ошибка', 'Шаг слишком большой')
            return 0
        try:
            self.epsilon = float(self.input_epsilon.get())
        except Exception:
            message.showerror('Ошибка', 'Эпсилон введена некорректно')
            return 0
        if self.epsilon >= 1 or self.epsilon < 0:
            message.showerror('Ошибка', 'Эпсилон введена некорректно')
            return 0
        try:
            self.nmax = int(self.input_nmax.get())
        except Exception:
            message.showerror('Ошибка', 'Максимальное количество итераций введено некорректно')
            return 0
        if self.nmax <= 0:
            message.showerror('Ошибка', 'Максимальное количество итерация меньше или равно 0')
            return 0
        return 1

    def get_roots(self):
        if not self.data_checking():
            return
        self.roots_values = []
        self.table_data = []
        self.count_numbers = self.find_count_numbers(self.epsilon)
        step = self.h
        counter = 0
        while step * (counter) + self.a < self.b:
            res = self.method_of_bisections(self.a + step * counter, self.a + step * (counter + 1), self.nmax)
            if step * (counter + 1) + self.a >= self.b:
                part = f'[{round(self.a + step * counter, self.count_numbers)}; ' \
                       f'{round(self.a + step * (counter + 1), self.count_numbers)}]'
            else:
                part = f'[{round(self.a + step * counter, self.count_numbers)}; ' \
                       f'{round(self.a + step * (counter + 1), self.count_numbers)})'
            if res == -1:
                self.table_data.append([len(self.table_data) + 1, part,
                                        '-', '-', 2])
            if res > 0:
                x = self.roots_values[-1]
                self.table_data.append([len(self.table_data) + 1, part,
                                        x, round(eval(self.function), self.count_numbers), res, '-'])
            counter += 1
        self.all_data_input = True
        print(self.table_data)

    def get_graph(self):
        # TODO
        if not self.all_data_input:
            message.showwarning('Ошибка', 'Корни ещё не вычислялись.')
            return
        child_window = ResultWindow(self.window, self.function, self.a, self.b, self.h, self.roots_values,
                                    self.table_data)
        child_window.start_window()


# def main_window():
#
#     window = tk.Tk()
#     window.title('Метод уточнения корней Брента')
#     set_standard_geometry(window, 600, 400)

# plot = Figure(figsize=(5, 5))
# graph = FigureCanvasTkAgg(plot, window)
# graph.get_tk_widget().grid(row=0, column=0)

# canvas = tk.Canvas(window, borderwidth=0, background="#ffffff", width=800)
# table_frame = tk.Frame(canvas, background="#ffffff", width=800)
# vsb = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
# canvas.configure(yscrollcommand=vsb.set)
# canvas.grid(row=1, column=0)
# canvas.create_window((2, 2), window=table_frame, anchor="nw")
# table_frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

# buttons_frame = tk.Frame(window)
# buttons_frame.grid(row=0, column=0)
# buttons_frame.rowconfigure(0, weight=1)
# buttons_frame.rowconfigure(1, weight=1)
# buttons_frame.rowconfigure(2, weight=1)
# buttons_frame.rowconfigure(3, weight=1)
# for _ in range(3):
#     buttons_frame.columnconfigure(_, weight=1)
#
# paddings = {'padx': 10, 'pady': 10}
# input_function_label = tk.Label(buttons_frame, text="Функция:")
# input_function_label.grid(row=0, column=0, **paddings)
# input_function_field = tk.Entry(buttons_frame)
# input_function_field.grid(row=1, column=0, **paddings)
#
# space_function_label = tk.Label(buttons_frame, text="Шаг:")
# space_function_label.grid(row=2, column=0, **paddings)
# space_function_field = tk.Entry(buttons_frame)
# space_function_field.grid(row=3, column=0, **paddings)
#
# start_text = tk.Label(buttons_frame, text="Начало отрезка:")
# start_text.grid(row=0, column=1, **paddings)
# start_field = tk.Entry(buttons_frame)
# start_field.grid(row=1, column=1, **paddings)
#
# end_text = tk.Label(buttons_frame, text="Конец отрезка:")
# end_text.grid(row=2, column=1, **paddings)
# end_field = tk.Entry(buttons_frame)
# end_field.grid(row=3, column=1)
#
# get_graph_button = tk.Button(buttons_frame, command=get_graph, text='Вычислить корни')
# get_graph_button.grid(row=1, column=2, **paddings)
#
# window.mainloop()

# Основные составляющие интерфейса: поле ввода, вывода и кнопка для перевода
# Распределяем вес для строк и столбцов по grid

# padding = {'padx': 10, 'pady': 5}
# # Надпись над полем ввода
# first_field_text = tk.StringVar(value='Число в 9-ной '
#                                       'системе' if MODE_OF_NUMBER_SYSTEM else 'Число в 10-ной системе')
# first_field_label = tk.Label(window, textvariable=first_field_text)
# first_field_label.grid(row=0, column=0, **padding)
# # Надпись на лейбом с результатом
# second_field_label = tk.Label(window, text='Результат')
# second_field_label.grid(row=0, column=2, **padding)
# # Поле ввода
# enter_text = tk.StringVar()
# enter_field = tk.Entry(window, width=30, textvariable=enter_text)
# enter_text.trace('w', check_symbols_line)
# enter_field.grid(row=1, column=0)
# enter_field.bind("<Up>", lambda event: translate())
# # Кнопка для перевода
# translate_button = tk.Button(window, text='Перевести', command=translate,
#                              padx="44", pady="7", background="DodgerBlue3", foreground="#ccc")
# translate_button.grid(row=1, column=1, **padding)
# # Лэйбл с результатом
# result_text = tk.StringVar(name=' ' * 30)
# result_label = tk.Label(window, textvariable=result_text, width=30)
# result_label.grid(row=1, column=2)
#
# # Вместо клавиатуры
# # ., 0, backspace
# keymap_style = {"padx": "5", "pady": "5", "background": "DodgerBlue3", "foreground": "#ccc", "font": '13'}
# important_button_1 = tk.Button(window, text='.', command=lambda: click_number_button('.'), **keymap_style)
# important_button_1.grid(row=2, column=0)
# important_button_2 = tk.Button(window, text='↩', command=erase_last_symbol, **keymap_style)
# important_button_2.grid(row=2, column=2)
# numb = 0
# zero = tk.Button(window, text='0', command=lambda x=numb: click_number_button(x), **keymap_style)
# zero.grid(row=2, column=1)
# numbers_buttons = dict()
# # циферки от 0 до 9
# for i in range(3, 6):
#     for j in range(3):
#         numb += 1
#         numbers_buttons[numb] = tk.Button(window, text=f'{numb}',
#                                           command=lambda x=numb: click_number_button(x) if not
#                                           (x == 9 and MODE_OF_NUMBER_SYSTEM) else
#                                           message.showerror('Ошибка ввода',
#                                                             'Введено 9 в девятеричной системе счисления'),
#                                           **keymap_style)
#         numbers_buttons[numb].grid(row=i, column=j)
# minus_button = tk.Button(window, text='-', command=lambda: click_number_button('-'), **keymap_style)
# minus_button.grid(row=6, column=1)
#
# window.mainloop()
# h = int(input())
# a = -10
# b = 10
window = MainWindow()
# window.function = 'x**2 - 5'
# print(window.find_count_numbers(0.0001))
# step = round(abs(a-b)/h, window.count_numbers)
# counter = 1
# while step*counter + a < b:
#     window.method_of_bisections(-10+step*counter, -10+step*(1+counter))
#     counter += 1
# print(window.roots_values)
window.prepare_window()
window.start_window()
