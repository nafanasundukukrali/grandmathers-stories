/**
 * Программа для нахождения максимального из чисел в потоке ввода и вывода его
 * в потоке вывода
 */

#include "find_numbers_average.h"
#include "io_check.h"

// Ошибка в количестве параметров
#define ERROR_INPUT_ARGC 1

#define WAITED_PARAM_COUNT 2

int main(int argc, char **argv)
{
    int return_code = EXIT_SUCCESS;
    FILE *f_input;
    FILE *f_output = stdout;

    if (argc != WAITED_PARAM_COUNT)
    {
        fprintf(f_output, "Error: the argc count is incorrect\n");
        return_code = ERROR_INPUT_ARGC;
    }
    
    if (return_code == EXIT_SUCCESS)
    {
        f_input = check_input_file(argv[1]);

        if (!f_input)
            return_code = ERROR_OPEN_FILE;
    }

    if (return_code == EXIT_SUCCESS)
    {
        return_code = get_min_max_count(f_input, stdout);

        if (fclose(f_input))
            return_code = ERROR_CLOSE_FILE;
    }

    return return_code;
}
