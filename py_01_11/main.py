# Программа для работы с текстом, введнным пользователем в коде
# Входные и выходные данные прописаны в соотвествующих функциях

# Текст пользователя
text = [
    'ъуъ.',
    "Вот это я тебе, взамен могильных роз, "
    "Взамен кадильного куренья; ",
    "Ты так сурово жил и до конца донес "
    "Великолепное",
    "И в душных стенах",
    "задыхался. И гостью страшную ты сам к себе впустил ",
    "И с ней наедине ",
    "остался. И нет тебя, и все вокруг 1/5/6/7/(-100)*7*20505060/10000молчит "
    "О скорбной и высокой жизни, "
    "жаворонок Лишь голос мой, как флейта, 50*0 50/0прозвучит",
    "И на твоей безмолвной 500",
    "100й, — (-)1/044 -100/200 жаворонок1/4",
    "Придется поминать того, кто, полный сил, "
    "Как будто бы вчера со мною говорил, "
    "Скрывая дрожь смертельной "
    "боли."
]


def left_corner():
    """
    Функция для выравнивания текста по левому краю
    Параметры отсуствуют
    Входные данные отсуствуют
    Выходные данные отсуствуют
    Возвращает новое положение текста
    """
    # Посимбольное удаление пробелов с правого и левого конца текста каждой строчки
    for i in range(len(text)):
        while text[i][0] == ' ':
            text[i] = text[i][1:]
        while text[i][-1] == ' ':
            text[i] = text[i][:len(text[i])-1]
        flag = False
        j = 0
        while j < len(text[i]):
            if text[i][j] == ' ' and not flag:
                flag = True
                j += 1
            elif text[i][j] == ' ':
                text[i] = text[i][:j]+text[i][j+1:len(text[i])]
            else:
                flag = False
                j += 1
    return 'LEFT'


def right_corner():
    """
    Функция для выравнивания текста по правому краю.
    Параметры отсуствуют.
    Входные данные отствуют.
    Выходные данные отсуствуют.
    Возвращает новое положение текста
    """
    # Отчищаем текст от пробелов на концах строк
    left_corner()
    # Длина максимальной строки
    max_len = max([len(text[i]) for i in range(len(text))])
    # Посимвольное
    for i in range(len(text)):
        while len(text[i]) < max_len:
            text[i] = ' '+text[i]
    return 'RIGHT'


def center_corner():
    """
    Выравниевани текста по центру
    Параметры отсутвуют
    Выходные данные отствуют
    Входные даннные отствуют
    Возвращает новое положение текста
    """
    # Выравнивание по левому краю
    left_corner()
    # Максимальная длина строки
    max_len = max([len(text[i]) for i in range(len(text))])
    # Посимвольное увеличение строк засчёт приавления пробелов слева и справа
    for i in range(len(text)):
        spaces_count = len(text[i].split())-1
        if not spaces_count:
            continue
        else:
            index = 0
            added_count = 2
            while len(text[i]) < max_len:
                if text[i][index] == ' ':
                    count = 0
                    id_1 = index
                    while text[i][id_1] == ' ':
                        count += 1
                        id_1 += 1
                    text[i] = text[i][:index]+' '*added_count+text[i][index+count:]
                if index + added_count >= len(text[i]):
                    added_count += 1
                    index = 0
                else:
                    index += added_count
            if len(text[i]) > max_len:
                j = 0
                flag = False
                while j < len(text[i]) and len(text[i]) > max_len:
                    if text[i][j] == ' ' and not flag:
                        flag = True
                        j += 1
                    elif text[i][j] == ' ':
                        text[i] = text[i][:j] + text[i][j + 1:len(text[i])]
                    else:
                        flag = False
                        j += 1
    return 'CENTER'


