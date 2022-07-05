# Программа для работы с текстовыми базами данных
# Выходные и выходные данные прописаны в соответствующих функциях

import os


def get_path_for_bases_folder(first_path_init=False):
    """
    Получения пути до директории, где хранятся базы.
    Параметры:
        * first_path_init True/False Параметр отвечает за приглашение ввода в случае некорректного ответа пользователя
    Входные данные: путь пользователя и его ответ,  в случае некорректного пути
    Выходные данные: приглашения ввода, в случае некорректного пути от пользователя
    """
    # Ввод пути пользователем
    path = input('Введите путь до директории, где будет происходить работа с базами: ')
    # Проверка корректности пути
    while not os.path.exists(path) and not os.path.isdir(path):
        if first_path_init:
            user_answer = input('Путь до директории введён некорректно. Повторите ввод? [Д/Н] В случае отказа'
                                'дальнейшая работа программы будет невозможной, программа завершит свою работу: ')
        else:
            user_answer = input('Путь до директории введён некорректно. Повторите ввод? [Д/Н]: ')
        if user_answer == 'Д':
            path = input('Введите путь до директории, где будет происходить работа с базами: ')
        elif user_answer == 'Н':
            return False, None
        else:
            print('Ответ дан некорректно. Повторите ввод.')
    # Возврат пути и True, в случае успешного получения пути
    return True, os.path.abspath(path)


def list_of_bases(path_of_bases_folder, need_to_print=True):
    """
    Функция для вывода списка баз рабочей директории.
    Параметры:
     * path_of_bases_folder - путь рабочей директории
     * need_ro_print - Необходимо ли выводить список файлов или нет
    Входные данные отсутствуют.
    Выходные данные: список баз, если это предусматривается соответствующим параметром
    Возвращает список баз в директории.
    """
    # Получения списка из введенного ранее пути с проверкой на формат и корректность баз
    files = list(filter(lambda x: x[-4:] == '.txt' and check_if_base_can_work(os.path.join(path_of_bases_folder, x))
                        and base_format_check(os.path.join(path_of_bases_folder, x)),
                        os.listdir(path_of_bases_folder)))
    # Если список баз пустой, то возвращает пустой список
    if not files:
        if need_to_print:
            print('Базы недоступны. Инициализируйте новую базу.')
        return []
    # Если список не пустой и need_to_print, то выводится список баз
    if need_to_print:
        print('Доступны следующие базы:')
        for i in range(len(files)):
            print(f'{i+1} -', files[i])
    return files


def choose_file(path_of_bases_folder):
    """
    Процедура для выбора баз данных
    :param path_of_bases_folder:
    :return:
    """
    bases_list = list_of_bases(path_of_bases_folder)
    if not bases_list:
        return None
    number_of_base = input('Введите номер интересующей базы: ')
    while not number_of_base.isdigit() or 0 < int(number_of_base) > len(bases_list):
        user_answer = input('Номер интересующей базы введен некорректно. Хотите ещё раз попробовать? [Д/Н]: ')
        if user_answer == 'Д':
            number_of_base = input('Введите номер интересующей базы: ')
        elif user_answer == 'Н':
            print('Внимание. Работа с предыдущей базой будет прекращена. Вам следует или инициализировтаь новую базу,'
                  'или всё же выбрать другую из списка.')
            return None
        else:
            continue
    return os.path.join(path_of_bases_folder, bases_list[int(number_of_base) - 1])


