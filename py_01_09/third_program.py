# Программа для транспонирования квадратной матрицы
# Входные данные прописаны в используемых фукнциях
# Выходные данные прописаны в используемых фукнциях


from default_matrix_funtions import square_float_matrix_input, default_matrix_print


def third_program():
    """
    Процедура для транспонирования матрицы.
    Парметры отсуствуют.
    Входные данные отсуствуют.
    Выходные данные отсуствуют.
    """
    # Ввод транспонированной матрицы
    matrix = square_float_matrix_input()
    # Транспонирование
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    print('Транспонированная матрица:')
    # Вывод транспонированной матрицы
    default_matrix_print(matrix)


third_program()
