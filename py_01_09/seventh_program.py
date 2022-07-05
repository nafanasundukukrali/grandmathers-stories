# Программа для замены в матрице гласных английских букв на точки.
# Входные данные прописаны в используемых фукнциях
# Выходные данные прописаны в используемых фукнциях

from default_matrix_funtions import rectangle_matrix_input, default_matrix_print


def seventh_program():
    """
    Процедура для замены в матрице гласных английских букв на точки.
    Параметры отсуствуют.
    Входные данные отсуствуют.
    Выходные данные отсуствуют.
    """
    # Ввод матрицы
    print('Ввод символьной матрицы:')
    matrix = rectangle_matrix_input(float_type=False, char_type=True)
    # Массив, содержащий в себе главные английские буквы
    search_symbols = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    # Замена главных на точки
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in search_symbols:
                matrix[i][j] = '.'
    # Вывод матрицы
    print('Новая матрица:')
    default_matrix_print(matrix, type_float=False)


seventh_program()

