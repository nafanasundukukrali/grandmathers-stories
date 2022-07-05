#ifndef PROCCESS_H
#define PROCCESS_H

#include <stdio.h>
#include <stdlib.h>

// Ошибка нахождения максимального значения среди чисел
#define ERROR_VALUE_RES 1
// Ошибка ввода
#define ERROR_INPUT 2

// Количество корректно считанных значений
#define CORRECT_COUNT_READ 1

int process(FILE *f, FILE *f_output);

#endif
