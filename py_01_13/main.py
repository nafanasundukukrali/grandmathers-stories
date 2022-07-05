# Программа для работы с текстовыми базами данных
# Выходные и выходные данные прописаны в соответствующих функциях

import os
import struct


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
    files = list(filter(lambda x: check_if_base_can_work(os.path.join(path_of_bases_folder, x))
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
    if os.path.exists(os.path.join(path_of_bases_folder, new_base_name)):
        try:
            with open(os.path.join(path_of_bases_folder, new_base_name), 'rb') as base:
                base.readline()
        except Exception:
            print('Возникла проблема с работой в папке, выбранной ранее пользователем. Выберете другую папку.')
            return
        os.remove(os.path.join(path_of_bases_folder, new_base_name))
    try:
        with open(os.path.join(path_of_bases_folder, new_base_name), 'wb') as file:
            file.write('1'.encode('utf-8', 'ignore'))
    except Exception:
        print('Невозможно работать с файлами в данной папке. Смените папку.')
        return
    # Получение списка полей базы
    # Формат базы подразумевает под собой 3 поля для базы
    i = 0
    list_of_fields = []
    while i < 3:
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
    fields_count = 3
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
    with open(os.path.join(path_of_bases_folder, new_base_name), 'wb') as base:
        for header in list_of_fields:
            base.write(struct.pack('20s', bytes(header, 'utf-8'))+struct.pack('20s', bytes('|', 'utf-8')))
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
                base.write(struct.pack('20s', bytes(new_value, 'utf-8'))+struct.pack('20s', bytes('|', 'utf-8')))


def check_if_base_can_work(work_base):
    """
    Функция проверки базы на читаемость
    """
    if os.path.exists(work_base):
        try:
            with open(work_base, 'rb') as base:
                base.seek(0)
                base.read(20).decode('utf-8')
            return True
        except Exception as EX:
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
    headers = []
    with open(work_base, 'rb') as base:
        lines_number = os.path.getsize(work_base)//120
        headers_number = 3
        for i in range(headers_number):
            try:
                new_header = base.read(20).decode('utf-8', 'ignore').replace('\x00', '')
                if not new_header:
                    print('База пустая. Инициализируйте базу.')
                    return
                else:
                    headers.append(new_header)
                base.read(20).decode('utf-8', 'ignore').replace('\x00', '')
            except Exception:
                print('База пустая. Инициализируйте базу.')
                return
        max_len_line = max(max_len_line, max(*[len(header) for header in headers]))
        k = headers_number
        while k < 3*(lines_number):
            base.seek(k*40)
            field = base.read(20).decode('utf-8', 'ignore').replace('\x00', '')
            max_len_line = max(max_len_line, len(field))
            base.read(20).decode('utf-8', 'ignore').replace('\x00', '')
            k += 1
    if headers:
        print('-' * ((max_len_line + 1) * 3 + 1))
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
    with open(work_base, 'rb') as base:
        base.read(120)
        k = 120
        for i in range(lines_number-1):
            print('|', end='')
            for j in range(3):
                base.seek(k)
                word = base.read(20).decode('utf-8', 'ignore').replace('\x00', '')
                print(str(' '*((max_len_line-len(word))//2)) + word + str(' '*((max_len_line-len(word))//2)),
                      end='')
                count = 0
                while len(' ' * ((max_len_line - len(word)) // 2)) * 2 + len(word) + count < max_len_line:
                    print(' ', end='')
                    count += 1
                print('|', end='')
                k += 40
            print()
        print('-' * ((max_len_line + 1) * 3 + 1))


def base_format_check(work_base):
    """
    Процедура для проверки базы на соотвествие введённому формату базы.
    """
    with open(work_base, 'rb') as base:
        # Корректный формат базы:
        #   * в каждой записи по 3 поля. Каждое поле отделено знаками '|' также закодированными в 20 байт. Таким образом
        #     на одну запись приходится 120 байт
        #   * в базе обязана содержаться хотя бы одна запись, иначе она считается некорректной
        if os.path.getsize(work_base) % 120 != 0 or os.path.getsize(work_base) == 0:
            return False
        first_number = os.path.getsize(work_base)//120
        second_number = 3
        k = 0
        while True:
            if k == second_number*first_number:
                break
            base.seek(40*k)
            a = base.read(40).decode('utf-8', 'ignore').replace('\x00', '')
            if not a:
                return False
            k += 1
        while True:
            try:
                base.seek(40 * (k+1))
                if not base.read(40).decode('utf-8', 'ignore').replace('\x00', ''):
                    return True
                else:
                    return False
            except Exception:
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
    """
    Процедура для добавления записи в базу
    Параметры:
        * work_base - текущая рабочая база
    Входные данные: соотвествующие значения полей новой записи
    Выходные данные: сообщение об ошибке и приглашения ввода
    """
    # Проверка корректности текущей рабочей базы
    if not first_checking_before_operation(work_base):
        return
    # Получение заголовков базы
    headers = []
    with open(work_base, 'rb') as base:
        for i in range(3):
            base.seek(i*40)
            headers.append(base.read(20).decode('utf-8', 'ignore').replace('\x00', ''))
    # "дописывание" новой записи в базу
    with open(work_base, 'r+b') as base:
        base.seek(os.path.getsize(work_base))
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
            base.write(struct.pack('20s', bytes(new_value, 'utf-8'))+struct.pack('20s', bytes('|', 'utf-8')))


def find_by_field(work_base, double=False):
    if not first_checking_before_operation(work_base):
        return
    # Вывод заголовков пользователю в виде {номер порядка в базе} - {заголовок}
    max_len_line = 0
    headers = []
    with open(work_base, 'rb') as base:
        lines_number = os.path.getsize(work_base)//120
        headers_number = 3
        for i in range(headers_number):
            try:
                new_header = base.read(20).decode('utf-8', 'ignore').replace('\x00', '')
                if not new_header:
                    print('База пустая. Инициализируйте базу.')
                    return
                else:
                    headers.append(new_header)
                    base.read(20).decode('utf-8', 'ignore').replace('\x00', '')
            except Exception:
                print('База пустая. Инициализируйте базу.')
                return
        max_len_line = max(max_len_line, max(*[len(header) for header in headers]))
        k = 3
        while k < headers_number * lines_number:
            base.seek(k * 40)
            field = base.read(20).decode('utf-8', 'ignore').replace('\x00', '')
            max_len_line = max(max_len_line, len(field))
            k += 1
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
                headers) or int(number_of_header)-1 == first_header_number:
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
    with open(work_base, 'rb') as base:
            k = 120
            for i in range(lines_number-1):
                line = []
                for j in range(3):
                    base.seek(k)
                    line.append(base.read(20).decode('utf-8', 'ignore').replace('\x00', ''))
                    k += 40
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


def delete_by_id(work_base):
    """
    Процедура, предназначенная для удаления одной записи из базы
    Параметры: рабочая база
    Входные данные: номер записи, которую надо удалить (и ответы на вопросы пользователю в случае некорректного номера)
    Выходные данные: сообщения об ошибках
    """
    # Проверка базы на корректность
    if not first_checking_before_operation(work_base):
        return
    # Количество строк и столбцов в базе
    first_number = os.path.getsize(work_base)//120-1
    second_number = 3
    # Вывод сообщение об ошибке, если база пустая
    if first_number == 0:
        print('База пустая, удалить ничего не получится (')
        return
    # Ввод номера записи, которую пользователь хочет удалить (и проверка, соответственно)
    line_id = input(f'В базе содержится {first_number} записей. Введите номер записи в базе (от 1 до {first_number}), '
                    f'которую хотите удалить: ')
    while not line_id.isdigit() or int(line_id) > first_number or int(line_id) < 1:
        user_answer = input('Номер записи введён некорректно. Хотите ввести его повторно? [Д/Н]: ')
        if user_answer == 'Д':
            line_id = input(
                f'В базе содержится {first_number} записей. Введите номер записи в базе (от 1 до {first_number}), '
                f'которую хотите удалить: ')
        elif user_answer == 'Н':
            print('Операция прервана.')
            return
        else:
            print('Ответ введён некорректно, повторите ввод.')
    line_id = int(line_id)
    # Перепись содержимого базы в новую без нужной строчки
    with open(work_base, 'r+b') as base1:
        k = line_id*120
        for i in range(line_id, first_number):
            base1.seek(k+120)
            data = base1.read(120)
            base1.seek(k)
            base1.write(data)
            k += 120
        base1.truncate(k)


def main():
    path_of_bases_folder = os.path.join(os.getcwd(), 'bases')
    menu = (
        '0 - Вывести содержимое меню\n'
        '1 - Выбрать файл для работы с базой\n'
        '2 - Инициализировать базу данных\n'
        '3 - Вывести содержимое базы данных\n'
        '4 - Добавить запись в базу данных\n'
        '5 - Поиск по одному полю\n'
        '6 - Поиск по двум полям\n'
        '7 - Изменить папку для поиска баз\n'
        '8 - Удаление записи в базе по её номеру в файле\n'
        '9 - Завершить работу программы\n'
    )
    if not os.path.exists(path_of_bases_folder):
        os.mkdir(path_of_bases_folder)
    work_base = None
    answer, path_of_bases_folder = get_path_for_bases_folder(first_path_init=True)
    if not answer:
        return
    while True:
        user_choose = input('Введите номер пункта меню. Введите 0, чтобы вывести меню: ')
        if not user_choose.isdigit() or -1 < int(user_choose) > 9:
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
        elif user_choose == '8':
            delete_by_id(work_base)
        else:
            break


main()
