/**
 * Программа для нахождения элемента с минимальной суммой цифр и удаления столбца, где стоит этот
 * элемент и строки.
 */
#include <stdio.h>
#include <stdlib.h>

// Коды возврата ошибок
// Количество строк или столбцов не целое
#define ERROR_PARAM_MATRIX_NOT_INT 1
// Количество строк или столбцов больше MAX_SIZE или меньше 1
#define ERROR_PARAM_MATRIX_INCCOR_NUM 2
// Какой-то элемент не целый
#define ERROR_ELEMENT_NOT_INT 3

// Код возврата успешного завершения работы функции
#define SUCCESS 0

// True/False
#define TRUE 1
#define FALSE 0

// Количество корректно введённых значений для scanf
#define CORRECT_INPUTS_COUNT 1

// Максимальное количество строк и столбцов
#define MAX_SIZE 10
// Минимальное количество строк и столбцов
#define MIN_SIZE 2

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

int get_numbers_sum(int number)
{
    /**
     * Функция для нахождения суммы цифр числа
     */
    int result = 0;
    number = abs(number);
    
    while (number > 0)
    {
        result += number % 10;
        number /= 10;
    }

    return result;
}

int get_min_sum_numbers_number(int (*matrix)[MAX_SIZE], const size_t rows, const size_t columns)
{
    /**
     * Функция для поиска элемента с минимальной суммой цифр в матрице
     */
    int min_sum = get_numbers_sum(matrix[0][0]);
    int min_number = matrix[0][0];

    for (size_t i = 0; i < rows; i++)
        for (size_t j = 0; j < columns; j++)
            if (min_sum > get_numbers_sum(matrix[i][j]))
            {
                min_number = matrix[i][j];
                min_sum = get_numbers_sum(matrix[i][j]);
            }

    return min_number;
}

void delete_column(int (*matrix)[MAX_SIZE], const size_t rows, const size_t columns, const size_t element_column)
{
    /**
     * Функция для удаления столбца, как только встречается элемент больше 
     * element_column
     */

    for (size_t i = 0; i < rows; i++)
        for (size_t j = 0; j < columns - 1; j++)
            if (j >= element_column)
                matrix[i][j] = matrix[i][j + 1];
}

void delete_row(int (*matrix)[MAX_SIZE], const size_t rows, const size_t columns, const size_t element_row)
{
    /**
     * Функция для удаления строки, как только встречается элемент больше
     * element_row
     */
    for (size_t i = 0; i < rows - 1; i++)
        for (size_t j = 0; j < columns; j++)
            if (i >= element_row)
                matrix[i][j] = matrix[i + 1][j];
}

void remove_column_and_row(int (*matrix)[MAX_SIZE], size_t *rows, size_t *columns)
{
    /**
     * Функция для нахождения элемента с минимальноой суммой цифр и удаления строки
     * и столбца, где такой элемент впервые встречается
     */
    int min_sum_numbers = get_min_sum_numbers_number(matrix, *rows, *columns);
    size_t element_column = 0, element_row = 0;
    
    for (size_t i = 0; i < *rows; i++)
        for (size_t j = 0; j < *columns; j++)
            if (matrix[i][j] == min_sum_numbers)
            {
                element_column = j;
                element_row = i;
            }  

    delete_column(matrix, *rows, *columns, element_column);
    delete_row(matrix, *rows, *columns, element_row); 
    *rows = *rows - 1;
    *columns = *columns - 1;
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

    if (!exit_code)
        exit_code = input_count(&columns, 0);

    // Ввод матрицы
    if (!exit_code)
        exit_code = input_matrix(matrix, rows, columns);
    
    if (exit_code == ERROR_ELEMENT_NOT_INT)
        printf("Error: not integer element of matrix\n");
    
    if (!exit_code)
    {
	// Удаление строки и столбца, где находится элемент с минимальной суммой цифр
        remove_column_and_row(matrix, &rows, &columns);    
 
        // Вывод матрицы
        print_matrix(matrix, rows, columns);
    }

    return exit_code;
}