def init_base(path_of_bases_folder):
    """
    Процедура для создания базы, если её нет в списке
    :param path_of_bases_folder:
    :return:
    """
    # Ввод названия базы
    print('Внимание! Процесс инициализации базы необратим после правильного введения именования файла! '
          'Существующий файл базы с аналогичным именем будет удален!')
    new_base_name = ' '.join(list(filter(lambda x: x, input('Введите название новой базы: ').split())))
    while sum([symbol in new_base_name for symbol in '\/:*?"<>|+%@!']) or new_base_name[-1] == '.':
        user_answer = input('Введённое название несоответствует критериям названий файлов операционной системы. '
                            'Повторите ввод? [Д/Н]: ')
        if user_answer == 'Д':
            new_base_name = ' '.join(list(filter(lambda x: x, input('Введите название новой базы: ').split())))
        elif user_answer == 'Н':
            return
        else:
            print('Вы некорректно ответили на вопрос.')
    # Чистка базы если такая есть
    if os.path.exists(os.path.join(path_of_bases_folder, new_base_name+'.txt')):
        try:
            with open(os.path.join(path_of_bases_folder, new_base_name+'.txt'), 'r') as base:
                base.readline()
        except Exception:
            print('Возникла проблема с работой в папке, выбранной ранее пользователем. Выберете другую папку.')
            return
        os.remove(os.path.join(path_of_bases_folder, new_base_name+'.txt'))
    try:
        with open(os.path.join(path_of_bases_folder, new_base_name+'.txt'), 'w') as file:
            file.write('1')
    except Exception:
        print('Невозможно работать с файлами в данной папке. Смените папку.')
        return
    # Получение списка полей базы
    fields_count = input('Введите количество полей базы: ')
    while not fields_count.isdigit() or fields_count[0] == '0':
        user_answer = input('Количество полей введено некорректно. Повторите ввод? [Д/Н]: ')
        if user_answer == 'Д':
            fields_count = input('Введите количество полей базы: ')
        elif user_answer == 'Н':
            print('Операция прервана.')
            return
        else:
            print('Ответ введён некорректно. Повторите ввод.')
    fields_count = int(fields_count)
    list_of_fields = []
    i = 0
    while i < fields_count:
        new_field = ' '.join(list(filter(lambda x: x, input(f'Введите название {i+1} поля. Внимание: '
                                                            f'полученное название поля будет приведено к '
                                                            f'нижнему регистру, лишние пробелы будут '
                                                            f'удалены: ').split()))).lower()
        while '|' in new_field:
            user_answer = input('Поле базы содержит запрещенный знак "|". Повторите ввод поля? [Д/Н]: ')
            if user_answer == 'Д':
                new_field = ' '.join(list(filter(lambda x: x, input(f'Введите название {i + 1} поля. Внимание: '
                                                                    f'полученное название поля будет приведено к '
                                                                    f'нижнему регистру, лишние пробелы будут '
                                                                    f'удалены: ').split()))).lower()
            elif user_answer == 'Н':
                print('Операция прервана.')
                return
            else:
                print('Ответ введён некорректно.')
        if new_field in list_of_fields:
            while new_field in list_of_fields:
                user_answer = input('Наименование поле уже присутствует в списке. Перенести в конец текущего списка '
                                    'полей/не добавлять полученное поле [В1/В2]: ')
                if user_answer == 'В1':
                    list_of_fields.remove(new_field)
                    list_of_fields.append(new_field)
                    break
                if user_answer == 'В2':
                    i -= 1
                    break
                else:
                    print('Ответ введён некорректно. Повторите ввод.')
        else:
            list_of_fields.append(new_field)
        i += 1
    fields_count = len(list_of_fields)
    # Получение количества записей базы
    lines_count = input('Введите количество записей базы: ')
    while not lines_count.isdigit():
        user_answer = input('Количество записей введено некорректно. Повторите ввод? [Д/Н]: ')
        if user_answer == 'Д':
            lines_count = input('Введите количество записей базы: ')
        elif user_answer == 'Н':
            print('Операция прервана.')
            return
        else:
            print('Ответ введён некорректно. Повторите ввод.')
    lines_count = int(lines_count)
    # Заполнение столбцов
    with open(os.path.join(path_of_bases_folder, new_base_name+'.txt'), 'w') as base:
        base.write('|'.join(list_of_fields)+'\n')
        for i in range(lines_count):
            print(f'~ {i+1} запись ~')
            for j in range(fields_count):
                new_value = input(f'Введите значение {i+1} записи для поля "{list_of_fields[j]}": ')
                while '|' in new_value:
                    user_answer = input('Поле содержит запрещённый символ "|". Повторите ввод? [Д/Н]: ')
                    if user_answer == 'Д':
                        new_value = input(f'Введите значение {i + 1} записи для поля "{list_of_fields[j]}": ')
                    elif user_answer == 'Н':
                        print('Операция прервана Некорректная база будет сохранена с данными, уже полученными на '
                              'данный момент')
                        return
                    else:
                        print('Ответ введён некорректно. Повторите ввод.')
                base.write(new_value+'|')
            base.write('\n')


