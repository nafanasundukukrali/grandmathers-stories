# Программа, формирования матрицу A по формуле ajk = sin(dj+fk) по массивам D и F, определения среднего арифметического
# положительных чисел каждой строки матрицы и количества элементов, меньших среднего арифметического, записи
# соотвествующих результатов в массивы AV и L и вывода матрицы A в виде матрицы и рядом столбцы AV и L.
# Входные данные прописаны в используемых фукнциях
# Выходные данные прописаны в используемых фукнциях

from math import sin
from array_functions import input_float_array


def matrix_init():
    """
    Фукнция для инициализации матрицы A на основании массивов D и F
    Входные даннные отсуствуют
    Выходные данные отствуют.
    Парметры отсуствуют.
    Возвращаемые значения: искомая матрица
    """
    # Ввод массива D
    print('Ввод массива D:')
    array_d = input_float_array()
    # Ввод массива F
    print('Ввод массива F:')
    array_f = input_float_array()
    # Формирование матрицы A согласно условиям задачи
    return [[sin(array_d[i]+array_f[j]) for j in range(len(array_f))] for i in range(len(array_d))]


def first_program():
    """
    Процедура для определения среднего арифметического положительных чисел каждой строки матрицы и количества
    элементов, меньших среднего арифметического, записи соотвествующих результатов в массивы AV и L и вывода
    матрицы A в виде матрицы и рядом столбцы AV и L.
    Параметры отсуствуют.
    Возвращаемые данные отсуствуют.
    Входные данные отсуствуют.
    Выходные данные: матрица, столбец массиа AV и столбец массива L
    """
    # Ввод матрицы A
    matrix = matrix_init()
    # Инициализация массива AV
    array_av = []
    # Инициализация массива L
    array_l = []
    # Формирование массивов AV и L согласно условиям задачи
    for i in range(len(matrix)):
        # Счётчик количества чисел больше 0
        count = 0
        # Переменная для подчёста суммы чисел больше 0
        elements_sum = 0
        for element in matrix[i]:
            if element > 0:
                count += 1
                elements_sum += element
        # Подсчёт среднего арифметического соотвествующих чисел (NAN, если среднее арифметическое не существует)
        if count == 0:
            array_av.append('NaN')
        else:
            array_av.append(elements_sum/count)
        # Формирвоание массива (NAN, если среднее арифметическое не существует)
        if type(array_av[-1]) != str:
            array_l.append(len(list(filter(lambda x: x < array_av[-1], matrix[i]))))
        else:
            array_l.append('NaN')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('{:^10.5f}'.format(matrix[i][j]), end=' ')
        print('{:^10.5f}'.format(array_av[i]) if type(array_av[i]) != str else 'NaN', array_l[i])


first_program()


