#include "io_check.h"

/**
 * Функция проверки открытия файла на чтение
 */
FILE *check_input_file(char *file)
{
    FILE *f_input = fopen(file, "r");

    return f_input;
}
