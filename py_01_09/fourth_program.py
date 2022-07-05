# Программа для поворота квадратной матрицы на 90 градусов по часовой стрелке, затем на 90
# градусов против часовой стрелки и вывода промежуточную и итоговой матрицу.
# Входные данные прописаны в используемых фукнциях
# Выходные данные прописаны в используемых фукнциях


from default_matrix_funtions import square_float_matrix_input, default_matrix_print


def fourth_program():
    """
    Процедура для поворота квадратной матрицы на 90 градусов по часовой стрелке, затем на 90
    градусов против часовой стрелки и вывода промежуточную и итоговой матрицу.
    Параметры отсуствуют.
    Выходные данные отсуствуют.
    Входные данные отсуствуют.
    """
    # Ввод матрицы
    matrix = square_float_matrix_input()
    # Поворот на 90 градусов
    for i in range(len(matrix)):
        for j in range(i, len(matrix)-i-1):
            (matrix[i][j], matrix[j][len(matrix) - 1 - i], matrix[len(matrix) - 1 - i][len(matrix) - 1 - j],
             matrix[len(matrix) - 1 - j][i]) = (matrix[len(matrix) - 1 - j][i],
                                                matrix[i][j], matrix[j][len(matrix) - 1 - i],
                                                matrix[len(matrix) - 1 - i][len(matrix) - 1 - j])
    # Вывод матрицы
    print('Поворот на 90 градусов по часовой стрелке квадратичной матрицы:')
    default_matrix_print(matrix)
    # Поворот в обратку
    for i in range(len(matrix)):
        for j in range(i, len(matrix) - i - 1):
            (matrix[len(matrix) - 1 - j][i], matrix[len(matrix) - 1 - i][len(matrix) - 1 - j],
             matrix[j][len(matrix) - 1 - i], matrix[i][j]) = (matrix[i][j], matrix[len(matrix) - 1 - j][i],
                                                              matrix[len(matrix) - 1 - i][len(matrix) - 1 - j],
                                                              matrix[j][len(matrix) - 1 - i])
    # Вывод итоговой матрицы
    print('Итоговая матрица:')
    default_matrix_print(matrix)


fourth_program()


