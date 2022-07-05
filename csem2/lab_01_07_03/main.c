/**
 * Программа для выисления значений двуз функций, абсолютную и относительную
 * погрешнось по введённому значению и эпсилон.
 */

#include <stdio.h>
#include <math.h>

// Код возврата в случае ошибки
#define ERROR 1
// Код возврата в случае корректного завершения работы программы
#define SUCCESS 0
// Эпсилон для сравнивания вещественных чисел
#define EPSILON 1e-10

double get_f_function_result(double input_value)
{
    /**
     * Функция для вычисления значения функции f
     */
    // Вычисление значения функции в точке
    double f_value = atan(input_value);

    // Вывод результата
    printf("F Result: %.6lf \n", f_value);

    // Возвращение значения
    return f_value;
}

double get_s_function_result(double value_power, double *input_epsilon)
{
    /**
     * Функция для вычисления значения функции s с точностью input_epsilon.
     * value_power как входящий x
     */
    
    // x^2 (во столько раз каждый раз увеличисвается числитель)
    double dif_power = value_power * value_power;
    // Знаменатель
    int div = 1;
    // Минут перед элементом
    int minus = 1;
    // Результат вычисления
    double result = 0;

    // Сравнение модуля каждого нового элемента с епсилон
    while (fabs(value_power / div) > *input_epsilon)
    {
        // Добавление нового элемента в сумму
        result += value_power / div * minus;
        div += 2;
        minus *= -1;
        value_power *= dif_power;
    }

    // Вывод полученного значения в терминал
    printf("S Result: %.6lf \n", result);

    // Возвращение полученной суммы с точностью эпсилон
    return result;
}

void print_delts(double f_value, double s_value)
{
    /**
     * Функция для нахождения и вывода в терпинал значений абсолютной и относительной 
     * погрешностей
     */

    // Абсолютная погрешность
    double delta_absolute = fabs(f_value - s_value);
    // Относительная погрешность
    double delta_relative = delta_absolute / fabs(f_value);
    
    // Вывод полученных значений в терминал
    printf("Delta absolute: %.6lf \n", delta_absolute);
    printf("Delta relative: %.6lf \n", delta_relative);
}

int main(void)
{
    // Входной x и эпсилон
    double input_value, input_epsilon;
    
    // Ввод значений и проверка их на валидность
    printf("Input start value and user epsilon: ");
    if (scanf("%lf%lf", &input_value, &input_epsilon) != 2 || fabs(input_value) > 1 || 
        fabs(input_value) < EPSILON || input_epsilon < EPSILON || 
        input_epsilon > 1)
    {
        printf("Input values are incorrect.\n");
        return ERROR;
    }

    // Вычиление и вывод значения функции s
    double s_value = get_s_function_result(input_value, &input_epsilon);
    
    // Вычисление и вывод значения функции f
    double f_value = get_f_function_result(input_value);

    // Вычисление и вывод погрешностей
    print_delts(f_value, s_value);

    // Корректное завершение работы программы
    return SUCCESS;
}

