#include "file_funcs.h"

/**
 * Функция для получения размера файла
 */
size_t get_file_size(FILE *file)
{
    if (!feof(file))
        rewind(file);

    size_t counter = 0;
    char buffer[MAX_NAME_LEN + 2];

    while (!feof(file) && fscanf(file, "%s", buffer) == READ_WRITE_COUNT && buffer[0])
        counter++;

    return counter;
}

void put_data_to_file(FILE *file, product_t *value)
{
    fprintf(file, "%s\n", value->name);
    fprintf(file, "%s\n", value->producer);
    fprintf(file, "%u\n", value->price);
    fprintf(file, "%u\n", value->count);
}

short read_line(FILE *file, char *string, size_t lenth)
{
    short return_code = 0;

    if (!fgets(string, lenth + 2, file))
    {
        return_code = ERROR_GET_DATA;
    }
    else
    {
        size_t actual_lenth = strlen(string);

        if (string[actual_lenth - 1] != '\n')
            return_code = ERROR_GET_DATA;
        else
            string[actual_lenth - 1] = '\0';
    }

    return return_code;
}

/**
 * Функция для получения заначения структуры 
 */
short get_products(FILE *file, product_t *products_array, size_t *count)
{
    *count = 0;
    size_t i = 0;
    char buffer[MAX_NAME_LEN + 2];

    rewind(file);

    while (read_line(file, products_array[i].name, MAX_NAME_LEN) == EXIT_SUCCESS)
    {
        *count = *count + 1;

        if (read_line(file, products_array[i].producer, MAX_PRODUCER_LEN) != EXIT_SUCCESS)
            return ERROR_GET_DATA;

        if (read_line(file, buffer, MAX_NAME_LEN) != EXIT_SUCCESS)
            return ERROR_GET_DATA;
        
        if (sscanf(buffer, "%u", &products_array[i].price) != READ_WRITE_COUNT)
            return ERROR_GET_DATA;

        if (read_line(file, buffer, MAX_NAME_LEN) != EXIT_SUCCESS)
            return ERROR_GET_DATA;

        if (sscanf(buffer, "%u", &products_array[i].count) != READ_WRITE_COUNT)
            return ERROR_GET_DATA;

        i++;
    }
    
    if (!feof(file) || !*count)
        return ERROR_INPUT_PARAMS;

    return EXIT_SUCCESS;
}

/**
 * Функция для создания файла с рандомными числами в заданном количестве
 */
short sort_products(FILE *input_file, const char *file_out_name)
{
    short return_code = EXIT_SUCCESS;
 
    product_t products_array[MAX_PRODUCTS_COUNT];

    size_t count = 0;

    return_code = get_products(input_file, products_array, &count);
    
    if (return_code != EXIT_SUCCESS)
        return return_code;

    if (fclose(input_file))
        return ERROR_CLOSE_FILE;

    bubble_sort(products_array, count);
       
    FILE *output_file = fopen(file_out_name, "w");
        
    if (!output_file)
        return ERROR_OPEN_FILE;
       
    for (size_t i = 0; i < count; i++)
        put_data_to_file(output_file, &products_array[i]); 

    if (fclose(output_file))
        return ERROR_CLOSE_FILE;

    return EXIT_SUCCESS; 
}

short check_same_end(const char string[MAX_NAME_LEN + 1], const char *expression)
{
    short return_code = TRUE;
    size_t string_len = strlen(string), expression_len = strlen(expression);
    size_t counter = 0;

    if (string_len >= expression_len)
        while (return_code == TRUE && expression_len-- > 0)
            return_code = string[string_len - ++counter] == expression[expression_len];
    else
        return_code = FALSE;

    return return_code;
}

short print_by_expression(product_t products[MAX_PRODUCTS_COUNT], const size_t count, const char *expression)
{
    size_t was_written = FALSE;
        
    for (size_t i = 0; i < count; i++)
        if (check_same_end(products[i].name, expression))
        {
            put_data_to_file(stdout, &products[i]);
            was_written = TRUE;
        }
    
    return !was_written;
}

/**
 * Функция для получения чисел из файла и записи их в массив
 */
short find_product_by_regexp(FILE *input_file, const char *expression)
{
    short return_code = EXIT_SUCCESS;
 
    if (strlen(expression) <= 0 || strlen(expression) > MAX_NAME_LEN + 2)
        return  ERROR_EXP_LEN;

    size_t count = 0;

    product_t products_array[MAX_PRODUCTS_COUNT];    
    return_code = get_products(input_file, products_array, &count);

    if (fclose(input_file))
        return ERROR_CLOSE_FILE;

    if (return_code == EXIT_SUCCESS)        
        return_code = print_by_expression(products_array, count, expression);

    return return_code;
}

short input_string(char *string, size_t max_lenth)
{
    char buffer[MAX_NAME_LEN + 1];
    
    if (scanf("%s", buffer) != READ_WRITE_COUNT)
        return ERROR_GET_DATA;
    
    strncpy(string, buffer, max_lenth + 1);
    string[strlen(buffer)] = 0;

    return EXIT_SUCCESS;
}

short input_user_product(product_t *user_product)
{
    short return_code = EXIT_SUCCESS;

    printf("Input name: ");

    if (input_string(user_product->name, MAX_NAME_LEN))
        return ERROR_GET_DATA;
    
    printf("Input producer: ");

    if (input_string(user_product->producer, MAX_PRODUCER_LEN))
        return ERROR_GET_DATA;
        
    printf("Input price: ");

    if (scanf("%u", &user_product->price) != READ_WRITE_COUNT)
        return ERROR_GET_DATA;

    printf("Input count: ");

    if (scanf("%u", &user_product->count) != READ_WRITE_COUNT)
        return ERROR_GET_DATA;

    return return_code;
}

short add_new_struct(FILE *input_file, const char *filename)
{
    short return_code = EXIT_SUCCESS;

    size_t count = 0;
    product_t products_array[MAX_PRODUCTS_COUNT];

    return_code = get_products(input_file, products_array, &count);

    if (fclose(input_file) && return_code == EXIT_SUCCESS)
        return ERROR_CLOSE_FILE;

    if (return_code == EXIT_SUCCESS)
    {
        product_t user_product;

        return_code = input_user_product(&user_product);

        if (return_code != EXIT_SUCCESS)
            return return_code;

        add_to_sorted_array(products_array, count, &user_product);

        FILE * file_output = fopen(filename, "w");
	    
        if (!file_output)
        {
            fclose(file_output);

            return ERROR_OPEN_FILE;
        }

        count++;

        for (size_t i = 0; i < count && return_code == EXIT_SUCCESS; i++)
            put_data_to_file(file_output, i + products_array);

        if (fclose(file_output))
            return ERROR_CLOSE_FILE;
    }

    return return_code;
}

/**
 * Функция проверки открытия файла на чтение
 */
FILE *check_input_file(const char *file)
{
    FILE *f_input = fopen(file, "r");
    
    size_t data_size = get_file_size(f_input);

    if (!f_input || !data_size)
    {
        fclose(f_input);
        return NULL;
    }

    return f_input;
}
