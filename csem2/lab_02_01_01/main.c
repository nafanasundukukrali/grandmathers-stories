/**
 * Программа для нахождения произведения нечётных чисел в массиве
 */

#include <stdio.h>
#include <stdlib.h>

// Ошибочные коды возврата
// Количество элементов не целое
#define COUNT_NOT_INTEGER 1
// Количество элементов меньше 0
#define COUNT_VALUE_ERROR 2
// Какой-то элемент не целое число
#define ELEMENT_NOT_INTEGER -1
// Нет нечётных элементв
#define NOT_ODD_NUMBERS 5

// Успешный код возврата
#define SUCCESS 0
// Учпешный ввод значения переменной
#define SUCCESS_INPUT 1

// Максимальное вводимое количество элементов
#define MAX_LEN 10


int get_odd_numbers_composition(int *elements, const int count)
{
    /**
     * Функция для нахлждения произведения нечётных чисел в массиве
     */
    // Результат
    int result = 1;

    // Цикл для перебора элементов и получения произведения 
    for (int i = 0; i < count; i++)
        if (abs(elements[i]) % 2 == 1)
            result *= elements[i];

    // Возвращение результата
    return result;
}

int input_array(int *elements, const int count)
{
    /**
     * Функция для ввода элементов в массив
     */
    int odd_numbers_counter = 0;
    for (int i = 0; i < count; i++)
    {
        printf("Input element of array: ");
        if (scanf("%d", &elements[i]) != SUCCESS_INPUT)
        {
            // Есть нецелое число, это ошибка
            return ELEMENT_NOT_INTEGER;
        }
	// Проверка, что число нечётное
        if (abs(elements[i]) % 2 == 1)
            odd_numbers_counter++;
    }
    return odd_numbers_counter;
}

int main(void)
{
    // Исходный массив чисел
    int elements[MAX_LEN];
    // Количество элементоов в массиве (для проверки корректности ввода)
    int count;
    
    // Ввод количества элементов массива и проверка корректности ввода
    printf("Input count: ");
    if (scanf("%d", &count) != SUCCESS_INPUT)
    {
        // Не является целым числом
        printf("Error: count is not integer\n");
        return COUNT_NOT_INTEGER;
    }
    if (count <= 0 || count > MAX_LEN)
    {
        // Меньше 1 или больше 10
        printf("Error: count if less than zero or more than ten\n");
        return COUNT_VALUE_ERROR;
    }

    // Локальная переменная для попутной проверки того, что в ведённом массиве есть нечётные числа
    int odd_number_counter = input_array(elements, count);

    // Проверка того, что в списке есть нечётные числа
    if (odd_number_counter == 0)
    {
        printf("Error: there are zero odd elements\n");
        return NOT_ODD_NUMBERS;
    }
    // Проверка корректности ввода элементов массива
    if (odd_number_counter < 0)
    {
        printf("Error: there are not integer elements\n");
        return ELEMENT_NOT_INTEGER;
    }
    
    // Подсчёт произведения нечётных чисел в массиве
    int result = get_odd_numbers_composition(elements, count); 

    // Вывод результата
    printf("Result: %d\n", result);

    // Возврат кода успешного завершения работы программы
    return SUCCESS;  
}

