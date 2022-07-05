#include "file_funcs.h"

/**
 * Функция для получения размера файла
 */
size_t get_file_size(FILE *file)
{
    fseek(file, 0, SEEK_END);

    size_t file_size = ftell(file);

    return file_size;
}

/**
 * Функция для получения псевдорандомного целого числа типа int
 */
int get_next_number()
{
    srand(time(NULL));

    return rand();
}

/**
 * Функция для затирания числа на позиции и записи нового
 */
short put_number_by_pos(FILE *file, const int pos, const int value)
{
    int return_code = fseek(file, pos * VALUE_SIZE, SEEK_SET);
    
    if (return_code == EXIT_SUCCESS)
        fwrite(&value, VALUE_SIZE, READ_WRITE_COUNT, file);
    else
        return_code = ERROR_WRITE_NUMBER_BY_POS;

    return return_code;
}

/**
 * Функция для получения числа по позиции
 */
short get_number_by_pos(FILE *file, const int pos, int *value)
{
    int return_code = fseek(file, pos * VALUE_SIZE, SEEK_SET);

    if (return_code != EXIT_SUCCESS || fread(value, VALUE_SIZE, READ_WRITE_COUNT, file) != READ_WRITE_COUNT)
        return_code = ERROR_GET_NUMBER_BY_POS;
    
    return return_code;
}

/**
 * Функция для создания файла с рандомными числами в заданном количестве
 */
short create_file_command(FILE *file, size_t count)
{
    short return_code = EXIT_SUCCESS;

    for (size_t i = 0; i < count && return_code == EXIT_SUCCESS; i++)
        return_code = put_number_by_pos(file, i, get_next_number() / (i % 5 + 1));

    return return_code; 
}

/**
 * Функция для получения чисел из файла и записи их в массив
 */
short get_numbers_from_file(FILE *file, int numbers_array[], const size_t size)
{
    short result_code = EXIT_SUCCESS;

    rewind(file);

    for (size_t i = 0; i < size && result_code == EXIT_SUCCESS; i++)
        result_code = get_number_by_pos(file, i, numbers_array + i);

    return result_code;
}

/**
 * Функция для вывода чисел из файла в терминал
 */
short print_numbers_command(FILE *file)
{
    size_t file_size = get_file_size(file);
    int numbers_array[file_size / VALUE_SIZE];

    short result_code = get_numbers_from_file(file, numbers_array, file_size / VALUE_SIZE);

    for (size_t i = 0; i < file_size / VALUE_SIZE && result_code == EXIT_SUCCESS; i++)
        printf("%d ", numbers_array[i]);

    return result_code;
}

/**
 * Функция проверки открытия файла на чтение
 */
FILE *check_input_file(const char *file, const short create_option)
{
    FILE *f_input;

    if (create_option)
        f_input = fopen(file, "wb");
    else
        f_input = fopen(file, "rb+");

    if (f_input && !create_option)
    {
        size_t file_size = get_file_size(f_input);

        if (!file_size || file_size % VALUE_SIZE != 0)
        {
            fclose(f_input);
            f_input = NULL;
        }
    }
    else if (!f_input)
    {
        fclose(f_input);
        f_input = NULL;
    }

    return f_input;
}
