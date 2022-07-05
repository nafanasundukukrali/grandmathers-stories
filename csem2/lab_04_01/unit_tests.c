#include <stdio.h>
#include <string.h>
#include "main.h"

#ifndef UNIT_TESTS_H
#define UNIT_TESTS_H

/**
 * Функция сравнения для вариаций strbrk (проваленный тест)
 */
short compare_strpbrk(const char *str1, const char *str2)
{
    return !(my_strpbrk(str1, str2) == strpbrk(str1, str2));
}

/**
 * Тест, в котором строка str2 - пустая
 */
short strpbrk_not_exist_symbol(void)
{
    return compare_strpbrk("1234", "");
}

/**
 * Тест, в котором делается попытка поиска нулевого символа
 */
short strpbrk_zero_symbol(void)
{
    return compare_strpbrk("1234", "\0");
}

/**
 * Тест, в котором осуществляется поиск одного из нескольких сиволов
 * str2 меньше str1
 */
short strpbrk_less_str2(void)
{
    return compare_strpbrk("acb def", "bc ");
}

/**
 * Тест, в котором осуществляется поиск одного из нескольких символов
 * str1 меньше str2
 */
short strpbrk_less_str1(void)
{
    return compare_strpbrk("ab", "cdefghjkab");
}

/**
 * Тест, в котором осуществляется поиск одного из нескольких символов
 * строки одинаковые
 */
short strpbrk_same_strs(void)
{
    return compare_strpbrk("abc123", "abc123");
}

/**
 * Функция для выполнения тестов для тестирования функции strpbrk
 */
short test_strpbrk(void)
{
    return strpbrk_not_exist_symbol() + strpbrk_zero_symbol() + strpbrk_less_str2() + strpbrk_less_str1() + strpbrk_same_strs();
}

/**
 * Функция для сравнения результатов обработки функций strspn
 */
short compare_strspn(const char *str1, const char *str2)
{
    return !(strspn(str1, str2) == my_strspn(str1, str2));
}

/**
 * Тест, в коотором осуществялется поиск нулевого символа
 */
short strspn_zero_symbol(void)
{
    return compare_strspn("abcde", "\0");
}

/**
 * Тест, в коотором осуществялется поиск пустой строки
 */
short strspn_zero_str2(void)
{
    return compare_strspn("abcde", "");
}

/**
 * Тест, в коотором осуществялется поиск строки больше str1
 */
short strspn_less_str1(void)
{
    return compare_strspn("abcde", "hfejekabcde");
}

/**
 * Тест, в коотором осуществялется поиск в строке где второй вхождение включает больше символов, чем первое
 */
short strspn_second_input_more(void)
{
    return compare_strspn("1999991299", "21");
}

/**
 * функция для тестирования strspn
 */
short test_strspn(void)
{
    return strspn_zero_symbol() + strspn_zero_str2() + strspn_less_str1() + strspn_second_input_more();
}

/**
 * Функция для сравнения результатов обработки функций strcspn
 */
short compare_strcspn(const char *str1, const char *str2)
{
    return !(strcspn(str1, str2) == my_strcspn(str1, str2));
}

/**
 * Тест, в коотором осуществялется поиск нулевого символа
 */
short strcspn_zero_symbol(void)
{
    return compare_strcspn("abcde", "\0");
}

/**
 * Тест, в коотором осуществялется поиск пустой строки
 */
short strcspn_zero_str2(void)
{
    return compare_strcspn("abcde", "");
}

/**
 * Тест, в коотором осуществялется поиск строки больше str1
 */
short strcspn_less_str1(void)
{
    return compare_strcspn("abcde", "hfejekabcde");
}

/**
 * Тест, в коотором осуществялется поиск в строке где второй вхождение включает больше символов, чем первое
 */
short strcspn_second_input_more(void)
{
    return compare_strcspn("1999991299", "21");
}

/**
 * функция для модульного тестирования strcspn
 */
short test_strcspn(void)
{
    return strcspn_zero_symbol() + strcspn_zero_str2() + strcspn_less_str1() + strcspn_second_input_more();
}

/**
 * Функция для сравнения результатов обработки функций strcspn
 */
short compare_strchr(const char *str, int symbol)
{
    return !(my_strchr(str, symbol) == strchr(str, symbol));
}

/**
 * Тест, в коотором осуществялется поиск нулевого символа
 */
short strchr_zero_symbol(void)
{
    return compare_strchr("abcde", '\0');
}

/**
 * Тест, в коотором осуществялется поиск символа в начале стрки
 */
short strchr_start(void)
{
    return compare_strchr("abcde", 'c');
}

/**
 * Тест, в коотором осуществялется поиск символа в середине строки
 */
short strchr_middle(void)
{
    return compare_strchr("1141414999991299", '9');
}

/**
 * Тест, в котором осуществляется поиск символа в конце строки
 */
short strchr_end(void)
{
    return compare_strchr("ab", 'b');
}

/**
 * функция для модульного тестирования strchr
 */
short test_strchr(void)
{
    return strchr_zero_symbol() + strchr_start() + strchr_middle() + strchr_end();
}

/**
 * Функция для сравнения результатов обработки функций strrchr
 */
short compare_strrchr(const char *str, int symbol)
{
    return !(my_strrchr(str, symbol) == strrchr(str, symbol));
}

/**
 * Тест, в коотором осуществялется поиск нулевого символа
 */
short strrchr_zero_symbol(void)
{
    return compare_strchr("abcde", '\0');
}

/**
 * Тест, в коотором осуществялется поиск символа в начале стрки
 */
short strrchr_start(void)
{
    return compare_strchr("abcde", 'a');
}

/**
 * Тест, в коотором осуществялется поиск символа в середине строки
 */
short strrchr_middle(void)
{
    return compare_strchr("1141414999991299", '4');
}


/**
 * Тест, в котором осуществляется поиск символа в конце строки
 */
short strrchr_end(void)
{
    return compare_strchr("ab", 'b');
}

/**
 * функция для модульного тестирования strchr
 */
short test_strrchr(void)
{
    return strrchr_zero_symbol() + strrchr_start() + strrchr_middle() + strrchr_end();
}

/**
 * Функция для выполенния тестирования всех функций
 */
short unit_tests(void)
{
    return test_strpbrk() + test_strspn() + test_strcspn() + test_strchr();
}

#endif
