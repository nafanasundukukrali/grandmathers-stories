/**
 * Программа для определения положения точки относительно прямой по кооринатам интересующей
 * точки и коррдинатам двух точек, расположенных на прямой
 */

#include <stdio.h>
#include <stdbool.h>
#include <math.h>

// Код корректного завершения работы программы
#define SUCCESS 0
// Код ошибки для первой точки
#define FIRST_DOT_ERROR 1
// Код ошибки для второй точки
#define SECOND_DOT_ERROR 2
// Код ошибки для третьей точки
#define THIRD_DOT_ERROR 3
// Код ошибки, если прямая вертикальная и точка не лежит на ней
#define VERTICAL_LINE_ERROR 4

// Точка расположена под прямой
#define UNDER_THE_LINE 2
// На прямой
#define ON_THE_LINE 1
// ПОд прямой
#define UPPER_THE_LINE 0

// Эпсилон для сравнения вещественных чисел
#define EPSILON 1E-8

void make_first_dot_the_lowerst(float *x1, float *y1, float *x2, float *y2)
{
    /**
     * Функция для расположения координат точек в порядке возрастания оординаты.
     * Параметры:
     * x1, у1 - координаты первой введённой точки
     * х2, у2 - координаты второй введённой точки
     */
    // Если координата оординат второй точки меньше, то происходит замена соотвествующих координат
    if (*y1 > *y2)
    {
        // Временный буфер для замены значений
        float buffer = *y1;

        *y1 = *y2;
        *y2 = buffer;
        buffer = *x2;
        *x2 = *x1;
        *x1 = buffer;
    }
}

float get_oblique_product(float x1, float y1, float x2, float y2, float xp, float yp)
{
    /**
     * Функция для взятия косого произведения по координатам трёх точек
     * Параметры: координаты трёх точек в декартовой системе координат
     * Выходные данные: косое произведение
     */
    // Вычисление координат первого вектора
    float vector_a_x = xp - x1;
    float vector_a_y = yp - y1;

    // Вычисление координат второго вектора
    float vector_b_x = x2 - x1;
    float vector_b_y = y2 - y1;

    // Вычисление самого косого произведения полученных векторов
    float product = vector_b_x * vector_a_y - vector_a_x * vector_b_y;
    
    // Возврат значения косого произведения
    return product;
}

int main(void)
{
    // Координаты первой точки на прямой
    float x1, y1;
    // Координаты второй точки на прямой
    float x2, y2;
    // Координаты интересующей точки
    float xp, yp;

    // Булевая переменная для отслеживания корректности ввода координат
    int error_checking = SUCCESS;

    // Ввод координат первой точки
    printf("Input co-ordinates of the first line dot splited by enter: ");
    if (scanf("%f%f", &x1, &y1) != 2)
        error_checking = FIRST_DOT_ERROR;
    // Ввод координат второй точки
    printf("Input co-ordinates of the second line dot splited by enter: ");
    if (scanf("%f%f", &x2, &y2) != 2)
        error_checking = SECOND_DOT_ERROR;
    // Ввод координат интересующей точки
    printf("Input co-ordinates of te interesting dot splited by enter: ");
    if (scanf("%f%f", &xp, &yp) != 2)
        error_checking = THIRD_DOT_ERROR;
    
    // Проверка коорректности ввода координат точек
    if (error_checking != SUCCESS)
    {
        printf("Input values are incorrected.\n");
        return error_checking;
    }

    // Проверка того, что прямая не вертикальная или точка не лежит на этой прямой
    if (error_checking || (fabsf(x1 - x2) < EPSILON && fabsf(x1 - xp) > EPSILON))
    {
        printf("Input values are incorrected.\n");
        return VERTICAL_LINE_ERROR;
    }

    // Расположение точек по возрастаю оординаты
    make_first_dot_the_lowerst(&x1, &y1, &x2, &y2);
    // Вычисление косого произведения
    float product = get_oblique_product(x1, y1, x2, y2, xp, yp);
    
    // Вывод результата оценки распожения точки отнсоительно прямой
    if (product < 0)
    {
        // Ниже прямой
        printf("Result: %d\n", UNDER_THE_LINE);
    }
    else if (fabsf(product) < EPSILON)
    {
        // Находится на прямой
        printf("Result: %d\n", ON_THE_LINE);
    }
    else
    {
        // Над прямой
        printf("Result: %d\n", UPPER_THE_LINE);
    }

    // Возврата кода успешного выполнения работы программы
    return SUCCESS;
}