def delete_word(word: str, actual_align):
    """
    Процедура, предназначеная для удаления слова из текста
    Параметры:
     * word - слово, которое нужно удалить
     * actual_align  текущее положение текста
    Входные данные отствуют
    Выходные данные отствуют
    """
    # Замена слова на путое
    change_word(word, '', actual_align)


def change_word(word: str, new_word: str, actual_align):
    """
    Процедура для замены слова
    Параметры:
        * word - слово, которое надо заменить
        * new_word - слово, которым заменяем
        * actual_align - текущее положение текста на странице
    Входные данные отствуют
    Выходные данные отствуют
    """
    # Выравнивание по левому краю
    left_corner()
    # Построчная замена слова на новое в зависимости от его положения касательно знаков пунктуальности и начала/конца
    for i in range(len(text)):
        if text[i]:
            text[i] = text[i].replace(f' {word} ', f' {new_word} ')
            text[i] = text[i].replace(f' {word};', f' {new_word};')
            text[i] = text[i].replace(f' {word},', f' {new_word},')
            text[i] = text[i].replace(f' {word}.', f' {new_word}.')
            text[i] = text[i].replace(f':{word},', f' {new_word}:')
            text[i] = text[i].replace(f': {word},', f' {new_word}: ')
            if len(text[i]) >= len(word)+1 and text[i][len(text[i])-len(word)-1:] == ' '+word:
                text[i] = text[i][:len(text[i])-len(word)] + new_word
            first_elem = text[i].split(' ')[0]
            if first_elem == word or first_elem == f'{word}.' or first_elem == f'{word};' or first_elem == f'{word},' or \
                    first_elem == f'{word}:':
                text[i] = new_word + text[i][len(word):]
    # Выравние полученного текста
    if actual_align == 'RIGHT':
        right_corner()
    if actual_align == 'CENTER':
        center_corner()


def find_word_in_sentence():
    """
    Процедура для поиска самых частоиспользуемых слов в предложении
    Параметры отствуют
    Входные данные отствуют
    Выходные данные: строки формата {номер предложения} - {самое часто используемое слово}
    """
    # Текущий номер предложения
    actual_sentence_number = 1
    # Словарь для слов в предложениях
    sentence_word_dict = dict()
    for i in range(len(text)):
        sentence_in_line = text[i].split('. ')
        index = 1
        for sentence in sentence_in_line:
            default_sentence = sentence
            sentence = sentence.replace(',', ' ').replace(';', ' ').replace(':', ' ').replace('-', ' ').replace('. ', ' ')
            if sentence[-1] == '.':
                sentence = sentence[:len(sentence)-1]
            for word in sentence.split():
                if not word:
                    continue
                word = word.lower()
                if word not in sentence_word_dict.keys():
                    sentence_word_dict[word] = 1
                else:
                    sentence_word_dict[word] += 1
            if len(sentence) != len(text[i]) and index != len(sentence_in_line) or \
                    default_sentence and default_sentence[-1] == '.':
                max_word = None
                max_used = 0
                for key, value in sentence_word_dict.items():
                    if value > max_used:
                        max_word = key
                        max_used = value
                print(f'{actual_sentence_number} - {max_word}')
                actual_sentence_number += 1
                sentence_word_dict.clear()
            index += 1


