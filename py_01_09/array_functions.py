from number_functions import numeric_type, integer_check


def default_float_array_print(array):
    for element in array:
        print('{:^10.5f}'.format(element), end=' ')
    print()


def input_int_array_with_conditions(left=None, right=None):
    """
    Ввод массива при ограничении количества элементов справа и слева. С повторами.
    """
    # Ввод количества элементов массива с проверкой на условие
    array_len = input(f'Введите целочиселенное количество элементов массива: ')
    if not right and not left:
        while not array_len.isdigit():
            user_answer = input('Количество элементов введено некорректно. Повторить ввод? [Д/Н]: ')
            if user_answer == 'Д':
                array_len = input('Введите целочиселенное количество элементов массива: ')
            elif user_answer == 'Н':
                print('Операция прервана пользователем. Возвращён пустой массив.')
                return []
            else:
                print('Ответ введён пользователем некорректно. Повторите ввод ответа на вопрос.')
    else:
        while (not array_len.isdigit()) or int(array_len) > right or int(array_len) < left:
            user_answer = input('Количество элементов введено некорректно. Повторить ввод? [Д/Н]: ')
            if user_answer == 'Д':
                array_len = input('Введите целочиселенное количество элементов массива: ')
            elif user_answer == 'Н':
                print('Операция прервана пользователем. Возвращён пустой массив.')
                return []
            else:
                print('Ответ введён пользователем некорректно. Повторите ввод ответа на вопрос.')
    array_len = int(array_len)
    target_array = []
    for i in range(array_len):
        element = input(f'Введите {i + 1} числовой элемент массива: ')
        if not left and not right:
            while not integer_check(element):
                user_answer = input('Введён элемента не числового типа. Повторить ввод? [Д/Н]: ')
                if user_answer == 'Д':
                    element = input(f'Введите {i + 1} числовой элемент массива: ')
                elif user_answer == 'Н':
                    print('Операция прервана пользователем. Возвращён пустой массив.')
                    return []
                else:
                    print('Ответ введён пользователем некорректно. Повторите ввод ответа на вопрос.')
        else:
            while not integer_check(element) and not int(element) > left and not int(element) < right:
                user_answer = input(f'Введён элемента либо не числового типа, либо меньше {left}, либо больше '
                                    f'{right}. Повторить ввод? [Д/Н]: ')
                if user_answer == 'Д':
                    element = input(f'Введите {i + 1} числовой элемент массива: ')
                elif user_answer == 'Н':
                    print('Операция прервана пользователем. Возвращён пустой массив.')
                    return []
                else:
                    print('Ответ введён пользователем некорректно. Повторите ввод ответа на вопрос.')

        target_array.append(int(element))
    return target_array


def input_float_array():
    """
    Функция для ввода массива с числовыми элементами.
    Входные данные отсуствуют.
    Выходные данные: вводимый массив в соотвествии с элементами числового типа
    """
    # Ввод и проверка на корректность количества элементов массива
    array_len = input('Введите целочиселенное количество элементов массива: ')
    while not array_len.isdigit():
        user_answer = input('Количество элементов введено некорректно. Повторить ввод? [Д/Н]: ')
        if user_answer == 'Д':
            array_len = input('Введите целочиселенное количество элементов массива: ')
        elif user_answer == 'Н':
            print('Операция прервана пользователем. Возвращён пустой массив.')
            return []
        else:
            print('Ответ введён пользователем некорректно. Повторите ввод ответа на вопрос.')
    # Приведение полученной строки с количеством элементов к целочисленному типу данных
    array_len = int(array_len)
    # Целевой вводимый массив
    target_array = []
    # Пострчоный ввод и проверка на корректность элементов массива
    for i in range(array_len):
        element = input(f'Введите {i+1} числовой элемент массива: ')
        while not numeric_type(element):
            user_answer = input('Введён элемента не числового типа. Повторить ввод? [Д/Н]: ')
            if user_answer == 'Д':
                element = input(f'Введите {i+1} числовой элемент массива: ')
            elif user_answer == 'Н':
                print('Операция прервана пользователем. Возвращён пустой массив.')
                return []
            else:
                print('Ответ введён пользователем некорректно. Повторите ввод ответа на вопрос.')
        target_array.append(float(element))
    # Возврат целевого массива
    return target_array
