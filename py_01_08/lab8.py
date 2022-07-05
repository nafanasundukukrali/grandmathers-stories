# Программа, позволяющая с использованием меню обеспечить работу с целочисленными матрицами
# Входные данные прописаны в используемых фукнциях
# Выходные данные прописаны в используемых фукнциях

def integer_check(number: str) -> bool:
    """
    Проверка входной строки на содержание целого чила
    Входные данные: строка с предполагаемым числом
    Выходные данные: True, если строка - целове число, False в обратном случае
    """
    # Убираем - в начале
    if number[0] == '-':
        number = number[1:len(number)]
    # Проверяем, что E e не стоят в начале и  их количество
    if (number[0] != 'E' and number[0] != 'e' and number[-1] != '-' and number[-1] != '+' and
            number[-1] != 'E' and number[-1] != 'e' and number.count('e') < 2 and number.count('E') < 2 and
            number.count('-') < 2 and number.count('+') < 2):
        # Строка вида 1E1.0 не число
        if 'E' in number and '.' in number and '.' in number.split('E')[1]:
            return False
        # Строка вида 1e1.0 не число
        if 'e' in number and '.' in number and '.' in number.split('e')[1]:
            return False
        # Строка вида 1.272772 не целое число
        if 'e' not in number and 'E' not in number and '.' in number:
            return False
        # Строка с .e e. не число
        if 'e.' in number or '.e' in number or 'E.' in number or '.E' in number:
            return False
        # Если '.' и есть в числе, то только если это экспоненциальная запись
        number = number.replace('E-', '', 1)
        number = number.replace('e-', '', 1)
        number = number.replace('e+', '', 1)
        number = number.replace('e+', '', 1)
        number = number.replace('e', '', 1)
        number = number.replace('E', '', 1)
        number = number.replace('.', '', 1)
        # Проверяем, что осталось число
        if number.isdigit():
            return float(number).is_integer()
    else:
        return False


def matrix_input(matrix: list, n: int, m: int):
    """
    Функция для ввода матрицы
    Входные данные: список для матрицы, или уже используемая матрица, текущее количество строк и столбцов
    Выходные данные: количество строк и столбцов в матрице
    """
    # Ввод количества столбцов и строк, а также проверка, что аднные коректны
    user_n_and_m = input('Введите количество столбцов и количество строк через пробел: ')
    while (len(user_n_and_m.split(' ')) == 1 or not user_n_and_m.split(' ')[0].isdigit() or
            not user_n_and_m.split(' ')[1].isdigit()):
        user_answer = input('Параметры матрицы заданы неверно. Попробуйте ввести их заново? [Д/Н]: ')
        if user_answer == 'Д':
            user_n_and_m = input('Введите количество столбцов и количество строк через пробел: ')
        elif user_answer == 'Н':
            print('Операция прервана.')
            return n, m
        else:
            print('Ответ введен некорректно. Повторите ввод.')
    # Количество столбцов
    n = int(user_n_and_m.split(' ')[0])
    # Количество строк
    m = int(user_n_and_m.split(' ')[1])
    # "чистим" список со старой матрицей
    matrix.clear()
    # Построчный ввод данных матрицы
    for i in range(m):
        # Ввод строки с элементами (проверка на то, что элементов было введено n)
        list_of_numbers = list(input(f'Введите элементы {i+1} строки матрицы через пробел: ').split())
        while len(list_of_numbers) != n:
            user_answer = input(f'Было введено количество элементов отличное от {n}. Попробуйте ввести '
                                f'строку заново? [Д/Н]: ')
            if user_answer == 'Д':
                list_of_numbers = list(input('Введите количество столбцов и количество строк через пробел: ').split())
            elif user_answer == 'Н':
                print('Операция прервана. Массив будет отчистен.')
                matrix.clear()
                return n, m
            else:
                print('Ответ введен некорректно. Повторите ввод.')
        # Проверка корректности введенных элементов
        not_right_js = []
        right_elements = []
        for j in range(len(list_of_numbers)):
            if not integer_check(list_of_numbers[j]):
                not_right_js.append(j+1)
            else:
                right_elements.append(float(list_of_numbers[j]))
        # Повторный ввод неправильно введённых элементов
        while not_right_js:
            print(f'Предупреждение: на позициях {not_right_js} присутствуют нечисловые значения.', end=' ')
            user_answer = input('Попробуйте ввести их заново? При отказе ввёднные данные в матрицу будут стёрты. '
                                '[Д/Н]: ')
            if user_answer == 'Д':
                for j in not_right_js:
                    new_elem = input(f'Введите элемент на {j} позиции: ')
                    while not integer_check(new_elem):
                        user_answer = input('Введён элемент нечислового типа. Попробуйте ввести число заново? При '
                                            'отказе ввёднные данные в матрицу будут стёрты. [Д/Н]: ')
                        if user_answer == 'Д':
                            new_elem = input(f'Введите элемент на {j} позиции: ')
                        elif user_answer == 'Н':
                            print('Операция прервана.')
                            return n, m
                        else:
                            print('Ответ введен некорректно. Повторите ввод.')
                    right_elements.insert(j-1, float(new_elem))
                    not_right_js.pop(0)
            elif user_answer == 'Н':
                print('Операция прервана. Текущие данные матрицы будут стёрты.')
                matrix.clear()
                return n, m
            else:
                print('Ответ введен некорректно. Повторите ввод.')
        matrix.append(right_elements)
    return n, m


