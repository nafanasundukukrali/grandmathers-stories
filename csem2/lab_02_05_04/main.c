/**
 * Программа для нахождения уникальных элментов массива
 */

#include <stdio.h>


// Ошибочные коды возврата
// Количество элементов не целое
#define COUNT_NOT_INTEGER 1
// Количество элементов меньше 1
#define COUNT_VALUE_ERROR 2
// Количество элементов больше 10
#define COUNT_MORE_MAX_LEN 3
// Какой-то элемент не целое число
#define ELEMENT_NOT_INTEGER 4
// Нет простых чисел среди элементов
#define NOT_PRIME_NUMBERS 5

// True/false
#define TRUE 1
#define FALSE 0

// Успешный код возврата
#define SUCCESS 0
// Учпешный код присваивания полученной значения значению переменной
#define SUCCESS_INPUT 1

// Максимальное вводимое количество элементов
#define MAX_LEN 10

void swap_elements(int *first_elem, int *second_elem)
{
    /**
     * Функция для перестановки значений элементов
     */
    int buffer = *first_elem;
    *first_elem = *second_elem;
    *second_elem = buffer;
}

void bubble_sort(int *start, int *end)
{
    /**
    * Функция для сортировки пузырьком массива, указатель на начальный элемент которого start
    * и указатель на конечный элемент которого end
    */
 
    // Сортировка массива
    for (int *i = start; i != end; i++)
        for (int *j = i + 1; j != end; j++)
            if (*i > *j)
                swap_elements(i, j);
}

int return_unic_elements_count(int *start_elements, int *end_elements)
{
    /**
    * Функция для нахождения количества уникальных элементов массива
    * с указателями на начальный элемент start_elements и указателем
    * на конечный элемент end_elements
    **/
    
    // Количество уникальных элементов
    int unic_count = 0;

    // Проверка, что количество элементов равно 0
    if (start_elements == end_elements)
        return unic_count;
    // Сортирока массива по возрастанию
    bubble_sort(start_elements, end_elements);
 
    // Сравнение первого элемента с последующим 
    if (start_elements + 1 != end_elements && *start_elements != *(start_elements + 1))
        unic_count += 1;

    // Проход по массиву со сравнением с предыдущим и последующим элементом
    for (int *i = start_elements + 1; i < end_elements - 1; i++)
        if (*i != *(i + 1))
            unic_count += 1;

    // Учитываем уникальность крайнего элемента
    unic_count += 1;
    
    // Возвращаем количество уникальных элементов
    return unic_count;
}

int *input_array(int *elements, const int count)
{
    /**
     * Функция для ввода элементов массива
     */
  
    int *end_elements = elements;
    for (int i = 0; i < count; i++)
    {
        printf("Input element of array: ");
        if (scanf("%d", elements + i) != 1)
        {
            printf("Error: elements is not number");
            return elements;
        }
        end_elements += 1;
    }
    return end_elements;
}

int main(void)
{
    // Исходный массив чисел
    int elements[MAX_LEN];
    // Локальная переменная для проверки корректности ввода количества
    // элементов массива
    int count = 0;
    // Булевая переменная для хранения информации о том, что количество элементов введено больше MAX_LEN
    short more_than_max_len = FALSE;
    
    printf("Input count: ");
    if (scanf("%d", &count) != 1)
    {
        // Не является целым числом
        printf("Error: count is not integer\n");
        return COUNT_NOT_INTEGER;
    }
    if (count <= 0)
    {
        // Меньше 1 или больше 10
        printf("Error: count less than zero or more than ten\n");
        return COUNT_VALUE_ERROR;
    }
    if (count > MAX_LEN)
    {
        count = MAX_LEN;
        more_than_max_len = TRUE;
    }
    
    // Ввод элементов массива
    int *end_elements = input_array(elements, count);
    if (end_elements == elements)
    {
        printf("Error: there are not integer elements\n");
        return ELEMENT_NOT_INTEGER;
    }

 
    // Нахождение количества уникальных элементов
    int unic_elements_count = return_unic_elements_count(elements, end_elements);
     
    // Вывод количества уникальных элементов 
    printf("Result: %d\n", unic_elements_count);

    // Возврат кода успешного завершения работы программы
    if (more_than_max_len)
        return COUNT_MORE_MAX_LEN;
    return SUCCESS;  
}