def check_if_base_can_work(work_base):
    """
    Функция проверки базы на читаемость
    """
    if os.path.exists(work_base):
        try:
            with open(work_base, 'r') as base:
                base.readline()
            return True
        except Exception:
            return False
    else:
        return False


def print_base(work_base):
    """
    Процедура для вывода базы.
    Параметры: выбранная база
    Входные данные отсуствуют
    Выходные данные: форматированная таблица из файла базы
    """
    if not first_checking_before_operation(work_base):
        return
    max_len_line = 0
    headers = None
    with open(work_base, 'r') as base:
        if base.readable():
            headers = base.readline()
            headers = headers[:len(headers)-1].split('|')
            if not headers[-1]:
                headers.pop()
            if not headers:
                print('База пустая. Инициализируйте базу.')
                return
            max_len_line = max(max_len_line, max(*[len(header) for header in headers]))
            for line in base:
                line = line.split('|')
                if not line[-1]:
                    line.pop()
                max_len_line = max(max_len_line, max(*[len(word) for word in line]))
    if headers:
        print('-' * ((max_len_line + 1) * len(headers) + 1))
        print('|', end='')
        for header in headers:
            print(str(' '*((max_len_line-len(header))//2)) + header + str(' '*((max_len_line-len(header))//2)), end='')
            count = 0
            while len(' '*((max_len_line-len(header))//2))*2+len(header)+count < max_len_line:
                print(' ', end='')
                count += 1
            print('|', end='')
        print()
        print('-'*((max_len_line+1)*len(headers)+1))
    with open(work_base, 'r') as base:
        if base.readable():
            base.readline()
            for line in base:
                line = line.split('|')
                print('|', end='')
                for word in line:
                    if word and word != '\n':
                        print(str(' '*((max_len_line-len(word))//2)) + word + str(' '*((max_len_line-len(word))//2)),
                              end='')
                        count = 0
                        while len(' ' * ((max_len_line - len(word)) // 2)) * 2 + len(word) + count < max_len_line:
                            print(' ', end='')
                            count += 1
                        print('|', end='')
                print()
            print('-' * ((max_len_line + 1) * len(headers) + 1))


def base_format_check(work_base):
    """
    Процедура для проверки базы на соотвествие введённому формату базы.
    """
    with open(work_base, 'r') as base:
        if base.readable():
            line = base.readline()
            count_symbol = line.count('|')
            if line and line[-1] == '\n':
                line = line[:len(line)-1]
            if not count_symbol and len(line) or count_symbol < 2:
                return False
            elif not len(line):
                return True
            for line in base:
                if line.count('|') != count_symbol+1:
                    return False
            return True
        else:
            return False


def first_checking_before_operation(work_base):
    if not work_base:
        print('Выберете сначала рабочую базу.')
        return False
    if not check_if_base_can_work(work_base):
        print('Выбранная база недоступна. Выберете другую рабочую базу.')
        return False
    if not base_format_check(work_base):
        print('База некорректна. Инициализируйте базу и повторите ввод.')
        return False
    return True


def add_line_in_base(work_base):
    if not first_checking_before_operation(work_base):
        return
    headers = []
    with open(work_base, 'r') as base:
        if base.readable():
            headers = base.readline()
            headers = headers[:len(headers)-1].split('|')
            if headers and headers[-1] == '\n':
                headers.pop()
            if not headers or not headers[0]:
                print('База пустая. Инициализируйте базу.')
                return
        else:
            print('Базу невозможно прочитать. Попробуйте позже.')
            return
    with open(work_base, 'a') as base:
        for header in headers:
            new_value = input(f'Введите значение для поля "{header}" новой записи: ')
            while '|' in new_value:
                user_answer = input('Поле содержит запрещённый символ "|". Повторите ввод? [Д/Н]: ')
                if user_answer == 'Д':
                    new_value = input(f'Введите значение для поля "{header}" новой записи: ')
                elif user_answer == 'Н':
                    print('Операция прервана Некорректная база будет сохранена с данными, уже полученными на '
                          'данный момент')
                    return
                else:
                    print('Ответ введён некорректно. Повторите ввод.')
            base.write(new_value+'|')
        base.write('\n')


def find_by_field(work_base, double=False):
    if not first_checking_before_operation(work_base):
        return
    # Вывод заголовков пользователю в виде {номер порядка в базе} - {заголовок}
    max_len_line = 0
    headers = []
    with open(work_base, 'r') as base:
        if base.readable():
            headers = base.readline()
            headers = headers[:len(headers) - 1].split('|')
            if not headers[-1]:
                headers.pop()
            if not headers:
                print('База пустая. Инициализируйте базу.')
                return
            max_len_line = max(max_len_line, max(*[len(header) for header in headers]))
            for line in base:
                line = line.split('|')
                if not line[-1]:
                    line.pop()
                max_len_line = max(max_len_line, max(*[len(word) for word in line]))
        else:
            print('Базу невозможно прочитать. Попробуйте позже.')
            return
    if not headers:
        print('База пустая. Инициализируйте её, а затем осуществите фильтр по записям.')
        return
    print('В базе данных содержатся следующие поля: ')
    for i in range(len(headers)):
        print(f'{i+1} - {headers[i]}')
    # Ввод номеров полей и значений, по которым будет происходить фильтр
    number_of_header = input('Введите номер поля, по которому будет происходить фильтр: ')
    while not number_of_header.isdigit() or 0 > int(number_of_header) - 1 or int(number_of_header) - 1 > len(headers):
        user_answer = input('Номер заголовка был введен не корректно. Повторите ввод? [Д/Н]: ')
        if user_answer == 'Д':
            number_of_header = input('Введите номер поля, по которому будет происходить фильтр: ')
        elif user_answer == 'Н':
            print('Операция прервана.')
            return
        else:
            print('Ответ введён некорректно, повторите ввод.')
    first_header_number = int(number_of_header)-1
    first_header_value = input(f'Введите значение для поля "{headers[first_header_number]}" новой записи: ')
    while '|' in first_header_value:
        user_answer = input('Поле содержит запрещённый символ "|". Повторите ввод? [Д/Н]: ')
        if user_answer == 'Д':
            first_header_value = input(f'Введите значение для поля "{headers[first_header_number]}" новой записи: ')
        elif user_answer == 'Н':
            print('Операция прервана Некорректная база будет сохранена с данными, уже полученными на '
                  'данный момент')
            return
        else:
            print('Ответ введён некорректно. Повторите ввод.')
    if double:
        number_of_header = input('Введите второй номер поля, по которому будет происходить фильтр: ')
        while not number_of_header.isdigit() or 0 > int(number_of_header) - 1 or int(number_of_header) - 1 > len(
                headers) or int(number_of_header) == first_header_number:
            user_answer = input('Номер заголовка был введен не корректно. Повторите ввод? [Д/Н]: ')
            if user_answer == 'Д':
                number_of_header = input('Введите второй номер поля, по которому будет происходить фильтр: ')
            elif user_answer == 'Н':
                print('Операция прервана.')
                return
            else:
                print('Ответ введён некорректно, повторите ввод.')
        second_header_number = int(number_of_header) - 1
        second_header_value = input(f'Введите значение для поля "{headers[second_header_number]}" новой записи: ')
        while '|' in first_header_value:
            user_answer = input('Поле содержит запрещённый символ "|". Повторите ввод? [Д/Н]: ')
            if user_answer == 'Д':
                second_header_value = input(f'Введите значение для поля "{headers[second_header_number]}" новой записи: ')
            elif user_answer == 'Н':
                print('Операция прервана Некорректная база будет сохранена с данными, уже полученными на '
                      'данный момент')
                return
            else:
                print('Ответ введён некорректно. Повторите ввод.')
    # Вывод заголовков базы
    print('-' * ((max_len_line + 1) * len(headers) + 1))
    print('|', end='')
    for header in headers:
        print(str(' ' * ((max_len_line - len(header)) // 2)) + header + str(' ' * ((max_len_line - len(header)) // 2)),
              end='')
        count = 0
        while len(' ' * ((max_len_line - len(header)) // 2)) * 2 + len(header) + count < max_len_line:
            print(' ', end='')
            count += 1
        print('|', end='')
    print()
    print('-' * ((max_len_line + 1) * len(headers) + 1))
    # Фильтр и вывод результатов этого фильтра
    with open(work_base, 'r') as base:
        if base.readable():
            base.readline()
            for line in base:
                line = line.split('|')
                if (line[first_header_number] == first_header_value and not double or double
                        and line[first_header_number] == first_header_value
                        and line[second_header_number] == second_header_value):
                    print('|', end='')
                    for word in line:
                        if word and word != '\n':
                            print(str(' '*((max_len_line-len(word))//2)) + word + str(' '*((max_len_line-len(word))//2)),
                                  end='')
                            count = 0
                            while len(' ' * ((max_len_line - len(word)) // 2)) * 2 + len(word) + count < max_len_line:
                                print(' ', end='')
                                count += 1
                            print('|', end='')
                    print()
            print('-' * ((max_len_line + 1) * len(headers) + 1))
        else:
            print('Базу невозможно прочитать. Попробуйте позже.')
            return


def main():
    path_of_bases_folder = os.path.join(os.getcwd(), 'bases')
    menu = (
        '0 - Вывести содержимое меню'
        '1 - Выбрать файл для работы с базой\n'
        '2 - Инициализировать базу данных\n'
        '3 - Вывести содержимое базы данных\n'
        '4 - Добавить запись в базу данных\n'
        '5 - Поиск по одному полю\n'
        '6 - Поиск по двум полям\n'
        '7 - Изменить папку для поиска баз\n'
        '8 - Завершить работу программы\n'
    )
    if not os.path.exists(path_of_bases_folder):
        os.mkdir(path_of_bases_folder)
    work_base = None
    answer, path_of_bases_folder = get_path_for_bases_folder(first_path_init=True)
    if not answer:
        return
    while True:
        user_choose = input('Введите номер пункта меню. Введите 0, чтобы вывести меню: ')
        if not user_choose.isdigit() or -1 < int(user_choose) > 7:
            print('Номер пункта  меню был введён неверно.')
            continue
        if user_choose == '0':
            print(menu)
        elif user_choose == '1':
            work_base = choose_file(path_of_bases_folder)
        elif user_choose == '2':
            init_base(path_of_bases_folder)
        elif user_choose == '3':
            print_base(work_base)
        elif user_choose == '4':
            add_line_in_base(work_base)
        elif user_choose == '5':
            find_by_field(work_base)
        elif user_choose == '6':
            find_by_field(work_base, double=True)
        elif user_choose == '7':
            answer, path_of_bases_folder = get_path_for_bases_folder()
        else:
            break


main()
