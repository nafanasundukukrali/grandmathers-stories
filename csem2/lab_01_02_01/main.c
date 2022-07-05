/**
 * Программа для нахождения площади равнобедренной  трапеции по основаниям и углу между боковой стороной и большим
 * основанием.
 */

#include <stdio.h>
#include <math.h>

// Пи
#define PI 3.14159265
// Развёрнутый угол
#define UNFOLDED_ANGLE 180

// Код правильного завершения выполенния программы
#define SUCCESS 0

float max(float a, float b)
{
/**
 * Функция для нахождения максимального из двух чисел.
 */
    if (a >= b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

float min(float a, float b)
{
/**
 * Функция для нахождения минимального из двух чисел.
 */
    if (a <= b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

int main(void)
{	
    // Переменные для оснований
    float side_a, side_b;
    // Переменная для угла
    float corner_fi;

    // Вввод оснований и величины угла в градусах
    printf("Input side  a: ");
    scanf("%f", &side_a);
    printf("Input side  b: ");
    scanf("%f", &side_b);
    printf("Input corner  fi: ");
    scanf("%f", &corner_fi);

    // Основные математические вычисления
    // Тангенс угла
    double tg_fi = tan(corner_fi * PI / UNFOLDED_ANGLE);
    // Нахождение высоты трапеции
    double height = tg_fi * (max(side_a, side_b) - min(side_a, side_b)) / 2; 
    // Нахождение площади трапеции
    double square = height * (side_a + side_b) / 2;

    // Вывод значения площади трапеции
    printf("Square: %lf\n", square);

    // Возрат кода корретного завершения выполнения программы
    return SUCCESS;
}

