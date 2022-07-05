/**
 * Программа для сравнения поведения пользовательский строковых функций и функций
 * для работы со строками из стандартной бибилиотеки
 */
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "unit_tests.h"

#define FALSE 0
#define TRUE 1

#ifndef MAIN_H
#define MAIN_H

/**
 * Функция для поиска первого вхождения любого из символа str2 в строке str1
 */
char *my_strpbrk(const char *str1, const char *str2)
{
    short founded = FALSE;

    char *founded_str = (char *) str1, *start_str2 = (char *) str2, *actual_str2 = (char *) str2;

    while (!founded && *founded_str)
    {
        actual_str2 = start_str2;

        while (!founded && *actual_str2 && *actual_str2 != *founded_str)
            actual_str2++;
        
        if (*founded_str == *actual_str2)
            founded = TRUE;

        founded_str++;
    }

    return (founded ? --founded_str : NULL);
}

/**
 * Функция прверки того, что символ char_ есть в строке str
 */
short check_if_symbol_in_str(const char char_, const char *str)
{
    char *pos = (char *) str;
    
    while (*pos && *pos != char_)
        pos++;

    return (*pos && *pos == char_);
}

/**
 * Функция для нахождения длины начального участка str1 содержащего символы str2
 */
size_t my_strspn(const char *str1, const char *str2)
{
    size_t result = 0;
    char *str1_ = (char *) str1;

    while (*str1_ && check_if_symbol_in_str(*str1_, str2))
    {
        str1_++;
        result++;
    }

    return result;
}

size_t my_strcspn(const char *str1, const char *str2)
{
    char *str_ = (char *) str1;
    size_t result = 0;

    while (*str_ && !check_if_symbol_in_str(*str_, str2))
    {
        result++;
        str_++;
    }

    return result;
}

/**
 * Функция нахождения первого вхождения символа в строку
 */
char *my_strchr(const char *str, int symbol)
{
    char *result = NULL;

    for (size_t i = 0; i <= strlen(str) + 1 && result == NULL; i++)
        if (*(str + i) == symbol)
            result = (char *) str + i;

    return result;
}

/**
 * Функция нахождения первого вхождения символа в строку с конца
 */
char *my_strrchr(const char *str, int symbol)
{
    char *result = NULL;

    for (size_t i = strlen(str); i <= strlen(str) && result == NULL; i--)
        if (*(str + i) == symbol)
            result = (char *) str + i;

    return result;
}

#endif

int main(void)
{
    printf("Not passed tests count: %d\n", unit_tests());

    return EXIT_SUCCESS; 
}
