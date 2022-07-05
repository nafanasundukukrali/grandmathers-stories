/**
 * Программа для нахождения НОД двух вещественных чисел
 */

#include <stdio.h>

// Код возврата в случае корректного завершения работы программы
#define SUCCESS 0
// Код возврата в случае ошибки
#define ERROR 1

int get_nod(int a, int b)
{
    /**
     * Функция для нахождения НОД двух чисел через алгоритм Евклида
     */
    while (b != 0 && a != 0)
    {
        if (a > b)
        {
            a = a % b;
        }
        else
        {
            b = b % a;
        }
    }
    return (a + b);
}

int main(void)
{
    // Исходные два натуральных числа
    int value_a, value_b;

    // Ввод исходных натуральных чисел с проверкой на то, что оба числа были введены корректно
    printf("Input two natural numbers with space between theme: ");
    if (scanf("%d%d", &value_a, &value_b) != 2 || value_a <= 1 || value_b <= 1)
    {
        printf("Input values are incorrect.");
        return ERROR;
    }

    // Нахождение НОД
    int result = get_nod(value_a, value_b);

    // Вывод результата
    printf("Result: %d\n", result);
    
    // Заврешение работы программы без ошибок
    return SUCCESS;
}

