def numeric_type(number):
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
