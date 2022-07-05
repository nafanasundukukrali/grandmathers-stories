"""
# Программа для нахождения интеграла функции методами правых прямоугольников и 3/8
# Входные и выходные данные прописаны в соотвествующих функциях программы
"""

import math

# Точность
epsilon = 10**-3

# Функция, для которой интегралы вычисляются
def d_function(x: float):
    return x**2

# Первообразная той функции
def function(x: float):
    return x**3/3


def numeric_type(number: str):
    """
    Проверка строки на то, что в ней записано число.
    Параметр: строка number, в которой хранится предполагаемое число
    Выходные данные: True False
    """
    # Убираем минус в начале -
    if not number:
        return False
    if number[0] == '-':
        number = number[1:]
    # Проверяем число на экспоненциальный формат (убираем e и e-, если они не стоят в начале и конце)
    if ('e' in number or 'E' in number) and number[0] != 'e' and number[0] != 'E' and number[-1] != '-':
        if 'e+' in number:
            number = number.replace('e+', '', 1)
        elif 'e-' in number:
            number = number.replace('e-', '', 1)
        else:
            number = number.replace('e', '', 1)
        if 'E+' in number:
            number = number.replace('E+', '', 1)
        elif 'E-' in number:
            number = number.replace('E-', '', 1)
        else:
            number = number.replace('E', '', 1)
    # Убираем точку
    if '.' in number and number[0] != '.' and number[-1] != '.':
        number = number.replace('.', '', 1)
    # Проверяем, что остались одни цифры
    return number.isdigit()


def method_of_right_rectangles(a: float, b: float, n: int):
    """
    Метод правых прямоугольников. В основе лежит то, что площадь под фукнцией делить на множество
    маленьких прямоугольников, одна сторона которого значения функции в точке, а другая delta.
    :param a: начало отрезка
    :param b: конец отрезка
    :param n: количество разбиений
    :return: Результат вычисления интегралла данным методом
    """
    # Вычисление дельты
    delta = abs((a-b)/n)
    # Сумма "сторон", равных значению функции в точке
    result = 0
    # Вычисление функции
    for i in range(1, n+1):
        result += d_function(a+i*delta)
    # Возврат суммы площадей прямоугольников
    return result*delta