def add_row(matrix: list, n: int, m: int):
    """
    Функция для добавления строки в матрицу.
    Входные данные: матрица, количество столбцов и строк
    Выходные данные: новое количество столбцов и строк
    """
    # Проверка на то, что матрица не пустая
    if n == 0 or m == 0:
        print('В матрице отсуствуют строки и столбцы. Введите сначала матрицу.')
        return n, m
    # Ввод индекса, куда пользовать хочет добавить строку
    user_x = input(f'В матрице {m} строк. Введите позицию строки среди строк матрицы, '
                   f'куда следует её добавить, считая от 1: ')
    while not user_x.isdigit() or int(user_x) - 1 > m or int(user_x) - 1 < 0:
        user_answer = input('Ведена некорректная позиция строки в матрице. Попробуйте ввести снова? [Д/Н]: ')
        if user_answer == 'Д':
            user_x = input(f'В матрице {m} строк. Введите позицию строки среди строк матрицы, '
                           f'куда следует её добавить, считая от 1: ')
        elif user_answer == 'Н':
            print('Операция прервана.')
            return n, m
        else:
            print('Ответ введен некорректно. Повторите ввод.')
    # Выбор пользователем способа добавления строки
    while True:
        possible = input(f'Введите способ работы алгоритма: с функциями Python или алгоритмически [П/А]: ')
        if possible == 'П' or possible == 'А':
            break
        else:
            print('Ответ введен некорректно. Повторите ввод.')
    # Ввод элементов новой строки (проверка, что было введенно n)
    list_of_numbers = list(input(f'Введите элементы строки матрицы через пробел: ').split())
    while len(list_of_numbers) != n:
        user_answer = input(f'Было введено количество элементов отличное от {n}. Попробуйте ввести '
                            f'строку заново? [Д/Н]: ')
        if user_answer == 'Д':
            list_of_numbers = list(input('Введите элементы строки матрицы через пробел: ').split())
        elif user_answer == 'Н':
            print('Операция прервана. Массив будет отчистен.')
            matrix.clear()
            return n, m
        else:
            print('Ответ введен некорректно. Повторите ввод.')
    not_right_js = []
    right_elements = []
    # Проверка корректности ведённых чисел
    for j in range(len(list_of_numbers)):
        if not integer_check(list_of_numbers[j]):
            not_right_js.append(j + 1)
        else:
            right_elements.append(float(list_of_numbers[j]))
    while not_right_js:
        print(f'Предупреждение: на позициях {not_right_js} присутствуют нечисловые значения.', end=' ')
        user_answer = input('Попробуйте ввести их заново? При отказе ввёднные данные в матрицу будут стёрты. '
                            '[Д/Н]: ')
        if user_answer == 'Д':
            for j in not_right_js:
                new_elem = input(f'Введите элемент на {j} позиции: ')
                while not integer_check(new_elem):
                    user_answer = input('Введён элемент нечислового типа. Попробуйте ввести число заново? При '
                                        'отказе ввёднные данные в матрицу будут стёрты. [Д/Н]: ')
                    if user_answer == 'Д':
                        new_elem = input(f'Введите элемент на {j} позиции: ')
                    elif user_answer == 'Н':
                        print('Операция прервана.')
                        return n, m
                    else:
                        print('Ответ введен некорректно. Повторите ввод.')
                right_elements.insert(j - 1, float(new_elem))
                not_right_js.pop(0)
        elif user_answer == 'Н':
            print('Операция прервана. Текущие данные матрицы будут стёрты.')
            matrix.clear()
            return n, m
        else:
            print('Ответ введен некорректно. Повторите ввод.')
    # Приведение введённой позиции пользователя к целочисленному виду
    user_x = int(user_x)
    # Добавление строки
    if possible == 'П':
        # С использованием функционала Python
        matrix.insert(user_x-1, right_elements)
    else:
        # Алгоритмически
        if user_x - 1 < len(matrix):
            last_element = matrix[user_x-1].copy()
            matrix[user_x - 1] = right_elements.copy()
        else:
            last_element = right_elements.copy()
        for i in range(user_x, m):
            actual_element = matrix[i].copy()
            matrix[i] = last_element.copy()
            last_element = actual_element.copy()
        if m+1 > len(matrix):
            matrix.append(last_element.copy())
    return n, m + 1


