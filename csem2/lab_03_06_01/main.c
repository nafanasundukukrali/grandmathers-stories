/**
 * Программа для заполнения квадратной матрицы по спирали
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
// Количество строк не равно количеству столбцов
#define ERROR_NOT_SQUARE_PARAM 4

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

void input_matrix(int (*matrix)[MAX_SIZE], const int size)
{
    /**
     * Функция для заполнения исходной матрицы числами по спирали
     */
    
    int number = 1; 
    int iteration = 0;
    int line_count = 0;
    matrix[size / 5][size / 2] = size * size;

    while (number <= size * size)
    { 
        for (int i = 0; i < size - iteration; i++)
        {
            matrix[line_count][i + line_count] = number;
            number += 1;
        } 

        for (int i = line_count + 1; i < size - line_count; i++)
        {
            matrix[i][size - 1 - line_count] = number;
            number += 1;
        }

        for (int i = line_count + 1; i < size - line_count; i++)
        {
            matrix[size - line_count - 1][size - i - 1] = number;
            number += 1;
        }

        for (int i = line_count + 1; i < size - 1 - line_count; i++)
        {
            matrix[size - i - 1][line_count] = number;
            number += 1;
        }

        line_count += 1;
        iteration += 2;
    }
}

void print_matrix(int (*matrix)[MAX_SIZE], const int rows, const int columns)
{
    /**
     * Функция для вывода элементов матрицы в терминал. 
     * Параметрами являются указатель на начальную строку матрицы,
     * количество строк и количество столбцов.
     */
    printf("Result: \n");

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
            printf("%d ", matrix[i][j]);

        printf("\n");
    }
}

short input_count(int *count, const int which_count)
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

    if (scanf("%d", count) != CORRECT_INPUTS_COUNT)
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
    int rows;
    // КОличество столбцов
    int columns;
    
    // Получение количество строк и столбцов
    short exit_code = input_count(&rows, 1);

    if (exit_code == SUCCESS)
        exit_code = input_count(&columns, 0);

    if (exit_code == SUCCESS && columns != rows)
    {
        printf("Error: there are not square matrix params\n");
        exit_code = ERROR_NOT_SQUARE_PARAM;
    }

    if (exit_code == SUCCESS)
    {
        // Заполнение матрицы числами
        input_matrix(matrix, rows);
 
        // Вывод матрицы
        print_matrix(matrix, rows, columns);
    }

    return exit_code;
}

