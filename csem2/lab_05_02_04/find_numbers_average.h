#ifndef FIND_NUMBERS_AVERAGE_H
#define FIND_NUMBERS_AVERAGE_H

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/// Количетсво корректно прочтённых данных
#define COUNT_CORRECT_READ 1
/// Эпсилон
#define EPSILON 1e-8

/// Ошибка минимума количества чисел
#define ERROR_NUMBERS_COUNT 2
/// Ошибка прочтения знчения
#define ERROR_NUMBERS_VALUES 3

int get_min_max_count(FILE *f_input, FILE *f_output);

#endif
