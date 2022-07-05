# Программа для вывода трёхмерного массива (массив матриц размера X*Y*Z) и его i-й среза по второму индексу.
# Входные данные прописаны в используемых фукнциях
# Выходные данные прописаны в используемых фукнциях

def v3_array_input(matrix):
    user_x_y_z = input('Введите параметры x, y, z матрицы: ')
    while (len(user_x_y_z.split(' ')) != 3 or not user_x_y_z.split(' ')[0].isdigit() or
           not user_x_y_z.split(' ')[1].isdigit() or not user_x_y_z.split(' ')[2].isdigit() or
           int(user_x_y_z.split(' ')[0] == 0)):
        user_answer = input('Параметры матрицы заданы неверно. Попробуйте ввести их заново? [Д/Н]: ')
        if user_answer == 'Д':
            user_x_y_z = input('Введите параметры x, y, z матрицы:')
        elif user_answer == 'Н':
            print('Операция прервана.')
            return
        else:
            print('Ответ введен некорректно. Повторите ввод.')
    x = int(user_x_y_z.split(' ')[0])
    y = int(user_x_y_z.split(' ')[1])
    z = int(user_x_y_z.split(' ')[2])
    for i in range(x):
        new_j_list = []
        for j in range(y):
            new_k_list = []
            for k in range(z):
                new_k_list.append(input(f'Введите {k+1} элемент {j+1} массива {i+1} строки трёхмерного массива: '))
            new_j_list.append(new_k_list)
        matrix.append(new_j_list)


def ninth_program():
    """
    Процедура для вывода трёхмерного массива (массив матриц размера X*Y*Z) и его i-й среза по второму индексу.
    Параметры отсуствуют
    Входные данные отсуствуют
    Выходные данные: i-й срез
    """
    # Матрица
    matrix = []
    # Ввод трёхмерного массива (без проверки данных, так как не было указано какого типа они должны быть)
    v3_array_input(matrix)
    # Ввод номера среза и его проверка
    user_i = input(f'Введите номер среза, считая, что 1-й массив трёхмерной матрицы стоит под номером 1. '
                   f'Номер среза не может быть больше {len(matrix)}: ')
    while not (user_i.isdigit() and len(matrix) >= int(user_i) > 0):
        user_answer = input('Введённый номер среза не корректный. Повторить ввод данных? [Д/Н]: ')
        if user_answer == 'Д':
            user_i = input(f'Введите номер среза, считая, что 1-й массив трёхмерной матрицы стоит под номером 1. '
                           f'Номер среза не может быть больше {len(matrix)}: ')
        elif user_answer == 'Н':
            print('Работа программы завершена')
            return
        else:
            print('Ответ дан некорректно. Повторите ввод ответа.')
    # Вывод i-го среза
    print('i-й срез:')
    user_k = int(user_i)-1
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            print(matrix[i][j][user_k], end=' ')
        print()


ninth_program()
