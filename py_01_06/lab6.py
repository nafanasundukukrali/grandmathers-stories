# Программу, позволяющая с использованием меню обеспечить работу с числовыми массивами:
# Входные данные прописанны в каждой используемой функции
# Выходные данные прописаны в используемых фукнциях
# Выходные данные прописаны в используемых фукнциях


def initialization_of_a_series():
    """
    Инициализайия списока первыми N элементами заданного в л/р 5 ряда (для варианта 71)
    Параметры: отсуствуют
    Входные данные: начальный аргумент для ряда и количество элементов ряда для списка
    Выходные данные: функция вовращает список, состоящий из элементов ряда. Если количество элементов не целовичленно,
    то возращается сообщение об ошибке. Так же с аргументом функции: если число x не вещественное (или целочисленное)
    было введено, то функция вернет сообщение об ошибке и попросит повторить операцию пункта меню.
    """
    # Начальный аргумент ряда
    x = input('Введите начальный аргумент: ')
    # По условию х - это либо целове число, либо число с плавающей запятой. Проверка ведется через строку через
    # удаление точки и тире  и проверки, что остались одни цифры.
    if not x.replace('-', '', 1).replace('.', '', 1).isdigit():
        # В строке присутствуют прочие символы помимо чисел, одной точки и тире -> формат ввода был неверен
        # Выводится сообщение об ошибке
        print('Введен некорректный аргумент! Повторите операцию, выбрав вновь данный пункт меню.')
        return
    # Вводится количество элементов ряда, которые необходимо найти
    n = input('Введите количество элементов ряда: ')
    # Проверяется, что было введено натуральное число
    if not n.isdigit():
        print('Колличество элементов ряда введено некорректно! Повторите операцию, выбрав вновь данный пункт меню.')
        return
    # Необходимые проверки были пройдены, полученные данные приводятся к численному типу
    x = float(x)
    n = int(n)
    # Пустой список для членов ряда, которые ищутся
    series_elements = []
    # Текущий нечетный n, необходимый для вычисления необходимого факториала и степени текущего члена ряда
    right_uneven_number = 1
    # Последний вычисленный член ряда
    last_member_in_series = x
    # Текущий факториал, небходимый для вычилсения текущего члена ряда
    factorial = 1
    for i in range(n):
        # Прибавление последнего вычисленного члена ряда к сумме
        series_elements.append(round(last_member_in_series, 4))
        for j in range(right_uneven_number + 1, right_uneven_number + 3):
            factorial *= j
        # Вычисляется нужное нечётное число
        right_uneven_number += 2
        # Получается следующий член ряда
        last_member_in_series = x ** right_uneven_number / factorial
    # Возвращается список найденных чисел в ряде
    return series_elements


def remove_list(series_elements, condition):
    """
    Функция для удаления списка.
    Параметры: список и Conditions, принимается значение 1 или 0. В зависимости от значения параметра различаются
    входные и выходные данные
    Входные данные: если conditions равен 0, то вводится пользовательский список, если 1, то других входных данных нет
    Выходные данные: если conditions равен 0, то будет выводится список элементов
    """
    # Проверка параметра condition
    if not condition:
        # Condition равен 0, выводится список
        print('Элементы списка:', end=' ')
        print(*series_elements)
        # Список "чистится"
        series_elements.clear()
        # Добаляются вводимые пользователем элементы
        new_serie = list(input('Введите элементы списка через пробел: ').split())
        new_serie1 = []
        list_of_not_number = []
        for i in range(len(new_serie)):
            if not numeric_type(new_serie[i]):
                list_of_not_number.append(i+1)
            else:
                new_serie1.append(float(new_serie[i]))
        if list_of_not_number:
            while True:
                print('Среди элементов присутствуют элементы не числового типа. '
                      f'Проблемы с элементами возникают на местах', *list_of_not_number)
                answer = input('Выполнить повторный ввод данных позиций? [Д/Н]: ')
                if answer == 'Д':
                    break
                if answer == 'Н':
                    while True:
                        answer1 = input('Удалённый список не будет восстановлен. Вы хотите продолжить? [Д/Н]: ')
                        if answer1 == 'Д':
                            return
                        if answer1 == 'Н':
                            break
                        else:
                            print('Ответ был дан некорректно. Повторите ввод ответа на вопрос.')
                else:
                    print('Ответ был дан некорректно. Повторите ввод ответа на вопрос.')
        series_elements.extend(new_serie1)
        for i in list_of_not_number:
            print(f'Введите {i} элемент списка: ', end='')
            new_element = input()
            while not numeric_type(new_element):
                answer = input('Был введен элемент не числового типа. '
                               'Повторить ввод/прекратить ввод чисел и продолжить работу с уже полученным правильным '
                               'списком [Д/Н]: ')
                if answer == 'Д':
                    new_element = input(f'Введите {i} элемент списка: ')
                elif answer == 'Н':
                    return
                else:
                    print('Ответ был дан некорректно. Повторите ввод ответа на вопрос.')
                    continue
            series_elements.insert(i-1, float(new_element))
    else:
        # Condition равен 0, чистится список
        series_elements.clear()


