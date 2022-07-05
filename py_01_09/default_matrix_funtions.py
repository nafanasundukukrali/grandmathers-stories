from number_functions import numeric_type


def rectangle_matrix_input(float_type=True, char_type=False, input_rows=0, input_columns=0):
    """
    Ввод прямойгольной матрицы.
    Параметры:
    float_type: матрица числового типа
    char_type: матрица символьного типа
    input_rows: введённая матрица должна быть с определённым количеством строк
    input_columns: введённая матрица должна быть с определённым количеством столбцоы
    При отсуствии формальных параметров функция работает, будто необходимо ввести произвольную прямоугольную числовую
    матрицу
    Входные данные: количество строк и столбцов, в заисимости от параметров
    Выходные данные отсуствуют
    """
    # Ввод количества столбцов, если количсевто строк матрицы фиксировано
    if input_rows and not input_columns:
        print(f'Согласно введённым данным прошлой матрицы, в матрице должно быть {input_rows} строк.')
        user_n = input('Введите количество элементов строке новой матрицы: ')
        while not user_n.isdigit():
            user_answer = input('Количество элементов в строке матрицы введён некорректно. '
                                'Попробуйте ввести заново? [Д/Н]: ')
            if user_answer == 'Д':
                user_n = input('Введите количество элементов строке новой матрицы: ')
            elif user_answer == 'Н':
                print('Операция прервана.')
                return []
            else:
                print('Ответ введен некорректно. Повторите ввод.')
        n = int(user_n)
        m = input_rows
    # Ввод количества столбцов и строк, если матрица произвольная
    elif (not input_columns) and (not input_rows):
        user_n_and_m = input('Введите количество столбцов и количество строк через пробел: ')
        while (len(user_n_and_m.split(' ')) == 1 or not user_n_and_m.split(' ')[0].isdigit() or
               not user_n_and_m.split(' ')[1].isdigit()):
            user_answer = input('Параметры матрицы заданы неверно. Попробуйте ввести их заново? [Д/Н]: ')
            if user_answer == 'Д':
                user_n_and_m = input('Введите количество столбцов и количество строк через пробел: ')
            elif user_answer == 'Н':
                print('Операция прервана.')
                return []
            else:
                print('Ответ введен некорректно. Повторите ввод.')
        n = int(user_n_and_m.split(' ')[0])
        # Количество строк
        m = int(user_n_and_m.split(' ')[1])
    # Матрица фиксирована обоими параметрами
    else:
        print(f'Количество строк в предыдущей матрице: {input_rows}')
        m = input_rows
        print(f'Количество столбцов в предыдущей матрице: {input_columns}')
        n = input_columns
    # Переменная для целевой матрицы
    matrix = []
    # Если проверка вводиммых данных, если матрица числовая
    if float_type:
        for i in range(m):
            new_row = []
            for j in range(n):
                new_element = input(f'Введите {j + 1} числовой элемент {i + 1} строки матрицы: ')
                while not numeric_type(new_element):
                    user_answer = input('Введён элемент нечислового типа. Попробуйте ввести число заново? При '
                                        'отказе введённые данные в матрицу будут стёрты. [Д/Н]: ')
                    if user_answer == 'Д':
                        new_element = input(f'Введите {j + 1} числовой элемент {i + 1} строки матрицы: ')
                    elif user_answer == 'Н':
                        print('Операция прервана.')
                        return []
                    else:
                        print('Ответ введен некорректно. Повторите ввод.')
                new_row.append(float(new_element))
            matrix.append(new_row)
    # Проверка данных на длину, если матрица символьная
    elif char_type:
        for i in range(m):
            new_row = []
            for j in range(n):
                new_element = input(f'Введите {j + 1} символьный элемент {i + 1} строки матрицы: ')
                while len(new_element) > 1:
                    user_answer = input('Введён элемент не символьного типа. Попробуйте ввести число заново? При '
                                        'отказе введённые данные в матрицу будут стёрты. [Д/Н]: ')
                    if user_answer == 'Д':
                        new_element = input(f'Введите {j + 1} символьный элемент {i + 1} строки матрицы: ')
                    elif user_answer == 'Н':
                        print('Операция прервана.')
                        return []
                    else:
                        print('Ответ введен некорректно. Повторите ввод.')
                new_row.append(new_element)
            matrix.append(new_row)
    return matrix


def square_float_matrix_input():
    """
    Функция предназначенная для ввода числовой квадратной матрицы.
    Параметры отсуствуют.
    Входные данные: порядок матрицы и её элементы
    Выходные данные отсуствуют.
    Возвращаемое значение: вводимая матрица
    """
    # Ввод и проверка на корректность порядка матрицы.
    user_n = input('Введите порядок матрицы квадратичной: ')
    while not user_n.isdigit():
        user_answer = input('Порядок матрицы введён некорректно. Попробуйте ввести заново? [Д/Н]: ')
        if user_answer == 'Д':
            user_n = input('Введите порядок матрицы квадратичной: ')
        elif user_answer == 'Н':
            print('Операция прервана.')
            return []
        else:
            print('Ответ введен некорректно. Повторите ввод.')
    # Преобразование порядка матрицы к строковому типу
    n = int(user_n)
    # Целевая матрица
    matrix = []
    # Построчный ввод элементов матрицы и проверка их на корректность
    for i in range(n):
        new_row = []
        for j in range(n):
            new_element = input(f'Введите {j+1} числовой элемент {i+1} строки матрицы: ')
            while not numeric_type(new_element):
                user_answer = input('Введён элемент нечислового типа. Попробуйте ввести число заново? При '
                                    'отказе введённые данные в матрицу будут стёрты. [Д/Н]: ')
                if user_answer == 'Д':
                    new_element = input(f'Введите {j+1} числовой элемент {i+1} строки матрицы: ')
                elif user_answer == 'Н':
                    print('Операция прервана.')
                    return []
                else:
                    print('Ответ введен некорректно. Повторите ввод.')
            new_row.append(float(new_element))
        matrix.append(new_row)
    # Вводимой матрицы
    return matrix


def default_matrix_print(matrix, type_float=True):
    """
    Процедура для вывода матрицы.
    Параметры:
    Фактические параметры: matrix - матрица, которую надо вывести
    Формальные параметры: type_float: False - матрица будет выводиться просто через пробел. True - матрица будет
    выводиться с форматированием чисел
    Входные данные отсуствуют.
    Выходные данные: введённая матрица
    """
    # Если матрица числовая
    if type_float:
        for i in range(len(matrix)):
            for element in matrix[i]:
                print('{:^10.5f}'.format(element), end=' ')
            print()
    # Если матрица другого типа или пользователь выводит значения матрицы через пробел
    else:
        for row in matrix:
            print(*row)