def method_of_three_divide_8(a: float, b: float, n: int):
    """
    Метод 3/8. Смысл заключаются в том, что мы берём кубическую параболу, максимально близкую к заданной функции,
    и смотрим плозадь уже под этой кривой. Площадь вычисляется на основании формулы Ньютона. Так как у нас для формулы
    есть необходимость, взятия 4 точек при разбиении n, то, мы исключая повторы, смотрим только каждую третью точку.
    Поэтому n должно быть кратно 3.
    :param a: начало отрезка
    :param b: конец отрезка
    :param n: количество разбиений
    :return: значение интегралла
    """
    # Дельта
    delta = abs((a - b) / n)
    result = 0
    for i in range(n//3):
        result += (d_function(a+i*3*delta) + 3*d_function(a+i*3*delta + delta) + 3*d_function(a+i*3*delta + 2*delta)
                   + d_function(a+i*3*delta + 3*delta))
    return result*delta*3/8


def main():
    # Ввод начала отрезка
    a = input('Введите начало отрезка: ')
    while not numeric_type(a):
        print('Начало отрезка введено некорректно.')
        a = input(f'Введите начало отрезка: ')
    a = float(a)
    # Ввод конца отрезка
    b = input('Введите конец отрезка: ')
    while not numeric_type(b):
        print('Конец отрезка введён неправильно.')
        b = input(f'Введите конец отрезка: ')
    b = float(b)
    # Ввод первого количества разюиений
    n1 = input('Введите первое количество участков разбиения: ')
    while not n1.isdigit():
        print('Первое количество участков разбиения введено некорректно.')
        n1 = input('Введите первое количество участков разбиения: ')
    n1 = int(n1)
    # Ввод второго количества разбиений
    n2 = input('Введите второе количество участков разбиения: ')
    while not n2.isdigit():
        print('Второе количество участкой разбиения введено некорректно.')
        n2 = input('Введите второе количество участков разбиения: ')
    n2 = int(n2)
    # Выбор минимального n с учётом кратности 3
    if n1 % 3 == 0 and n2 % 3 != 0:
        nx = n1
    elif n2 % 3 == 0 and n1 % 3 != 0:
        nx = n2
    else:
        nx = min(n1, n2)
    # "Реальный" определённый интегралл
    real_result = function(b) - function(a)
    # Результат через метод правых прямоугольников на n1
    result_first_n_rectangle = method_of_right_rectangles(a, b, n1)
    # Результат через метод правых прямоугольникоу на n2
    result_second_n_rectangle = method_of_right_rectangles(a, b, n2)
    # Нахождение абсолютной и относительной погрешностей метода прямоугольников
    first_absolute_error = abs(real_result - method_of_right_rectangles(a, b, nx))
    first_relative_error = first_absolute_error/abs(real_result)*100
    # Нахождение погрешной и значений вметода 3/8 с учётом крастности 3
    if n1 % 3 == 0:
        result_first_n_three_divide_8 = method_of_three_divide_8(a, b, n1)
    if n2 % 3 == 0:
        result_second_n_three_divide_8 = method_of_three_divide_8(a, b, n2)
    if nx % 3 == 0:
        second_absolute_error = abs(real_result - method_of_three_divide_8(a, b, nx))
        second_relative_error = second_absolute_error/abs(real_result)*100
    # Вывод таблицы и погрешностей методов
    print('|' + ('-' * 30 + '|') + ('-' * 21 + '|') * 2)
    print('|' + ' ' * 30 + '|' + ' ' * 10 + 'n1' + ' ' * 9 + '|' + ' ' * 10 + 'n2' + ' ' * 9 + '|')
    print('|' + ('-' * 30 + '|') + ('-' * 21 + '|') * 2)
    print('|' + ' Метод правых прямоугольников ' + '|' + '{:^21.7f}'.format(result_first_n_rectangle)
          + '|' + '{:^21.7f}'.format(result_second_n_rectangle) + '|')
    print('|' + ('-' * 30 + '|') + ('-' * 21 + '|') * 2)
    print('|' + '{:^30}'.format('Метод 3/8') + '|' + ('{:^21.7f}'.format(result_first_n_three_divide_8) if n1 % 3 == 0
          else '{:^21}'.format('-')) + '|' + ('{:^21.7f}'.format(result_second_n_three_divide_8) if n2 % 3 == 0
          else '{:^21}'.format('-')) + '|')
    print('|' + ('-' * 30 + '|') + ('-' * 21 + '|') * 2)
    print('Абсолютная погрешность метода правых прямоугольников:', '{:.7f}'.format(first_absolute_error))
    print('Относительная погрешность метода правых прямоугольников:', '{:.7f}'.format(first_relative_error))
    print('Абсолютная погрешность метода 3/8:', '{:.7f}'.format(second_absolute_error) if nx % 3 == 0
          else '-')
    print('Относительная погрешность метода 3/8:', '{:.7f}'.format(second_relative_error) if nx % 3 == 0
          else '-')
    # Проверка на то, что можно сравнивать (невозможно определить, есл нельзя сосчитать порешности 3/8)
    if nx % 3 != 0:
        print('Невозможно определить, какой из методов работает хуже.')
        return
    if first_relative_error == second_relative_error:
        print('Оба метода работают одинаково.')
        return
    # Ввод максимального количества итераций (а то программа будет работать три миллиона лет)
    iteration_n = input('Введите максимальное количество итераций при вычислении n: ')
    while not iteration_n.isdigit():
        print('Максимальное количество итераций введено некорректно')
        iteration_n = input('Введите максимальное количество итераций при вычислении n: ')
    iteration_n = int(iteration_n)
    iteration_counter = 0
    # Проверка отнсоительно отнсоительной опгрешности какой метод хуже
    if first_relative_error > second_relative_error:
        # Хуже метод правых прямоугольников
        found_n = 1
        print('Метод правых прямоугольников менее точный.')
        # Вычисление n
        while (abs(method_of_right_rectangles(a, b, found_n) - method_of_right_rectangles(a, b, found_n*2)) >= epsilon
               and iteration_counter <= iteration_counter):
            found_n *= 2
            iteration_counter += 1
    else:
        # Хуже метод 3/8
        found_n = 3
        print('Метод 3/8 менее точный.')
        # Вычисление n
        while (abs(method_of_three_divide_8(a, b, found_n) - method_of_three_divide_8(a, b, found_n*2)) >= epsilon
               and iteration_counter <= iteration_n):
            found_n *= 2
            iteration_counter += 1
    # Вывод n, если это возможно
    if iteration_counter > iteration_n:
        print('За введённое количество итераций не получилось найти количество разбиений.')
    else:
        print('Искомое N:', found_n)


main()