def add_element(series_elements):
    """
    Добавление элемента в список
    Параметр: список
    Входные данные: вводится элемент списка и позиция, на которую необходимо добавить элемент
    Выходные данные: если позиция не рентабельна в рамках данного списка, то выводится сообщение об ошибке. В противном
    случае добавляется элемент на необходимую позицию.
    """
    # Вводится элемент, который необходимо добавить
    element = input('Введите элемент списка: ')
    while not numeric_type(element):
        answer = input('Был введен элемент не числового типа. '
                       'Повторить ввод/прервать операцию [Д/Н]: ')
        if answer == 'Д':
            element = input(f'Введите элемент списка: ')
        elif answer == 'Н':
            return
        else:
            print('Ответ был дан некорректно. Повторите ввод ответа на вопрос.')
    while not numeric_type(element):
        while True:
            user_answer = input('Введеный элемент не является элементом числового типа. '
                                'Повторить ввод? [Д/Н]: ')
            if user_answer == 'Д':
                element = input('Введите элемент списка: ')
                break
            elif user_answer == 'Н':
                return
            else:
                print('Ответ введен некорректно. Повторите ввод. ')
                continue
    # Вводится позиция, на которую необходимо добавить элемент
    position = input(f'В списке {len(series_elements)} элементов. Первому элементу соотвествует первая позиция в списке'
                     f'. Введите позицию, куда следует добавить элемент в списке: ')
    # Проверка кооректности позиции (сначала, что это целое число, а затем, что модуль не больше длины списка)
    if not position.replace('-', '', 1).isdigit() or abs(int(position))-1 > len(series_elements):
        print('Введенная позиция некорректна, повторите операцию.')
        return
    # Приведение позиции к целочисленному типу
    position = int(position) - 1
    # Уведомление пользователя, что было введено число меньше 0
    if int(position) < 0:
        # Подтверждение пользователем, что было действительно введено отрицательное число
        while True:
            user_answer = input('Введена позиция меньше 0, элемент будет добавлен на позицию, считая с конца. '
                                'Продолжить? [Д/Н]: ')
            if user_answer == 'Д' or user_answer == 'Н':
                break
            else:
                continue
        if user_answer == 'Н':
            print('Выполение операции прервано.')
            return
    # Вставка элемента
    series_elements.insert(position, float(element))


def remove_element(series_elements):
    """
    Функция для удаления элемента из списка.
    Параметр: элемент списка
    Входные данные: позиция, с которой необходимо удалить элемент
    Выходные данные: в случае некорректности позиции выводится сообщение об ошибке. В случае, если позиция меньше 0,
    пользователя уведомляют о том, что была введена позиция меньше 0.
    """
    # Вводится позиция, на которую необходимо добавить элемент
    position = input(f'В списке {len(series_elements)} элементов. Первому элементу соотвествует первая позиция в списке'
                     ' ВНИМАНИЕ! Числа экспоненциального вида не читаются за целочисленные'
                     f'. Введите позицию, куда следует добавить элемент в списке: ')
    # Проверка кооректности позиции (сначала, что это целое число, а затем, что модуль не больше длины списка)
    # integer_type считает числа
    if not integer_type(position) and '.' not in position and abs(int(position)) - 1 >= len(series_elements):
        print('Введенная позиция некорректна, повторите операцию.')
        return
    # Приведение позиции к целочисленному типу
    position = int(position) - 1
    # Уведомление пользователя, что было введено число меньше 0
    if int(position) < 0:
        # Подтверждение пользователем, что было действительно введено отрицательное число
        while True:
            user_answer = input('Введена позиция меньше 0, элемент будет добавлен на позицию, считая с конца. '
                                'Продолжить? [Д/Н]: ')
            if user_answer == 'Д' or user_answer == 'Н':
                break
            else:
                continue
        if user_answer == 'Н':
            print('Выполение операции прервано.')
            return
    # Удаление элемента
    series_elements.pop(position)


