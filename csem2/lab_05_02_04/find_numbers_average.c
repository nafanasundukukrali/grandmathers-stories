#include "find_numbers_average.h"

/**
 * Поиск минимума и максимума
 */
int find_max_and_min(FILE *f_input, float *max, float *min)
{
    int return_code = EXIT_SUCCESS;
    float value;
    int numbers_count = 0, max_count = 0, min_count = 0;
    
    rewind(f_input);

    if (fscanf(f_input, "%f", &value) != COUNT_CORRECT_READ)
    {
        return_code = ERROR_NUMBERS_COUNT;
    }
    else
    {
        *min = value;
        *max = value;
        numbers_count++;
        max_count = 1;
        min_count = 1;
    }

    while (return_code == EXIT_SUCCESS && fscanf(f_input, "%f", &value) == COUNT_CORRECT_READ)
    {
        if (value > *max)
        {
            *max = value;
            max_count = 1;
        }
        else if (value < *min)
        {
            *min = value;
            min_count = 1;
        }
        else if (fabs(value - *max) < EPSILON)
        {
            max_count++;
        }
        else if (fabs(value - *min) < EPSILON)
        {
            min_count++;
        }

        numbers_count++;
    }
    
    if (return_code == EXIT_SUCCESS && numbers_count < 3)
        return_code = ERROR_NUMBERS_COUNT;

    if (return_code == EXIT_SUCCESS && (min_count != 1 || 
        max_count != 1 || fabs(*max - *min) < EPSILON))
        return_code = ERROR_NUMBERS_VALUES;

    return return_code;
}

/**
 * Писк количества и суммы между минимумом и максимумом
 */
void find_sum_and_count_between(FILE *f_input, const float min, const float max, float *sum, int *count)
{
    float value;
    *sum = 0;
    *count = 0;

    rewind(f_input);
    
    while (fscanf(f_input, "%f", &value) == COUNT_CORRECT_READ && 
        fabs(value - min) > EPSILON && fabs(value - max) > EPSILON);

    while (fscanf(f_input, "%f", &value) == COUNT_CORRECT_READ && 
        fabs(value - min) > EPSILON && fabs(value - max) > EPSILON)
    {
        *count += 1;
        *sum += value;	
    }
}

/**
 * Функция для нахождения количества чисел между минимумом и максимумом
 *  после их нахождения
 */
int get_min_max_count(FILE *f_input, FILE *f_output)
{
    int return_code = EXIT_SUCCESS, count = 0;
    float max = 0, min = 0, sum = 0;

    return_code = find_max_and_min(f_input, &max, &min);
    
    if (return_code == EXIT_SUCCESS)
        find_sum_and_count_between(f_input, max, min, &sum, &count);

    if (return_code == EXIT_SUCCESS && count == 0)
        return_code = ERROR_NUMBERS_VALUES;
    
    if (return_code == EXIT_SUCCESS && min < max)
        fprintf(f_output, "Result: %.6f\n", sum / count);
    else if (return_code != EXIT_SUCCESS)
        fprintf(f_output, "Error: there less number count than two or incorrect inputs\n");
    
    return return_code;
}
