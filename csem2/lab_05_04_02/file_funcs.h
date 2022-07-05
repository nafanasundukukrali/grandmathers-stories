#ifndef FILE_FUNCS_H
#define FILE_FUNCS_H

#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <ctype.h>
#include <limits.h>
#include <inttypes.h>
#include "products.h"

/// Не найдено ни одно из наименований охожих на выражение
#define ERROR_FOUNDED_EXP 1
/// Не получилось открыть файд
#define ERROR_OPEN_FILE 11
/// Ошибка при чтении данных
#define ERROR_GET_DATA 12
/// Ошибка при записи данных
#define ERROR_FILE_DATA 13
/// ОШибка при записи числа по позиции
#define ERROR_WRITE_NUMBER_BY_POS 14
/// Введённое выражение слшком длинное
#define ERROR_EXP_LEN 15
/// Ошибка закрытия файла
#define ERROR_CLOSE_FILE 16
/// Ошибка в командах их параметрах
#define ERROR_INPUT_PARAMS 53


#define FALSE 0
#define TRUE 1

// Количество данных для прочтения
#define READ_WRITE_COUNT 1
// Количество полей в структуре
#define VALUE_SIZE 4

FILE *check_input_file(const char *file);

short add_new_struct(FILE *input_file, const char *filename);

short find_product_by_regexp(FILE *input_file, const char *expression);

short sort_products(FILE *input_file, const char *file_out_name);

size_t get_file_size(FILE *file);

#endif