def find_k_extreme(series_elements):
    """
    Находение K-го экстремума среди значений списка.
    Входные данные: список, в котором необходимо найти экстремум
    Выходные данные: в случае, если список пуст, то выводится сообщение об ошибке; в случае, если в списке содержится
    не числовой элемент, то выводится сообщение об ошибке; в случае, если в списке все элементы являются числами, то
    ищется к-й экстремум, а его нет, то выводится сообщение об ошибке, в противном случае выводится экстремум.
    """
    # Проверка того, что список не пустой
    if not series_elements:
        print('Список ещё пустой!')
        return
    # Вводится номер экстремума
    k = input('Введите номер экстремума. Внимание! Ввод числа экспоненциального вида будет оценен некорректно: ')
    # Провека на то, что число положитено.
    if 'e' in k or 'E' in k or not positive_integer(k):
        print('Номер экстремума введен некорректно! Повторите операцию, выбрав вновь данный пункт меню.')
        return
    # Перевод числа к целочисленному типу
    k = int(k)
    # Количество найденных экстремумов
    extreme_count = 0
    # Текущий экстремум
    extreme = None
    # Поиск экстремумов
    for i in range(1, len(series_elements)-1):
        if (series_elements[i - 1] > series_elements[i] < series_elements[i + 1] or
                series_elements[i - 1] < series_elements[i] > series_elements[i + 1]):
            extreme_count += 1
            extreme = series_elements[i]
        if extreme_count == k:
            break
    # Сравнение количества экстремумов с тем, которое было введено
    if extreme_count == k:
        print(extreme)
    else:
        print('Данное количество экстремумов отсуствует в списке.')


def check_prime(number):
    """
    Проверка числа на то, что оно простое
    Параметр: вводится целочисленное число в формате float
    """
    # Берется модуль числа
    number = abs(number)
    # Начинаем проверять начин
    divider = 2
    # Параметр для подсчёта колчиества делителей
    divider_counter = 0
    # Проверка отсуствия натуральных делителей помимо 1 и самого числа
    while divider ** 2 < number:
        if number % divider == 0:
            divider_counter += 1
            break
        else:
            divider += 1
    # Возврат результата проверки
    if number == 2:
        return True
    elif number == 1:
        return False
    elif not divider_counter:
        return True
    else:
        return False


def subsequence(series_elements):
    # Проверка на то, что список не пустой
    if not series_elements:
        print('Список ещё пустой!')
        return
    # Максимальная подпоследовательность вообще в списке
    max_subsequence = []
    # Последняя найденная последовательность чисел
    local_subsequence = []
    # Поиск необходимой подпоследовательности
    last_elem = 0
    for element in series_elements:
        if integer_type(str(element)) and element < 0 and check_prime(element) and element < last_elem:
            local_subsequence.append(element)
            last_elem = element
        else:
            if len(max_subsequence) < len(local_subsequence):
                max_subsequence = local_subsequence
            local_subsequence = []
            last_elem = 0
    if len(max_subsequence) < len(local_subsequence):
        max_subsequence = local_subsequence
    # Вывод подпоследовательности, если такая вообще была
    if max_subsequence:
        print(*max_subsequence)
    else:
        print('Подпоследовательность отсуствует в ряде!')


def numeric_type(number):
    """
    Проверка строки на то, что в ней записано число.
    Параметр: строка number, в которой хранится предполагаемое число
    Выходные данные: True False
    """
    # Убираем минус в начале -
    if number[0] == '-':
        number = number[1:]
    # Проверяем число на экспоненциальный формат (убираем e и e-, если они не стоят в начале и конце)
    if ('e' in number or 'E' in number) and number[0] != 'e' and number[0] != 'E' and number[-1] != '-':
        if 'e-' in number:
            number = number.replace('e-', '', 1)
        else:
            number = number.replace('e', '', 1)
        if 'E-' in number:
            number = number.replace('E-', '', 1)
        else:
            number = number.replace('E', '', 1)
    # Убираем точку
    if '.' in number and number[0] != '.' and number[-1] != '.':
        number = number.replace('.', '', 1)
    # Проверяем, что остались одни цифры
    return number.isdigit()


def positive_integer(x):
    """
    Проверка числа на то, что оно целове и больше 0
    Параметр: строчка с символами
    """
    # Проверка на то, что число целое
    if not integer_type(x):
        return
    # Проверка на то, что число больше 0
    return float(x) > 0


