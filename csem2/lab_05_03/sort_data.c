#include "sort_data.h"

/**
 * Перестановка элементов местами массива по указанным указателям
 */
void swap_elements(int *first, int *second)
{
    int buffer = *first;
    *first = *second;
    *second = buffer;
}

/**
 * Сортировка "пузырьком" элементов массива порядке возврастания
 */
void bubble_sort(int *start, int *end)
{
    while (start != end)    
    {
        int *start_new = start;
        
        while (start_new != end)
        {
            if (*start > *start_new)
                swap_elements(start, start_new);

            start_new++;
        }

        start++;
    }
}

/**
 * Сортировка чисел из файла и их перезапись
 */
short sort_numbers_command(FILE *file)
{
    size_t file_size = get_file_size(file);
    int numbers_array[file_size / VALUE_SIZE];
    short result_code = get_numbers_from_file(file, numbers_array, file_size / VALUE_SIZE);
    
    if (result_code == EXIT_SUCCESS)
    {
        bubble_sort(numbers_array, numbers_array + file_size / VALUE_SIZE);

        for (size_t i = 0; i < file_size / VALUE_SIZE; i++)
            put_number_by_pos(file, i, numbers_array[i]);
    }
    
    return result_code;
}
