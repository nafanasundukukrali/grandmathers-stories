/**
 * Программа для нахождения элементов с суммой цифр больше 10,
 * помещения их в массив и сдвига этого массива на 3 позиции влево
 */

#include <stdio.h>
#include <stdlib.h>

// Коды возврата ошибок
// Количество строк или столбцов не целое
#define ERROR_PARAM_MATRIX_NOT_INT 1
// Количество строк или столбцов больше MAX_SIZE или меньше MIN_SIZE
#define ERROR_PARAM_MATRIX_INCCOR_NUM 2
// Какой-то элемент не целый
#define ERROR_ELEMENT_NOT_INT 102
// Нет элементов с суммой цифр больше 10
#define ERROR_NOT_INTRS_NUM 101

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

int get_number_sum(int number)
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

short input_matrix_and_array(int (*matrix) [MAX_SIZE], const size_t rows, const size_t columns, int *array)
{
    /**
     * Функция для заполнения исходной матрицы вводимыми элементами
     * по указателю на начальную строку матрицы, количество строк и столбцов
     */
    short count = 0;
    int buffer = 0;

    for (size_t i = 0; i < rows && count != ERROR_ELEMENT_NOT_INT; i++)
        for (size_t j = 0; j < columns && count != ERROR_ELEMENT_NOT_INT; j++)
        {
            printf("Input element: ");

            if (scanf("%d", &buffer) != CORRECT_INPUTS_COUNT)
                count = ERROR_ELEMENT_NOT_INT;

            if (count != ERROR_ELEMENT_NOT_INT)
            {
                matrix[i][j] = buffer;

                if (get_number_sum(buffer) > 10)
                {
                    array[count] = buffer;
                    count ++;
                }
            }
        }

    if (count == SUCCESS)
        count = ERROR_NOT_INTRS_NUM;

    return count;
}

void print_matrix(int (*matrix) [MAX_SIZE], const size_t row, const size_t columns, int *array)
{
    /**
     * Функция для вывода элементов массива. Параметрами являются
     * указатель на анчальный элемент массива и количество элементов.
     */
    printf("Result: \n");
    int array_index = 0;

    for (size_t i = 0; i < row; i++)
    {
        for (size_t j = 0; j < columns; j++)
            if (get_number_sum(matrix[i][j]) > 10)
            {
                printf("%d ", array[array_index]);
                array_index ++;
            }
            else
                printf("%d ", matrix[i][j]);

        printf("\n");
    }
}

void swap_elements(int *array, const size_t index1, const size_t index2)
{
    /**
     * Функция для перестановки двух элементов массива по указанным индексам
     */
    int buffer = array[index1];
    array[index1] = array[index2];
    array[index2] = buffer;
}

void move_elements_to_left(int *array, const size_t count)
{
    /**
     * Функция для сдвига массива на 3 позиции влево
     */
    for (size_t i = 0; i < 3; i++)
        for (size_t j = 0; j < count - 1; j++)
            swap_elements(array, j, j + 1);
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
    // Количество строк 
    size_t rows;
    // КОличество столбцов
    size_t columns;
    // Искомый массив  с числами
    int array[MAX_SIZE * MAX_SIZE];
    // Матрица
    int matrix[MAX_SIZE][MAX_SIZE];
    size_t count;

    // Получение количество и столбцов и проверка корректности значений
    short exit_code = input_count(&rows, 1);

    if (exit_code == SUCCESS)
        exit_code = input_count(&columns, 0);

    if (exit_code == SUCCESS)
    {
        count = input_matrix_and_array(matrix, rows, columns, array);

        if (count == ERROR_ELEMENT_NOT_INT)
        {
            printf("Error: not integer element of matrix\n");
            exit_code = ERROR_ELEMENT_NOT_INT;
        }
        else if (count == ERROR_NOT_INTRS_NUM)
        {
            printf("Error: all sum numbers less than eleven\n");
            exit_code = ERROR_NOT_INTRS_NUM;
        }
    }

    if (exit_code == SUCCESS)
    {
        // Сдвиг влево на 3 позиции
        move_elements_to_left(array, count);    
 
        // Вывод матрицы
        print_matrix(matrix, rows, columns, array);
    }

    return exit_code;
}