def add_column(matrix: list, n: int, m: int):
    """
    Добавление столбца в матрицу.
    Входные данные: матрица, количество столбцов и строк
    Выходные данные: новое количество столбцов и строк
    """
    # Проверка, что матрица была введена
    if n == 0 or m == 0:
        print('В матрице отсуствуют строки и столбцы. Введите сначала матрицу.')
        return n, m
    # Вводколичества столбцов
    user_x = input(f'Количество стролбцов в матрице: {n}. Введите позицию столбца среди столбцов матрицы, '
                   f'куда следует его добавить, считая от 1: ')
    while not user_x.isdigit() or int(user_x) - 1 > n or int(user_x) - 1 < 0:
        user_answer = input('Ведена некорректная позиция столбца в матрице. Попробуйте ввести снова: ')
        if user_answer == 'Д':
            user_x = input(f'Количество стролбцов в матрице: {n}. Введите позицию столбца среди столбцов матрицы, '
                           f'куда следует его добавить, считая от 1: ')
        elif user_answer == 'Н':
            print('Операция прервана.')
            return n, m
        else:
            print('Ответ введен некорректно. Повторите ввод.')
    while True:
        possible = input(f'Введите способ работы алгоритма: с функциями Python или алгоритмически [П/А]: ')
        if possible == 'П' or possible == 'А':
            break
        else:
            print('Ответ введен некорректно. Повторите ввод.')
    # Ввод элементов столбца. Проверка на то, чтобы было введено m
    list_of_numbers = list(input(f'Количетсво строк: {m}. Введите элементы столбца матрицы через пробел: ').split())
    while len(list_of_numbers) != m:
        user_answer = input(f'Было введено количество элементов отличное от {m}. Попробуйте ввести '
                            f'столбец заново? [Д/Н]: ')
        if user_answer == 'Д':
            list_of_numbers = list(input('Введите элементы столбца матрицы через пробел: ').split())
        elif user_answer == 'Н':
            print('Операция прервана. Массив будет отчистен.')
            matrix.clear()
            return n, m
        else:
            print('Ответ введен некорректно. Повторите ввод.')
    # Проверка жлементов строки и их повторный ввод
    not_right_js = []
    right_elements = []
    for j in range(len(list_of_numbers)):
        if not integer_check(list_of_numbers[j]):
            not_right_js.append(j + 1)
        else:
            right_elements.append(float(list_of_numbers[j]))
    while not_right_js:
        print(f'Предупреждение: на позициях {not_right_js} присутствуют нечисловые значения.', end=' ')
        user_answer = input('Попробуйте ввести их заново? При отказе ввёднные данные в матрицу будут стёрты. '
                            '[Д/Н]: ')
        if user_answer == 'Д':
            for j in not_right_js:
                new_elem = input(f'Введите элемент на {j} позиции: ')
                while not integer_check(new_elem):
                    user_answer = input('Введён элемент нечислового типа. Попробуйте ввести число заново? При '
                                        'отказе ввёднные данные в матрице будут стёрты. [Д/Н]: ')
                    if user_answer == 'Д':
                        new_elem = input(f'Введите элемент на {j} позиции: ')
                    elif user_answer == 'Н':
                        print('Операция прервана.')
                        return n, m
                    else:
                        print('Ответ введен некорректно. Повторите ввод.')
                right_elements.insert(j - 1, float(new_elem))
                not_right_js.pop(0)
        elif user_answer == 'Н':
            print('Операция прервана. Текущие данные матрицы будут стёрты.')
            matrix.clear()
            return n, m
        else:
            print('Ответ введен некорректно. Повторите ввод.')
    # Преобразование позиции нового столбца в целочисленный вид
    user_x = int(user_x)
    # Выбор работы алгоритма
    if possible == 'П':
        # Ввод с помощью функционала языка
        for i in range(m):
            matrix.insert(user_x-1, right_elements[i])
    else:
        # Ввод алгоритмически
        for i in range(m):
            if user_x - 1 < len(matrix[i]):
                last_element = matrix[i][user_x-1]
                matrix[i][user_x - 1] = right_elements[i]
            else:
                last_element = right_elements[i]
            for j in range(user_x, n):
                actual_element = matrix[i][j]
                matrix[i][j] = last_element
                last_element = actual_element
            if n+1 > len(matrix[i]):
                matrix[i].append(last_element)
    return n+1, m


