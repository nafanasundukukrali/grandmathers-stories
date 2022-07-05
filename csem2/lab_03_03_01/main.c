/**
 * Программа для сортировки строк матрицы в порядке убывания по наибольшему элементу
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

int get_max_array_element(int *matrix, const size_t count)
{
    /**
     * Функция для поиска наибольшего элемента в строке
     */
    int max_element = matrix[0];

    for (size_t i = 0; i < count; i++)
        if (max_element < matrix[i])
            max_element = matrix[i];

    return max_element;
}

void swap_rows(int *row1, int *row2, const size_t count)
{
    /**
     * Функция для переставления элементов строк матриц местами
     */
    for (size_t i = 0; i < count; i++)
    {
        int buffer = row1[i];
        row1[i] = row2[i];
        row2[i] = buffer;
    }
}

void sort_matrix_rows(int (*matrix)[MAX_SIZE], const size_t rows, const size_t columns)
{
    /**
     * Функция для сортировки строк матрицы в порядке убывания по наибольшему элементу
     * с использыванием сортировки пузырьком
     */ 
    for (size_t i = 0; i < rows; i++)
        for (size_t j = 0; j < rows - 1; j++)
            if (get_max_array_element(matrix[j], columns) < get_max_array_element(matrix[j + 1], columns))
                swap_rows(matrix[j], matrix[j + 1], columns);
}

short input_count(size_t *count, int which_count)
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

    // Ввод матрицы
    if (exit_code == SUCCESS)
        exit_code = input_matrix(matrix, rows, columns);

    if (exit_code == ERROR_ELEMENT_NOT_INT)
        printf("Error: not integer element of matrix\n");
    
    if (exit_code == SUCCESS)
    {
        // Сортировка матрицы по наибольшему элементу в порядке убывания
        sort_matrix_rows(matrix, rows, columns);    
 
        // Вывод матрицы
        print_matrix(matrix, rows, columns);
    }

    return exit_code;
}