def integer_type(x):
    """
    Проверка строки на то, что в ней записано целочисленное число. За целочисленные числа будем считать
    строки из серии -1.123e10, 1e, -1.0, 1
    Параметр: строка х, проверка которой ведется
    """
    # Уюирается -, если он есть
    if x[0] == '-':
        x = x[1:len(x)]
    # Проверка на то, что было введено вообще число
    if not numeric_type(x):
        return False
    # Если точки нет и e нет, то в любом случае нам число подходит
    if '.' not in x and 'e' not in x and 'E' not in x:
        return True
    else:
        # Если e-, то в любои случае возращается False
        if 'e-' in x or 'E-' in x:
            return False
        # Если e и при этом есть точка, то необходимо, что число после e было больше числа разрядов после точки
        if '+' in x:
            x.replace('+', '')
        if ('e' in x or 'E' in x) and '.' in x:
            if 'E' in x:
                after_e = int(x.split('E')[1])
                after_dot = x.split('E')[0].split('.')[1]
            else:
                after_e = int(x.split('e')[1])
                after_dot = x.split('e')[0].split('.')[1]
            return len(after_dot) <= after_e
        else:
            # Есть просто точка, поэтому два варинта: 1.000 или 1.2. Проверяем на наличие других символов в строке после
            # точки
            after_dot = x.split('.')[1]
            there_not_zero = False
            for symbol in after_dot:
                if symbol != '0':
                    there_not_zero = True
                    break
            return not there_not_zero


def print_list(series_elements):
    """
    Вывод текущих элементов списка.
    Парметры: список, элементы которого необходмого вывести
    Входные данные отсуствуют
    Выходные данные: элементы списка или сообщение, что списко пуст
    """
    if not series_elements:
        print('Элементы в списке отсуствуют!')
        return
    for element in series_elements:
        print('{:.7f}'.format(element), end=' ')
    print()


def menu():
    """
    Функция для работы с меню программы.
    Параметры отсуствуют.
    Входные данные: необходимая команда пользователя
    Выходные данные: приветсвие, меню программы, сообщение об ошибке, если команда не рентабельна.
    """
    # Приветствие
    print("Здравствуйте!")
    # Строка для меню программы и инструкции для работы с ним
    menu_string = ('Работа с меню ведется через ввод чисел от 0 до 8 включительно в соотвествии с пунктами меню.\n'
                   'Меню:\n'
                   '0 - Вывести меню\n'
                   '1 - Проинициализировать список первыми N элементами заданного в л/р 5 ряд (вариант 71)\n'
                   '2 - Очистить список и ввести его с клавиатуры\n'
                   '3 - Добавить элемент в произвольное место списка\n'
                   '4 - Удалить произвольный элемент из списка (по номеру)\n'
                   '5 - Очистить список\n'
                   '6 - Найти значение K-го экстремума в списке\n'
                   '7 - Найти наиболее длинную убывающую последовательность отрицательных чисел, '
                   'модуль которых является простым числом\n'
                   '8 - Вывод текущих элементов списка\n'
                   '9 - Завершить работу программы\n')
    # Первый вывод меню программы
    print(menu_string)
    # Список для работы
    series_elements = []
    # Программа будет работать, пока пользователь не введет 8 команду (там стоит break для цикла)
    while True:
        # Строка ввода команды
        command = input('Введите необходимую команду для работы со списком или 0 для вывода меню: ')
        # Проверка на соотвествие команды пункту меню
        if not command.isdigit() or int(command) > 8:
            print('Команда введена неверно!', end=' ')
            print(menu_string)
            continue
        # Приведение команды к целочисленному типу и выбор пункта меню
        command = int(command)
        if command == 0:
            # Вывод меню в терминал
            print(menu_string)
        elif command == 1:
            # Инициализация списока первыми N элементами заданного в л/р 5 ряд (вариант 71)
            series_elements = initialization_of_a_series()
        elif command == 2:
            # Очистка списока и ввод его с клавиатуры
            remove_list(series_elements, 0)
        elif command == 3:
            # Добавить элемент в произвольное место списка
            add_element(series_elements)
        elif command == 4:
            # Удалить произвольный элемент из списка (по номеру)
            remove_element(series_elements)
        elif command == 5:
            # Очистить список
            remove_list(series_elements, 1)
        elif command == 6:
            # Найти значение K-го экстремума в списке
            find_k_extreme(series_elements)
        elif command == 7:
            # Найти наиболее длинную последовательность по варианту (у меня вариант 9)
            subsequence(series_elements)
        elif command == 8:
            # Вывод элементов списка
            print_list(series_elements)
        elif command == 9:
            # Завершение работы программы
            break


menu()





















