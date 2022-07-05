/**
 * Программа для отражения элементов матрицы между диагоналями
 * относительно центрального элемента
 */

#include <stdio.h>

// Коды возврата ошибок
// Количество строк или столбцов не целое
#define ERROR_PARAM_MATRIX_NOT_INT 1
// Количество строк или столбцов больше MAX_SIZE или меньше 1
#define ERROR_PARAM_MATRIX_INCCOR_NUM 2
// Какой-то элемент не целый
#define ERROR_ELEMENT_NOT_INT 3
// Количество строк не равно количеству столбцов
#define ERROR_NOT_SAME_PARAM 4

// Код возврата успешного завершения работы функции
#define SUCCESS 0

// Количество корректно введённых значений для scanf
#define CORRECT_INPUTS_COUNT 1

// Максимальное количество строк и столбцов
#define MAX_SIZE 10
// Минимальное количество строк и столбцов
#define MIN_SIZE 1

short input_matrix(int (*matrix)[MAX_SIZE], const size_t rows, const size_t columns)
{
    /**
     * Функция для заполнения исходной матрицы вводимыми элементами
     * по указателю на начальную строку матрицы, количество строк и столбцов
     */
    short return_code = SUCCESS;

    for (size_t i = 0; i < rows && return_code == SUCCESS; i++)
        for (size_t j = 0; j < columns && return_code == SUCCESS; j++)
        {
            printf("Input element: ");

            if (scanf("%d", &matrix[i][j]) != CORRECT_INPUTS_COUNT)
                return_code = ERROR_ELEMENT_NOT_INT;
        }

    return return_code;
}

void print_matrix(int (*matrix)[MAX_SIZE], const size_t rows, const size_t columns)
{
    /**
     * Функция для вывода элементов матрицы в терминал. 
     * Параметрами являются указатель на начальную строку матрицы,
     * количество строк и количество столбцов.
     */
    printf("Result: \n");

    for (size_t i = 0; i < rows; i++)
    {
        for (size_t j = 0; j < columns; j++)
            printf("%d ", matrix[i][j]);

        printf("\n");
    }
}

void swap_elements(int (*matrix)[MAX_SIZE], const size_t row1, const size_t row2, const size_t column)
{
    /**
     * Функция для перестановки дву х элементов матрицы по указанным индексам
     */
    int buffer = matrix[row1][column];
    matrix[row1][column] = matrix[row2][column];
    matrix[row2][column] = buffer;
}

void reflect_matrix_elements(int (*matrix)[MAX_SIZE], const size_t rows, const size_t columns)
{
    /**
     * Функция для отражения элементов между диагоналями матрицы
     */
    for (size_t i = 0; i < rows; i++)
        for (size_t j = i; j < columns - i; j++)
            swap_elements(matrix, i, rows - i - 1, j);
}

short input_count(size_t *count, const int which_count)
{
    /**
     * Функция дл получения количетсва столбцов/строк
     * Значение which_count == 1 - количество столбцов
     * Значение which_count == 0 - количество строк
     */
    short return_code = SUCCESS;

    if (which_count)
        printf("Input rows count:");
    else
        printf("Input column count:");

    if (scanf("%lu", count) != CORRECT_INPUTS_COUNT)
    {
        if (which_count)
            printf("Error: rows count is not integer\n");
        else
            printf("Error: columns count is not integer\n");

        return_code = ERROR_PARAM_MATRIX_NOT_INT;
    }

    if (return_code == SUCCESS && (*count > MAX_SIZE || *count < MIN_SIZE))
    {
        if (which_count)
            printf("Error: columns count is not between zero and eleven\n");
        else
            printf("Error: columns count is not between zero and eleven\n");

        return_code = ERROR_PARAM_MATRIX_INCCOR_NUM;
    }

    return return_code;
}

int main(void)
{
    // Исходная матрица
    int matrix[MAX_SIZE][MAX_SIZE];
    // Количество строк 
    size_t rows;
    // КОличество столбцов
    size_t columns;

    // Получение количество и столбцов и проверка корректности значений
    short exit_code = SUCCESS;
    exit_code = input_count(&rows, 1);

    if (exit_code == SUCCESS)
        exit_code = input_count(&columns, 0);
    
    if (exit_code == SUCCESS && rows != columns)
    {
        printf("Error: not sqare matrix\n");
        exit_code = ERROR_NOT_SAME_PARAM;
    }

    // Ввод матрицы
    if (exit_code == SUCCESS)
    {
        exit_code = input_matrix(matrix, rows, columns);

        if (exit_code != SUCCESS)
            printf("Error: not integer element of matrix\n");
    }

    if (exit_code == SUCCESS)
    {
        // Отражение элементов матрицы между диагоналями
        reflect_matrix_elements(matrix, rows, columns);    
 
        // Вывод матрицы
        print_matrix(matrix, rows, columns);
    }

    return exit_code;
}

