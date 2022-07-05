/**
 * Программа для сортировки продуктов, добавлени продукта
 * и нахождения продуктов с окончание, соотвествующему окончанию
 * Метод сортировки пузырьком.
 */

#include "products.h"
#include "file_funcs.h"

/// Ошибка ввода количества параметров
#define ERROR_INPUT_ARGC 2
/// Необходимое количество параметров при вызове команды p или s 
#define PARAM_ST_FT_COUNT 4
/// Необходимое количество параметров при вызове команды c
#define PARAM_AT_COUNT 3

/// Необходимое количество успешно считанные переменных
#define SUCCESS_READ_COUNT 1
/// Необходимое количество байт для строки из одного символа  в массиве строк
#define CHAR_STR_LEN 2

int main(int argc, char **argv)
{
    if (argc < PARAM_AT_COUNT || strlen(argv[1]) != CHAR_STR_LEN || argv[1][1] != 't')
    {
        return ERROR_INPUT_PARAMS;
    }
    else
    {
        FILE *input_file = check_input_file(argv[2]);

        if (!input_file)
        {
            return ERROR_INPUT_PARAMS;
        }
        else if (argc == PARAM_ST_FT_COUNT && argv[1][0] == 's')
        {   
            return sort_products(input_file, argv[3]);
        }
        else if (argc == PARAM_ST_FT_COUNT && argv[1][0] == 'f')
        {
            return find_product_by_regexp(input_file, argv[3]);
        }
        else if (argc == PARAM_AT_COUNT && argv[1][0] == 'a')
        {
            return add_new_struct(input_file, argv[2]);
        }
        else
        {
            fclose(input_file);

            return ERROR_INPUT_PARAMS;
        }
    }
}