def remove_row(matrix: list, n: int, m: int):
    """
    Удаление строки матрицы.
    Входные данные: текущее количество столбцов и сток соотвественно
    Выходные данные: обновленное колчиество строк и столбцов
    """
    # Проверка на то, что введённая матрица не пустая
    if m == 0 or n == 0:
        print('Элементы в матрице отствуют.')
        return n, m
    # Ввод позиции строки, которую надо удалить
    user_x = input(f'В матрице {m} строк. Введите позицию строки, которую надо удалить среди строк матрицы, '
                   f' считая от 1: ')
    while not user_x.isdigit() or int(user_x) - 1 >= m or int(user_x) - 1 < 0:
        user_answer = input('Ведена некорректная позиция строки в матрице. Попробуйте ввести снова? [Д/Н]: ')
        if user_answer == 'Д':
            user_x = input(f'В матрице {m} строк. Введите позицию строки, которую надо удалить среди '
                           f'строк матрицы, считая от 1: ')
        elif user_answer == 'Н':
            print('Операция прервана.')
            return n, m
        else:
            print('Ответ введен некорректно. Повторите ввод.')
    # Ввода способа работа алгоритма
    while True:
        possible = input(f'Введите способ работы алгоритма: с функциями Python или алгоритмически [П/А]: ')
        if possible == 'П' or possible == 'А':
            break
        else:
            print('Ответ введен некорректно. Повторите ввод.')
    # Приведение позиции к виду для работы с матрицей
    user_x = int(user_x)-1
    # Выбор способа работы программы
    if possible == 'П':
        # Возможность языка
        del matrix[user_x]
    else:
        # Алгоритмически
        if user_x+1 != m:
            for i in range(user_x+1, m):
                matrix[i-1] = matrix[i].copy()
    return n, m - 1


