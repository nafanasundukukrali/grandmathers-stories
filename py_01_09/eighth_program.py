# Программа для формирования матрицы C путём построчного перемножения матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B), сложения всех
# элементы в столбцах матрицы C и записи их в массив V.
# Входные данные прописаны в используемых фукнциях
# Выходные данные прописаны в используемых фукнциях


from default_matrix_funtions import rectangle_matrix_input, default_matrix_print
from array_functions import default_float_array_print


def eighth_program():
    """
    Процедура для формирования матрицы C путём построчного перемножения матриц A и B
    одинаковой размерности (элементы в i-й строке матрицы A умножаются на
    соответствующие элементы в i-й строке матрицы B), сложения всех
    элементы в столбцах матрицы C и записи их в массив V.
    Параметры отсуствуют.
    Входные данные отсуствуют.
    Выходные данные отсуствуют.
    """
    # Ввод матрицы A
    matrix_a = rectangle_matrix_input()
    # Ввод матрицы B с параметрами матрицы A
    matrix_b = rectangle_matrix_input(input_rows=len(matrix_a), input_columns=(len(matrix_a[0]) if len(matrix_a)
                                                                               else 0))
    # Формирование матрицы C
    matrix_c = [[matrix_b[i][j]*matrix_a[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
    # Вывод матрицы C
    print('Матрица C:')
    default_matrix_print(matrix_c)
    # Переменная для массива V
    array_v = []
    # Формировнаие массива V
    for i in range(len(matrix_c[0]) if len(matrix_c) else 0):
        sum_of_column = 0
        for j in range(len(matrix_a)):
            sum_of_column += matrix_c[j][i]
        array_v.append(sum_of_column)
    # Вывод массива V
    print('Массив V:')
    default_float_array_print(array_v)


eighth_program()


