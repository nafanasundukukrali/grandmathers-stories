# Программа для перевода вещественных чисел из девятеричной в десятеричную систему счисления и обратно.

import tkinter as tk
import tkinter.messagebox as message

# Глобальная переменная для отслеживания в какую систему счисления мы переводим
# 0 - 10 -> 9
# 1 - 9 -> 10
# По умолчанию 9 -> 10
MODE_OF_NUMBER_SYSTEM = 1


def translate_from_9_to_10(line):
    # Перевод из девятеричной в десятеричную
    less_zero = 1 if line[0] == '-' else 0
    if less_zero:
        line = line[1:]
    left_side = line.split('.')[0]
    result = int(left_side, 9)
    if '.' in line:
        right_side = line.split('.')[1]
        max_step = len(right_side)
        for i in range(1, max_step+1):
            result += int(right_side[i-1]) * (9**(-i))
    return str(round(result if not less_zero else -result, 3))


def translate_from_10_to_9(line):
    # Перевод из десятичной в девятеричную
    less_zero = 1 if line[0] == '-' else 0
    if less_zero:
        line = line[1:]
    left_side = line.split('.')[0]
    result = ''
    start = int(left_side)
    while start > 8:
        result = str(start % 9) + result
        start //= 9
    result = str(start) + result
    if '.' in line:
        result += '.'
        right_side = line.split('.')[1]
        start = float('0.'+right_side)
        for i in range(3):
            start *= 9
            result += str(start)[0]
    return result if not less_zero else '-'+result


def check_if_there_number(text):
    # Проверка введённого числа на корректность
    if not text:
        return 'пустое поле ввода'
    if text == '.' or text == '-':
        return 'не является числом'
    if MODE_OF_NUMBER_SYSTEM == 1 and '9' in text:
        return 'в девятеричной системе счисления введена цифра 9'
    if text[-1] == '.':
        return 'не является числом'
    return 'OK'