def solve_example(actual_align):
    """
    Процедура для решения примеров с умножением/делением в тексте
    Входные данные отствуют
    параметры отствуют
    Выходные данные отствут
    """
    for i in range(len(text)):
        example = ''
        index = 0
        while ('/' in text[i] or '*' in text[i]) and index < len(text[i]):
            added = False
            if text[i][index] in '*/)' and example and example != '-' or text[i][index] in '0123456789':
                example += text[i][index]
                added = True
            elif text[i][index] == '-' and not example:
                example += '-'
            elif example and index < len(text[i])-2 and text[i][index]+text[i][index+1] == '(-':
                example += '(-'
                index += 2
                continue
            elif len(example) == 1 or '*' not in example and '/' not in example:
                example = ''
            if (len(example) > 1 and not added) or (index+1 == len(text[i]) and example):
                while example[-1] in '*/()-':
                    index -= 1
                    example = example[:len(example)-1]
                example1 = example
                minuses = example.count('-')
                example = example.replace('-', '')
                example = example.replace('(', '')
                example = example.replace(')', '')
                index -= len(example)
                first_number = ''
                second_number = ''
                operation = ''
                error = False
                for symbol in example:
                    if not operation and not second_number and symbol in '0123456789' and type(first_number) == str:
                        first_number += symbol
                    elif symbol in '0123456789':
                        second_number += symbol
                    elif symbol in '*/' and not operation:
                        operation = symbol
                    else:
                        if type(first_number) == str:
                            first_number = float(first_number)
                        if operation == '*':
                            if len(second_number) > 1 and second_number[0] == '0':
                                error = True
                                break
                            first_number *= float(second_number)
                        elif operation == '/':
                            if second_number[0] == '0':
                                error = True
                                break
                            first_number /= float(second_number)
                        operation = symbol
                        second_number = ''
                if error:
                    index += 4
                    text[i] = text[i].replace(example1, 'None', 1)
                else:
                    if type(first_number) == str:
                        first_number = float(first_number)
                    if operation == '*':
                        if len(second_number) > 1 and second_number[0] == '0':
                            error = True
                        else:
                            first_number *= float(second_number)
                    elif operation == '/':
                        if second_number[0] == '0':
                            error = True
                        else:
                            first_number /= float(second_number)
                    if error:
                        index += 4
                        text[i] = text[i].replace(example1, 'None', 1)
                    else:
                        first_number = '{:.7f}'.format(first_number*(-1) if minuses % 2 != 0 else first_number)
                        index += len(first_number)
                        text[i] = text[i].replace(example1, first_number, 1)
                example = ''
            index += 1
    if actual_align == 'RIGHT':
        right_corner()
    elif actual_align == 'CENTER':
        center_corner()


def main():
    actual_align = 'LEFT'
    menu = (
        "0 - Вывести меню\n"
        "1 - Выровнять текст по левому краю\n"
        "2 - Выровнять текст по правому краю\n"
        "3 - Выровнять текст по ширине\n"
        "4 - Удаление всех вхожденийзаданного слова\n"
        "5 - Замена одного слова другим во всём тексте\n"
        "6 - Вычисление арифметического выражения внутри текста (умножение и деление)\n"
        "7 - Найти наиболее часто встречающееся слово в каждом предложении\n"
        "8 - Вывести текст\n"
        "9 - Завершить выполнение программы\n"
    )
    while True:
        user_answer = input('Введите номер команды. Введите 0, чтобы ознакомиться с меню: ')
        if (not user_answer.isdigit()) or int(user_answer) > 9:
            print('Номер команды введён некорректно.')
            continue
        user_answer = int(user_answer)
        if not user_answer:
            print(menu)
        elif user_answer == 1:
            actual_align = left_corner()
        elif user_answer == 2:
            actual_align = right_corner()
        elif user_answer == 3:
            actual_align = center_corner()
        elif not text and 8 > user_answer > 4:
            print('Пустой текст, команда невыполнима.')
        elif user_answer == 4:
            word = input('Введите слово. Примечание: функция регистрозависимая: ')
            delete_word(word, actual_align)
        elif user_answer == 5:
            word = input('Введите слово, которое хотите заменить. Примечание: функция регистрозависимая: ')
            word_new = input('Введите слово, на которое хотите заменить текущее. '
                             'Примечание: функция регистрозависимая: ')
            change_word(word, word_new, actual_align)
        elif user_answer == 6:
            solve_example(actual_align)
        elif user_answer == 7:
            find_word_in_sentence()
        elif user_answer == 8:
            print(*text, sep='\n')
        elif user_answer == 9:
            return


main()
