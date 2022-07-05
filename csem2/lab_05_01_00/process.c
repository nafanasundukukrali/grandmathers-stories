#include "process.h"

/**
 * Функция для считывания целых чисел из файла f, нахождения
 * максимального из чисел и записи его в файл f_output
 */
int process(FILE *f, FILE *f_output)
{
    int return_code = EXIT_SUCCESS;

    int value = -1, max_value = -1, value_last = 1;

    fprintf(f_output, "Input vals: ");

    while (fscanf(f, "%d", &value) == CORRECT_COUNT_READ)
    {
        if (value_last < 0 && value > max_value)
            max_value = value;
        
        value_last = value;
    }

    if (return_code == EXIT_SUCCESS && (max_value <= 0))
    {
        fprintf(f_output, "Error: result val is inccorect\n");
        return_code = ERROR_VALUE_RES;
    }
    else
    {
        fprintf(f_output, "Result: %d\n", max_value);
    }

    return return_code;
}
