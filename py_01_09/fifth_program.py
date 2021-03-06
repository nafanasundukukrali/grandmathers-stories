# Программа для подсчёта в каждой строке матрицы D количества элементов, превышающих
# суммы элементов соответствующих строк матрицы Z, размещения этого
# количества в массиве G, умножения матрицу D на максимальный элемент
# массива G и напечатывания матрицы D до и после преобразования, а также массив G.
# Входные данные прописаны в используемых фукнциях
# Выходные данные прописаны в используемых фукнциях


from default_matrix_funtions import rectangle_matrix_input, default_matrix_print


def fifth_program():
    """
    Процедура для подсчёта в каждой строке матрицы D количества элементов, превышающих
    суммы элементов соответствующих строк матрицы Z, размещения этого
    количества в массиве G, умножения матрицу D на максимальный элемент
    массива G и напечатывания матрицы D до и после преобразования, а также массив G.
    Параметры отсуствуют.
    Входные данные отсуствуют.
    Выходные данные: массив G и матрица D до и после преобразований
    """
    # Ввод матрицы D
    print('Ввод матрицы D:')
    matrix_d = rectangle_matrix_input()
    # Вывод матрицы D до преобразований
    print('Матрица D:')
    default_matrix_print(matrix_d)
    # Ввод матрицы Z, с условием что её разме сопостовим с размерами матрицы D
    print('Ввод матрицы Z:')
    matrix_z = rectangle_matrix_input(input_rows=len(matrix_d))
    # Создание массива G
    array_g = [len(list(filter(lambda x: x > sum(matrix_z[i]), matrix_d[i])))for i in range((len(matrix_d)))]
    # Вывод массива G
    print('Массив G:')
    print(*array_g)
    # Пеобразование матрицы D
    for i in range(len(matrix_d)):
        for j in range(len(matrix_d[i])):
            matrix_d[i][j] *= array_g[i]
    # Вывод матрицы D
    print('Новая матрица D:')
    default_matrix_print(matrix_d)


fifth_program()