def remove_column(matrix: list, n: int, m: int):
    """
    Функция для удаления столбца матрицы
    Входные данные: матрица, количество столбцов и строк
    Выходные данные: обновлённое количество столбцов и строк
    """
    # Проверка, что матрица не пустая
    if n == 0 or m == 0:
        print('Элементы в матрице отствуют.')
        return n, m
    # Ввод позици стролбца, который надо удалить, и проверка корректности позиции
    user_x = input(f'Количество столбцов в матрице: {n}. Введите позицию столбца, который надо удалить из матрицы, '
                   f'считая от 1: ')
    while not user_x.isdigit() or int(user_x) - 1 >= n or int(user_x) - 1 < 0:
        user_answer = input('Ведена некорректная позиция строки в матрице. Попробуйте ввести снова? [Д/Н]: ')
        if user_answer == 'Д':
            user_x = input(f'Количество столбцов в матрице: {n}. Введите позицию столбца, который надо удалить из '
                           f'матрицы, считая от 1: ')
        elif user_answer == 'Н':
            print('Операция прервана.')
            return n, m
        else:
            print('Ответ введен некорректно. Повторите ввод.')
    # Выбор способа работы алгоритма
    while True:
        possible = input(f'Введите способ работы алгоритма: с функциями Python или алгоритмически [П/А]: ')
        if possible == 'П' or possible == 'А':
            break
        else:
            print('Ответ введен некорректно. Повторите ввод.')
    # Приведение введённой позиуи к виду,удобной для работы с матрицей
    user_x = int(user_x)-1
    # Выбор способа работы алгоритма
    if possible == 'П':
        # Функционал языка
        for i in range(len(matrix)):
            del matrix[i][user_x]
    else:
        # Алгоритмически
        for i in range(m):
            if user_x+1 != n:
                for j in range(user_x+1, n):
                    matrix[i][j-1] = matrix[i][j]
    return n-1, m


def find_row(matrix, n, m):
    """
    Процедура для поиска строки, имеющую наибольшее количество подряд идущих одинаковых элементов
    Входные данные: матрица, текущее количество столбцов, количество строк
    """
    # Проверка, что матрица не пустая
    if n == 0 or m == 0:
        print('Элменты в матрице отсуствуют!')
        return
    # Максимальное количество одинаковых элементов в матрице
    all_max = 1
    # Индекс первой строки, имеющей максимальное количество одинаковых элементов
    row_number = -1
    # Перебор всех строк матрицы и сравнение локального максимального количества одинаковых элементов с общим
    for i in range(m):
        # Последний рассмотренный элемент
        last_element = matrix[i][0]
        # Текущее максимальное количество подряд идущих элементов
        double_local_max = 1
        # Локальный максимум в строке
        local_max = 0
        for j in range(1, n):
            if last_element == matrix[i][j]:
                double_local_max += 1
            else:
                local_max = max(double_local_max, local_max)
                double_local_max = 1
            last_element = matrix[i][j]
        local_max = max(double_local_max, local_max)
        # Сравнение локального максимума с максимумом
        if local_max > all_max:
            all_max = local_max
            row_number = i
    # Если all_max == 1, значит в строках отсуствуют подряд идущие одинаковые элементы. Вывод сообщения
    if all_max == 1:
        print('В матрице отсутвуют строки с одинаковыми элементами.')
        return
    # Вывод строки с максимальным количеством одинаковых идущих подряд элементов
    print(f'Максимальное количество подряд идущих одинаковых элементов: {all_max}')
    print(f'Строка: ')
    for i in range(n):
        print(matrix[row_number][i], end=' ')
    print()


def find_column(matrix, n, m):
    """
    Процедура для поиска столбца, имеющего наибольшее количество нулевых элементов
    Входные данные: матрица, количество столбцов, количество строк
    """
    # Проверка того, что матрица не пустая
    if n == 0 or m == 0:
        print('Элменты в матрице отсуствуют!')
        return
    # Общее максимальное количество нулевых элементов
    all_max = -1
    # Столбец с максимальным количеством нулевых элементов
    column_number = -1
    # Перебор столбцов матрицы
    for i in range(n):
        # При каждой итерации локальный счётчик нулей обнуляется
        count = 0
        # Поиск количество нулей в столбце
        for j in range(m):
            if matrix[j][i] == 0:
                count += 1
        # Сравнение локльного количества с общим количеством
        if count > all_max:
            all_max = count
            column_number = i
    # Проверка на то, что есть хотя бы один столбец с нулевым элементов в матрице
    if all_max == 0:
        print('Ни один столбец не содержит нулевого элемента.')
        return
    # Вывод количества нулей и интересующий столбец
    print(f'Максимальное количество нулевых элементов: {all_max}')
    print(f'Столбец: ')
    for i in range(m):
        print(matrix[i][column_number], end=' ')
    print()