def main_window():
    """
    Главная функция программы, вызывает сначала стартовое окно для выбора системы счисления по умолчанию,
    а затем само главное окно программы.
    """
    global MODE_OF_NUMBER_SYSTEM

    def check_symbols_line(*args):
        # Функция для проверки того, что пользователь не ввёл строку более 30 символов. В *args ничего полезного и
        # ничего нужного.
        if len(enter_text.get()) > 30:
            message.showwarning('Предупреждение',
                                'Вы ввели количество знаков, превышающее 30. Не хорошо, мы не одобряем. Больше вводить '
                                'нельзя!')
            enter_text.set(enter_text.get()[:30])
        if enter_text.get() and not enter_text.get()[-1].isdigit() and enter_text.get()[-1] != '.'\
                and enter_text.get()[-1] != '-':
            message.showwarning('Предупреждение',
                                'Последний символ введён некорректно. На вход принимаются цифры, знак "." или "-".')
            enter_text.set(enter_text.get()[:-1])

    def erase_last_symbol():
        if len(enter_text.get()):
            enter_text.set(enter_text.get()[:-1])

    def click_number_button(entry_symbol):
        enter_text.set(enter_text.get() + str(entry_symbol))
        check_symbols_line()

    def delete_first_field():
        # Очистка поля ввода
        enter_text.set('')

    def delete_second_field():
        # Очистка поля вывода
        result_text.set(' ')
        result_label.update()

    def delete_all_fields():
        # Очистка обоих полей
        delete_first_field()
        delete_second_field()

    def change_mode_of_system():
        # Смена режима перевода
        global MODE_OF_NUMBER_SYSTEM
        if MODE_OF_NUMBER_SYSTEM:
            first_field_text.set('Число в 10-й системе')
            first_field_label.update()
        else:
            first_field_text.set('Число в 9-й системе')
            first_field_label.update()
        MODE_OF_NUMBER_SYSTEM = 0 if MODE_OF_NUMBER_SYSTEM else 1

    def about():
        # Функция для вывода информации о программе
        message.showinfo('О программе', 'Автор: Конкина А. Н., ИУ7-23Б. \nПрограмма для перевода вещественных чисел из'
                                        ' девятеричной в десятеричную систему счисления и обратно.')

    def translate():
        # Перевод из одной системы счисления в другую
        line = enter_text.get()
        answer = check_if_there_number(line)
        if answer == 'OK':
            result = translate_from_9_to_10(line) if MODE_OF_NUMBER_SYSTEM else translate_from_10_to_9(line)
            result_text.set(result)
            result_label.update()
        else:
            message.showerror('Ошибка перевода', f'Невозможно выполнить перевод числа.\n'
                                                 f'Ошибка: {answer}')

    def set_standard_geometry(subject, w=600, h=400):
        """
        Функция для установки геометрических параметров окна. По умолчанию ширина 600, высота 400. Позиционирование
        по центру.
        """
        subject.geometry(f'{w}x{h}+{subject.winfo_screenwidth() // 2 - w // 2}'
                         f'+{subject.winfo_screenheight() // 2 - h // 2}')

    def get_information_dialog(text, text_bt1='Да', text_bt2='Нет', title='Системы счисления',
                               first_function=None, second_function=None):
        """
        Функция для вывода диалогового окна с бинарным выбором дальнейшего сценарий.
        :param second_function: Функция, которая будет вызываться при нажатии второй кнопки. Если функции не будет,
        то по умолчанию это кнопка будет считаться кнопкой смены режима (из 9 в 10)
        :param first_function: Функция, которая будет вызываться при нажатии первой кнопки. Если функции не будет, то
        по умолчанию это кнопка будет считаться кнопкой смены режима (из 10 в 9)
        :param text: Обязательный параметр - информационный тест
        :param text_bt1: Текст первой кнопки
        :param text_bt2: Текст второй кнопки
        :param title: Текст заголовка.
        :return:
        """
        def on_closing():
            # Функция для закрытия окна (почему-то destroy вызывает ошибку)
            ask_window.quit()
            exit(0)

        def choose_right():
            # Функция для смены параметра MODE_OF_NUMBER_SYSTEM (10 -> 9). Закрывает диалоговое окно.
            global MODE_OF_NUMBER_SYSTEM
            MODE_OF_NUMBER_SYSTEM = 1
            ask_window.quit()
            ask_window.destroy()

        def choose_left():
            # Функция для смены параметра MODE_OF_NUMBER_SYSTEM (9 -> 10). Закрывает диалоговое окно.
            global MODE_OF_NUMBER_SYSTEM
            MODE_OF_NUMBER_SYSTEM = 0
            ask_window.quit()
            ask_window.destroy()

        # Создание окна и задача его параметров
        ask_window = tk.Tk()
        ask_window.title(title)
        set_standard_geometry(ask_window, 400, 100)
        # Помещение теста диалогового окна по центру
        lb_1 = tk.Label(ask_window, text=text)
        lb_1.pack(side='top', pady=10)
        # Расположение кнопок
        bt_1 = tk.Button(ask_window, text=text_bt1, command=choose_left if not first_function else first_function,
                         padx="44", pady="7", background="DodgerBlue3", foreground="#ccc")
        bt_1.pack(side='left', padx=10)
        bt_2 = tk.Button(ask_window, text=text_bt2, command=choose_right if not second_function else second_function,
                         padx="44", pady="7", background="DodgerBlue3", foreground="#ccc")
        bt_2.pack(side='right', padx=10)

        ask_window.protocol("WM_DELETE_WINDOW", on_closing)
        ask_window.mainloop()

    # Вызов диалогового окна для выбора стартового обработчика выбора режима
    get_information_dialog('Выберете в какую систему счисления следует переводить: ', 'Из 10 в 9', 'Из 9 в 10')
    # Заготавливаются параметры главного окна
    window = tk.Tk()
    window.title('Калькулятор систем счисления 9 -> 10 | 10 -> 9')
    set_standard_geometry(window)

    # Меню главного окна
    menu = tk.Menu(window)
    menu_of_delete = tk.Menu(menu)
    menu_of_delete.add_command(label='Очистить первое поле', command=delete_first_field)
    menu_of_delete.add_command(label='Очистить второе поле', command=delete_second_field)
    menu_of_delete.add_command(label='Очистить все поля', command=delete_all_fields)
    menu.add_cascade(label='Очистка полей', menu=menu_of_delete)
    menu_of_modes = tk.Menu(menu)
    menu_of_modes.add_command(label='9 -> 10', command=change_mode_of_system)
    menu_of_modes.add_command(label='10 -> 9', command=change_mode_of_system)
    menu.add_cascade(label='Режим', menu=menu_of_modes)
    menu.add_command(label='Перевести', command=translate)
    menu.add_command(label='О программе', command=about)
    window.config(menu=menu)

    # Основные составляющие интерфейса: поле ввода, вывода и кнопка для перевода
    # Распределяем вес для строк и столбцов по grid
    for _ in range(3):
        window.columnconfigure(_, weight=1)
    for _ in range(7):
        window.rowconfigure(_, weight=1)
    padding = {'padx': 10, 'pady': 5}
    # Надпись над полем ввода
    first_field_text = tk.StringVar(value='Число в 9-ной '
                                          'системе' if MODE_OF_NUMBER_SYSTEM else 'Число в 10-ной системе')
    first_field_label = tk.Label(window, textvariable=first_field_text)
    first_field_label.grid(row=0, column=0, **padding)
    # Надпись на лейбом с результатом
    second_field_label = tk.Label(window, text='Результат')
    second_field_label.grid(row=0, column=2, **padding)
    # Поле ввода
    enter_text = tk.StringVar()
    enter_field = tk.Entry(window, width=30, textvariable=enter_text)
    enter_text.trace('w', check_symbols_line)
    enter_field.grid(row=1, column=0)
    enter_field.bind("<Up>", lambda event: translate())
    # Кнопка для перевода
    translate_button = tk.Button(window, text='Перевести', command=translate,
                                 padx="44", pady="7", background="DodgerBlue3", foreground="#ccc")
    translate_button.grid(row=1, column=1, **padding)
    # Лэйбл с результатом
    result_text = tk.StringVar(name=' '*30)
    result_label = tk.Label(window, textvariable=result_text, width=30)
    result_label.grid(row=1, column=2)

    # Вместо клавиатуры
    # ., 0, backspace
    keymap_style = {"padx": "5", "pady": "5", "background": "DodgerBlue3", "foreground": "#ccc", "font": '13'}
    important_button_1 = tk.Button(window, text='.', command=lambda: click_number_button('.'), **keymap_style)
    important_button_1.grid(row=2, column=0)
    important_button_2 = tk.Button(window, text='↩', command=erase_last_symbol, **keymap_style)
    important_button_2.grid(row=2, column=2)
    numb = 0
    zero = tk.Button(window, text='0', command=lambda x=numb: click_number_button(x), **keymap_style)
    zero.grid(row=2, column=1)

    numbers_buttons = dict()
    # циферки от 0 до 9
    for i in range(3, 6):
        for j in range(3):
            numb += 1
            numbers_buttons[numb] = tk.Button(window, text=f'{numb}',
                                              command=lambda x=numb: click_number_button(x) if not
                                              (x == 9 and MODE_OF_NUMBER_SYSTEM) else
                                              message.showerror('Ошибка ввода',
                                                                'Введено 9 в девятеричной системе счисления'),
                                              **keymap_style)
            numbers_buttons[numb].grid(row=i, column=j)
    minus_button = tk.Button(window, text='-', command=lambda: click_number_button('-'), **keymap_style)
    minus_button.grid(row=6, column=1)

    window.mainloop()

main_window()
