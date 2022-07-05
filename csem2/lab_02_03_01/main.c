/**
 * Программа для вставки в исходный массив чисел вибоначи после каждогоо кратного 3 числа
 */

#include <stdio.h>

// Ошибочные коды возврата
// Количество элементов не целое
#define COUNT_NOT_INTEGER 1
// Количество элементов меньше 1 или больше MAX_SIZE
#define COUNT_VALUE_ERROR 2
// Какой-то элемент не целое число
#define ELEMENT_NOT_INTEGER 4
// Нет простых чисел среди элементов
#define NOT_PRIME_NUMBERS 5

// True/False
#define TRUE 1
#define FALSE 0

// Успешный код возврата
#define SUCCESS 0
// Количество успешно присвоенных значений переменных
#define SUCCESS_INPUT 1

// Максимальное вводимое количество элементов
#define MAX_LEN 10

void three_swap(int *buffer, int *second_buffer, int *element)
{
    /**
     * Функция для замены элемента предыдущим во время сдвига
     */
    *second_buffer = *element;
    *element = *buffer;
    *buffer = *second_buffer;
}

void input_next_fibonachi(int *old_fibonachi, int *next_fibonachi, int *element)
{
    /**
     * Функция для вставки следующего числа фибоначи после свдига
     */
    *element = *next_fibonachi;
    int buffer = *next_fibonachi;
    *next_fibonachi += *old_fibonachi;
    *old_fibonachi = buffer;
}

void add_fibonachi_numbers(int *elements, int *count)
{
    /**
     * Функция для добавления в массив чисел Фибоначи после позиций с элементами кратными 3
     */
    // Локальная перменная для хранения позиции текущей ячейки нового массива
    int position = 0;
    // Локальная переменная для отслежживания прошлого числа фибоначи
    int old_fibonachi = 0;
    // Локальная переменная для отслеживания последнего полученного числа фибоначи
    int new_fibonachi = 0;

    // Обход всего массива elements до совпадения с количеством элементов или превышения максимума
    while (position < *count && position < MAX_LEN*2)
    {
        if (elements[position] % 3 == 0)
        {
            // Найден элемент, кратный трём

	    // Буфферы для сдвига элементоов вправо на 1
            int buffer, second_buffer;

            // Сдвиг
            buffer = elements[position + 1];
            for (int i = position + 2; i < *count + 1; i++)
            {
                three_swap(&buffer, &second_buffer, &elements[i]);
            }

            if (old_fibonachi == 0 && new_fibonachi == 0)
            {
                // Вставка первого числа фибоначи
                elements[position + 1] = new_fibonachi;
                new_fibonachi = 1;

		// Увеличение текущей позиции
                position += 2;
                *count += 1;
                continue;
            }

	    // Вставка последующих чисел фибоначи
            input_next_fibonachi(&old_fibonachi, &new_fibonachi, &elements[position + 1]);

	    // Увеличение позиции
            position += 2;
            *count += 1;
        }
        else
            // Увеличение позиции
            position++;
    }
}

short input_array(int *elements, const int count)
{
    /**
     * Функция для ввода элеметов массива
     */
    for (int i = 0; i < count; i++)
    {
        printf("Input element of array: ");
        if (scanf("%d", &elements[i]) != SUCCESS_INPUT)
        {
            // Есть нецелое число, это ошибка
            printf("Error: there are zero odd elements\n");
            return ELEMENT_NOT_INTEGER;
        }
    }

    return SUCCESS;
}

void print_array(int *elements, const int count)
{
    /**
     * Функция для вывода элементов массива
     */
    printf("Result: ");
    for (int i = 0; i < count; i++)
        printf("%d ", elements[i]); 
}

int main(void)
{
    // Исходный массив чисел
    int elements[MAX_LEN * 2];
    // Локальная переменная для проверки корректности ввода количества
    // элементов массива
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
        // Меньше 1 или больеш 10
        printf("Error: count if less than zero or more than ten\n");
        return COUNT_VALUE_ERROR;
    }

    // Ввод элементов массива
    short input_check = input_array(elements, count);
    if (input_check != SUCCESS)
    {
        printf("Error: there are not integer elements\n");
        return ELEMENT_NOT_INTEGER;
    }

    // Заполнение старого массива числами Фибоначи
    add_fibonachi_numbers(elements, &count); 

    // Вывод значений элементов нового массива
    print_array(elements, count);

    // Возврат кода успешного завершения работы программы
    return SUCCESS;  
}