def change_rows(matrix, n, m):
    """
    Процедура для перестановки местами строки с наибольшим и наименьшим количеством отрицательных элементов матрицы
    Входные данные: матрица, количество столбцов матрице, количество строк
    """
    # Проверка на то, что матрица не пустая
    if n == 0 or m == 0:
        print('Элементы в матрице отсуствуют!')
        return
    # Каноничный алгоритм добавления/удаления дабвилять/удалять строки мтарицы
    # Максимум и минимум отрицательных чисел в строках. Изначально это количество отрицательных занчений в 1 строке
    all_max = all_min = len(list(filter(lambda x: x < 0, matrix[0][:n])))
    # Индексы минимума и максимума отцательных значений соотвественно. Изначально это индекс 1 строки матрицы
    index_row_min = index_row_max = 0
    # Перебор каждой строки матрицы
    for i in range(1, m):
        # Локальное количество отрицательных элементов
        not_plus = len(list(filter(lambda x: x < 0, matrix[i][:n])))
        # Сравнение с максимумом
        # Персетраховка на случай, если в первой строке было 0 элементов, но в строке есть максимум и минимум
        if all_min == 0 and not_plus != 0:
            index_row_max = i
            all_min = not_plus
        # Сравнение с максимумом
        if not_plus >= all_max:
            index_row_max = i
            all_max = not_plus
        # Сравнение с минимумом
        if not_plus <= all_min and not_plus != 0:
            index_row_min = i
            all_min = not_plus
    # Случай, если в матрице не отрицательных чисел
    if all_max == 0:
        print('В матрице отствуют отрицательные числа.')
    # Случай, если в матрице есть строки с отрицательными числами, но их количество в них одинаково
    elif all_max == all_min:
        print('В строках, в которых есть отрицательыне числа, количество совпадает.')
    # Случай, если всё хорош и можно вычислить максимум и минимум
    else:
        print('Строка с максимальным числом отрицательных элементов:')
        print(*matrix[index_row_max])
        print('Строка с минимальным числом отрицательных элементов:')
        print(*matrix[index_row_min])
        print('Новая матрица: ')
        # Перестановка строк
        copy_row = matrix[index_row_max].copy()
        matrix[index_row_max] = matrix[index_row_min].copy()
        matrix[index_row_min] = copy_row.copy()
        for i in range(m):
            print(*matrix[i])


def change_columns(matrix, n, m):
    """
    Процедура для перестановки местами столбцы с максимальной и минимальной суммой элементов
    Входные данные: матрица, количество столбцов в ней, количество строк в ней
    """
    # Проверка того, что матрица не пустая
    if n == 0 or m == 0:
        print('Элементы в матрице отсуствуют!')
        return
    # Минимум и максимум суммы в матрице. Присваим исходное значение - сумма в первом столбце
    all_max = all_min = 0
    for i in range(m):
        all_max += matrix[i][0]
        all_min += matrix[i][0]
    # Индекс столбца с минимумом и максимумом суммы
    index_column_min = index_column_max = 0
    # Перебор столбцов матрицы
    for i in range(1, n):
        # Сумма столбца матрицы
        local_sum = 0
        for j in range(m):
            local_sum += matrix[j][i]
        # Сравнение максимума столбца и минимума
        if local_sum >= all_max:
            all_max = local_sum
            index_column_max = i
        if local_sum <= all_min:
            all_min = local_sum
            index_column_min = i
    if all_max == all_min:
        print('Суммы в столбцах совпадают')
    else:
        print('Столбец с максимальной суммой:')
        for i in range(m):
            print(matrix[i][index_column_max], end=' ')
        print('\nСтолбец с минимальной суммой:')
        for i in range(m):
            print(matrix[i][index_column_min], end=' ')
        print('\nНовая матрица: ')
        # Перестановка столбцов
        for i in range(m):
            value = matrix[i][index_column_min]
            matrix[i][index_column_min] = matrix[i][index_column_max]
            matrix[i][index_column_max] = value
        for i in range(m):
            print(*matrix[i])


