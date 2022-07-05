/**
 * Программа для сортировки введённоог массива пузырьком
 */

#include <stdio.h>
#include <stdbool.h>

// Ошибочные коды возврата
// Количество элементов больше указанного в MAX_LEN
#define COUNT_MORE_MAX_LEN 100
// Количество элементво равно 0
#define COUNT_ZERO 6

// Успешный код возврата
#define SUCCESS 0

// Максимальное вводимое количество элементов
#define MAX_LEN 10

// Количество корректо введённых значений
#define SUCCESS_INPUT 1

void swap_elements(int *element1, int *element2)
{
    /**
     * Функция для перестановки элементов местами
     */
    int buffer = *element1;
    *element1 = *element2;
    *element2 = buffer;
}

void bubble_sort(int *elements, const int count)
{
    /**
     * Функция для сортировки пузырькм массива elements длины count по взрастанию
     */
    
    // Сортировка массива
    for (int i = 0; i < count; i++)
    {
        for (int j = 0; j < count - 1; j++) 
        {
            if (elements[j] > elements[j + 1]) 
                swap_elements(&elements[j], &elements[j + 1]);
        }
    }
}

int input_array(int *elements)
{
    /**
     * Функция для ввода элементов массива
     */
    
    int count = 0;
    
    // Ввод элементов массива
    printf("Input element of array: ");
    while (count < MAX_LEN && scanf("%d", &elements[count]) == SUCCESS_INPUT)
    {
        printf("Input element of array: ");
        count++;
    }
    return count;
}

void print_array(int *elements, const int count)
{
    /**
     * Функция для вывода элементов массива
     */
    printf("Result: ");
    for (int i = 0; i < count; i++)
        printf("%d ", elements[i]);
    printf("\n");
}

int main(void)
{
    // Исходный массив чисел
    int elements[MAX_LEN];
    // Локальная переменная для проверки корректности ввода количества
    // элементов массива (здесь же ввод элементов массива)
    int count = input_array(elements);
    if (count == 0)
    {
        printf("Error: zero elements");
        return COUNT_ZERO;
    }

    // Проверка на то, что не введён массив с количествов элементов больше 10
    int buffer;
    bool more_than_ten = count == 10 && scanf("%d", &buffer);
    
    // Сортировка массива и заполнение его числами Фибоначи
    bubble_sort(elements, count); 

    // Вывод значений элементов нового массива
    print_array(elements, count);

    // Возврат кода успешного завершения работы программы
    if (more_than_ten)
        return COUNT_MORE_MAX_LEN;
    return SUCCESS;  
}

