/**
 * Программа для вычисления объёма и температуры смеси при известных
 * температурах и объёмов жидкостей в двух ёмкостьях.
 */

#include <stdio.h>

// Код успешного завершения работы программы
#define SUCCESS 0

int main(void)
{
    // Переменные для хранения объёма и температуры жидкости в первом сосуде
    // и объёма и температуры жидкости во втором сосуде
    float first_v, first_t, second_v, second_t;
    
    // Вводятся данные касательно текущих объёмов и температуры жидкости в сосудах
    printf("Input the first volume: ");
    scanf("%f", &first_v);
    printf("Input the first temperature: ");
    scanf("%f", &first_t);
    printf("Input the second volume: ");
    scanf("%f", &second_v);
    printf("Input the second temperature: ");
    scanf("%f", &second_t);
    
    // Вычисление объёма и температуры жидкости в смеси
    // Это суммарный обём первых двух и средняя температура первых двух
    float summa_v = first_v + second_v;
    float average_t = (first_v * first_t + second_v * second_t) / summa_v;

    // Вывод полученных значений в терминал
    printf("Volume: %f \nTemperature:  %f ", summa_v, average_t);

    // Возврат кода успешного завершения выполнения программы
    return SUCCESS;
}

