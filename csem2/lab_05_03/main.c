/**
 * Программа для нахождения максимального из чисел в потоке ввода и вывода его
 * в потоке вывода
 *
 * Выбранный целочисленный тип - int
 * Метод сортировки - пузырьком
 * Порядок упорядовачивания - в порядке возрастания
 */

#include <string.h>
#include "sort_data.h"
#include "file_funcs.h"

// Ошибка в командах их параметрах
#define ERROR_INPUT_PARAMS 1
// Ошибка ввода количества параметров
#define ERROR_INPUT_ARGC 2
// Необходимое количество параметров при вызове команды p или s 
#define PARAM_R_S_COUNT 3
// Необходимое количество параметров при вызове команды c
#define PARAM_C_COUNT 4

#define SUCCESS_READ_COUNT 1
// Необходимое количество байт для строки из одного символа  в массиве строк

int main(int argc, char **argv)
{
    short return_code = EXIT_SUCCESS;
    size_t buffer;
    FILE *input_file;
    
    if (!((argc == PARAM_R_S_COUNT && strlen(argv[1]) == 1 && 
        (strcmp(argv[1], "p") || strcmp(argv[1], "s"))) 
        || (argc == PARAM_C_COUNT && 
        strlen(argv[1]) == 1 && strcmp(argv[1], "c"))))
    {
        return_code = ERROR_INPUT_ARGC;
    }
    else if (!strcmp(argv[1], "p")) 
    {
        input_file = check_input_file(argv[2], FALSE);

        if (!input_file)
            return_code = ERROR_INPUT_PARAMS;
        else
            return_code = print_numbers_command(input_file);

        if (input_file && fclose(input_file))
            return_code = ERROR_CLOSE_FILE;
    }
    else if (!strcmp(argv[1], "s")) 
    {
        input_file = check_input_file(argv[2], FALSE);

        if (!input_file)
            return_code = ERROR_INPUT_PARAMS;
        else
            return_code = sort_numbers_command(input_file);

        if (input_file && fclose(input_file))
            return_code = ERROR_CLOSE_FILE;
    }
    else if (!strcmp(argv[1], "c")) 
    {
        short result_get = sscanf(argv[2], "%zu", &buffer) != SUCCESS_READ_COUNT;
           
        if (result_get)
            return_code = ERROR_INPUT_PARAMS;
                
        if (return_code == EXIT_SUCCESS)
        {
            if (!(input_file = check_input_file(argv[3], TRUE)))
                return_code = ERROR_INPUT_PARAMS + 4;
            else
                return_code = create_file_command(input_file, buffer);
                    
            if (fclose(input_file))
                return_code = ERROR_CLOSE_FILE;
        }
    }

    return return_code;
}
