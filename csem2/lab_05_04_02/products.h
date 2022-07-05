#ifndef PRODUCTS_H
#define PRODUCTS_H

#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <limits.h>

#define TRUE 1

// Максимальная длина имени продута
#define MAX_NAME_LEN 30
// Максимальное наименование производителя
#define MAX_PRODUCER_LEN 15
// Максимальное количество продуктов
#define MAX_PRODUCTS_COUNT 500

/**
 * Структуры продукс
 * name - имя продукта
 * producer - производитель
 * price - цена за единицу товара
 * count - количество товаров
 */
typedef struct 
{
    char name[MAX_NAME_LEN + 2];
    char producer[MAX_PRODUCER_LEN + 2];
    uint32_t price;
    uint32_t count;
} product_t;

void bubble_sort(product_t products[], const size_t count);

void add_to_sorted_array(product_t products_array[], const size_t count, product_t *user_struct);

#endif
