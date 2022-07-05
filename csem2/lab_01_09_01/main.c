/**
 * Программа для вывода синуса от суммы корней неотрицательных чисел.
 */

#include <stdio.h>
#include <math.h>

// Код возврата в случае ошибки
#define ERROR 1
// Код возврата успешного завершения работы программы
#define SUCCESS 0
// Код возврата в случае некорректного ввода значения
#define INCORRECT_INPUT -1
// Эпсилон для сравнения вещественных чисел
#define EPSILON 1e-8

double get_sin_argument_sum()
{
    /**
     * Функция для вычисления суммы корней введённых чисел, делённых на их номер в
     * последовательности.
     * Возвращает соответствующую сумму.
     */
    
    // Значение для старта
    double input_value = 0;
    // Искомая сумма
    double sum = 0;
    // Текущий порядковый номер
    int counter = 0;
    
    // Приглашение ввода для последовательности чисел
    printf("Input numbers with space between theme: ");
    // Цикл обработки с условием работы, пока не будет обнаружено отрицательное число
    while (input_value > 0 || fabs(input_value) < EPSILON)
    {
        // Обработка стартового значения
        if (counter == 0)
        {
            //
            sum = 0;
        }
        else
        {
            // Прибавление соотвествующего номеру элемента последовательности
            sum += sqrt(input_value / counter);
        }

	// Увеличение счётчика чисел
        counter += 1;
        
	// Ввод нового числа и обработка корректности введённых данных
        if ((scanf("%lf", &input_value) != 1) ||
            (input_value < 0 && counter == 1))
            return INCORRECT_INPUT;
    }

    // Возврат суммы
    return sum;
}

int main(void)
{
    // Вычисление соотвествующей суммы корней для ичпользования её как аргумента синуса
    double sin_argument_sum = get_sin_argument_sum();
    // Проверка был ли корретен ввод каждого числа на основании сравнения результата
    // с кодом ошибки ввода
    if (fabs(sin_argument_sum - INCORRECT_INPUT) < EPSILON)
    {
        printf("Input values are incorrect.");
        return ERROR;
    }
    
    // Вычисление результата
    double result = sin(sin_argument_sum);

    // Вывод результата
    printf("Result: %.6lf \n", result);

    // Возврат успешного завершения работы программы
    return SUCCESS;
}