def print_matrix(matrix, n, m):
    """
    Процедура для вывода матрицы
    Входные данные: матрица, количество столбцов и строк
    """
    # Проверка того, что матрица не пустая
    if n == 0 or m == 0:
        print('Матрица пустая!')
        return
    # Построчный вывод матрицы
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()


def main():
    """
    Функция для работы с меню программы.
    Параметры отсуствуют.
    Входные данные: необходимая команда пользователя
    Выходные данные: приветсвие, меню программы, сообщение об ошибке, если команда нерентабельна.
    """
    # Приветствие
    print("Здравствуйте!")
    # Строка для меню программы и инструкции для работы с ним
    menu_string = ('Работа с меню ведется через ввод чисел от 0 до 8 включительно в соотвествии с пунктами меню.\n'
                   'Меню:\n'
                   '0 - Вывести меню\n'
                   '1 - Ввести матрицу\n'
                   '2 - Добавить строку\n'
                   '3 - Удалить строку\n'
                   '4 - Добавить столбец\n'
                   '5 - Удалить столбец\n'
                   '6 - Найти строку, имеющую наибольшее количество подряд идущих одинаковых элементов\n'
                   '7 - Переставить местами строки с наибольшим и наименьшим количествомотрицательных элементов\n'
                   '8 - Найти столбец, имеющий наибольшее количество нулевых элементов\n'
                   '9 - Переставить местами столбцы с максимальной и минимальной суммой элементов\n'
                   '10 - Вывести матрицу\n'
                   '11 - Завершить выполнение программы\n')
    # Первый вывод меню программы
    print(menu_string)
    # Матрица
    matrix = []
    # Считает текущее количество столбцов в матрице
    n = 0
    # Считает текущее количество строк в матрице
    m = 0
    # Программа будет работать, пока пользователь не введет 8 команду (там стоит break для цикла)
    while True:
        # Строка ввода команды
        command = input('Введите необходимую команду для работы со списком или 0 для вывода меню: ')
        # Проверка на соотвествие команды пункту меню
        if not command.isdigit() or int(command) > 11:
            print('Команда введена неверно!', end=' ')
            print(menu_string)
            continue
        # Приведение команды к целочисленному типу и выбор пункта меню
        command = int(command)
        if command == 0:
            # Вывод меню в терминал
            print(menu_string)
        elif command == 1:
            # Ввод матрицы
            n, m = matrix_input(matrix, n, m)
        elif command == 2:
            # Добавить строку
            n, m = add_row(matrix, n, m)
        elif command == 3:
            # Удалить строку
            n, m = remove_row(matrix, n, m)
        elif command == 4:
            # Добавить столбец
            n, m = add_column(matrix, n, m)
        elif command == 5:
            # Удалить столбец
            n, m = remove_column(matrix, n, m)
        elif command == 6:
            # Найти строку, имеющую наибольшее количество подряд идущих одинаковых элементов
            find_row(matrix, n, m)
        elif command == 7:
            # Переставить местами строки с наибольшим и наименьшим количествомотрицательных элементов
            change_rows(matrix, n, m)
        elif command == 8:
            # Найти столбец, имеющую наибольшее количество нулевых элементов
            find_column(matrix, n, m)
        elif command == 9:
            # Переставить местами столбцы с максимальной и минимальной суммой элементов
            change_columns(matrix, n, m)
        elif command == 10:
            # Вывести матрицу
            print_matrix(matrix, n, m)
        elif command == 11:
            # Завершить программу
            break


main()
