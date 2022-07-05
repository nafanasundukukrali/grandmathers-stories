#include "products.h"

/**
 * Функция для переставновки двух элементов списка по указателя
 */
void swap_elements(product_t *first, product_t *second)
{
    product_t buffer = *first;
    *first = *second;
    *second = buffer;
}

/**
 * Функция для сортировки списка
 */
void bubble_sort(product_t products[], const size_t count)
{
    for (size_t i = 0; i < count - 1; i++)
        for (size_t j = i + 1; j < count; j++)
            if (products[j].price > products[i].price || 
                (products[j].price == products[i].price && 
                products[j].count > products[i].count))
                swap_elements(&products[j], &products[i]);
}

/**
 * Функция для добалвения продукта в стортированный список
 */
void add_to_sorted_array(product_t products_array[], const size_t count, product_t *user_struct)
{
    size_t i = 0;
    short checking = TRUE, checking_first, checking_second;

    while (i < count && checking)
    {
        checking_first = products_array[i].price > user_struct->price;
        checking_second = products_array[i].price == user_struct->price && products_array[i].count > user_struct->count;
        checking = checking_first || checking_second;	
        
        if (checking)
            i++;
    }
    
    size_t pos = count;
    
    if (i < count)
        swap_elements(&products_array[pos], &products_array[pos - 1]);
    
    while (pos > 0 && --pos > i)
        swap_elements(&products_array[pos], &products_array[pos - 1]);

    swap_elements(&products_array[i], user_struct);
}
