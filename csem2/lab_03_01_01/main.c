/**
 * Программа для нахождения массива, где каждый элемент равен 1, если в сооотвествующей
 * строке матрицы элементы симметричны.
 */
#include <stdio.h>

// Коды возврата ошибок
// Количество строк или столбцов не целое
#define ERROR_PARAM_MATRIX_NOT_INT 1
// Количество строк или столбцов больше MAX_SIZE или меньше 1
#define ERROR_PARAM_MATRIX_INCCOR_NUMBER 2
// Какой-то элемент не целый
#define ERROR_ELEMENT_NOT_INT -1 

// Код возврата успешного завершения работы функции
#define SUCCESS 0

// Количество корректно введённых значений для scanf
#define CORRECT_INPUTS_COUNT 1

// Максимальное количество строк и столбцов
#define MAX_SIZE 10
// Минимальное значение количества строки столбцов
#define MIN_SIZE 1

short input_matrix(int (*matrix)[MAX_SIZE], const size_t rows, const size_t columns)
{
    /**
     * Функция для заполнения исходной матрицы вводимыми элементами
     * по указателю на начальную строку матрицы, количество строк и столбцов
     */
    short return_code = SUCCESS;

    for (size_t i = 0; i < rows && return_code == SUCCESS; i++) 
        for (size_t j = 0; j < columns; j++)
        {
            printf("Input element: ");
            
            if (scanf("%d", &matrix[i][j]) != CORRECT_INPUTS_COUNT)
                return_code = ERROR_ELEMENT_NOT_INT;
        }
    
    return return_code;
}

void print_array(int *array, const size_t count)
{
    /**
     * Функция для вывода элементов массива
     */
    printf("Result: ");

    for (size_t i = 0; i < count; i++)
        printf("%d ", array[i]);

    printf("\n");
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

        return_code = ERROR_PARAM_MATRIX_INCCOR_NUMBER;
    }

    return return_code;
}

void find_symmetric_rows(int *array, int (*matrix)[MAX_SIZE], const size_t rows, const size_t columns)
{
    /**
     * Функция для нахождения симметричных строк
     */

    for (size_t i = 0; i < rows; i++)
    {
        size_t count = 0;

        for (size_t j = 0; j < columns; j++)
            if (matrix[i][j] == matrix[i][columns - 1 - j])
                count++;

        if (count == columns || count + 1 == columns)
            array[i] = 1;
        else
            array[i] = 0;
    }
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
    short exit_code = input_count(&rows, 1);
    
    exit_code = (!exit_code ? input_count(&columns, 0) : exit_code);
    
    // Ввод матрицы
    exit_code = (!exit_code ? input_matrix(matrix, rows, columns) : exit_code);

    if (exit_code == ERROR_ELEMENT_NOT_INT)
        printf("Error: not integer element of matrix\n");
        
    if (!exit_code)
    {
        // Получение искомого массива
        int result[MAX_SIZE];
        find_symmetric_rows(result, matrix, rows, columns);
 
        // Вывод полученного массива
        print_array(result, rows);
    }

    return exit_code;
}

