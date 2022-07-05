/**
 * Программа для создания нового массива с простыми числами из входного массива
 */

#include <stdio.h>

// Ошибочные коды возврата
// Количество элементов не целое
#define COUNT_NOT_INTEGER 1
// Количество элементов меньше 1 или больше MAX_LEN
#define COUNT_VALUE_ERROR 2
// Какой-то элемент не целое число
#define ELEMENT_NOT_INTEGER -1
// Нет простых чисел среди элементов
#define NOT_PRIME_NUMBERS 5

// true/false
#define TRUE 1
#define FALSE 0

// Успешный код возврата
#define SUCCESS 0
// Успешное количество присваиваний значений перменным
#define SUCCESS_INPUT 1

// Максимальное вводимое количество элементов
#define MAX_LEN 10

short check_prime_number(int a)
{
    /**
     * Функция для проверки того, что число a является простым
     */
    // Проверка, что число натуральное
    if (a <= 1)
        return FALSE;
    // Переменная для хранения текущего делителя
    int divider = 2;
    
    // Увеличение ткущего делителя, пока его квадрат не станет больше числа или
    // он не окажется делителем числа
    while (divider * divider < a && a % divider != 0)
        divider++;
    
    // Если не являетсяделителем, то квадрат полученного числа
    // дожен быть больше интересующего числа
    return ((divider * divider > a && a % divider != 0) || a == 2);
}

int get_prime_numbers_array(int *old_elements, const int old_count, int *new_elements)
{
    /**
     * Функция для нахождения простых чисел в массиве old_elements
     * и перемещение их в массив new_elements
     */
    // Локальная перменная для хранения позиции текущей ячейки нового массива
    int counter = 0;

    // Обход всего массива old_elementis
    for (int i = 0; i < old_count; i++)
        if (check_prime_number(old_elements[i]))
        {
            new_elements[counter] = old_elements[i];
            counter++;
        }

    // Возвращает количество элементов в новом масиве
    return counter;
}

short input_array(int *elements, const int count)
{
    /**
     * Функция для ввода элементов массива count длины elements
     */

    // Локальная переменная для попутной проверки того, что в ведённом массиве есть нечётные числа
    short prime_numbers_there = FALSE;
    // Ввод элементов массива
    for (int i = 0; i < count; i++)
    {
        printf("Input element of array: ");
        if (scanf("%d", &elements[i]) != SUCCESS_INPUT)
        {
            // Есть нецелое число, это ошибка
            return ELEMENT_NOT_INTEGER;
        }

	// Проверка, что есть число простое в списке
        if (!prime_numbers_there && check_prime_number(elements[i]))
            prime_numbers_there = TRUE;
    }
    return prime_numbers_there;
}

void print_array(int *elements, const int count)
{
    /**
     * Функция для вывода значений элементов массива
     */
    printf("Result: ");
    for (int i = 0; i < count; i++)
        printf("%d ", elements[i]);
}

int main(void)
{
    // Исходный массив чисел
    int elements[MAX_LEN];
    // Локальная переменная для проверки корректности ввода количества
    // элементов массива
    int input_count;
    
    // Ввод количества элементов массива и проверка корректности ввода
    printf("Input count: ");
    if (scanf("%d", &input_count) != SUCCESS_INPUT)
    {
        // Не является целым числом
        printf("Error: count is not integer\n");
        return COUNT_NOT_INTEGER;
    }
    if (input_count <= 0 || input_count > MAX_LEN)
    {
        // Меньше 1 или больше 10
        printf("Error: count if less than zero or more than ten\n");
        return COUNT_VALUE_ERROR;
    }

    // Локальная переменная для попутной проверки того, что в ведённом массиве есть нечётные числа
    short prime_numbers_there = input_array(elements, input_count);

    // Проверка того, что в массиве есть простые числа
    if (!prime_numbers_there)
    {
        printf("Error: there are zero prime numbers elements\n");
        return NOT_PRIME_NUMBERS;
    }
    // Проверка того, что массив ведён корректно
    if (prime_numbers_there == ELEMENT_NOT_INTEGER)
    {
        printf("Error: there are not integer elements\n");
        return ELEMENT_NOT_INTEGER;
    }

    // Новый массив
    int new_elements[MAX_LEN];
    // Заполнение нового массива
    const int new_count = get_prime_numbers_array(elements, input_count, new_elements); 

    // Вывод значений элементов нового массива
    print_array(new_elements, new_count);

    // Возврат кода успешного завершения работы программы
    return SUCCESS;  
}

