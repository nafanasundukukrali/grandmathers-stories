/**
 * Программа для разделения вхдной строки на слова и формирования новой строки со словами в обратном
 * порядке и уникальными буквами
 */

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// Кды возврата ошибочного завершения работыы программы
// Длина стороки меньше минимлаьного значения или больше максимального
#define ERROR_STR_LEN 1
// Ошибка длины строки, которая идёт как негативный тес
#define ERROR_STR_LEN_NOT_CRITIC 2
// Был встречен неизвестный символ в строке
#define ERROR_UNKNOWN_SYMBOL 3
// Количество слов равно нулю
#define ERROR_WORD_COUNT 4

#define TRUE 1
#define FALSE 0

// максимальное количество символов с строке
#define MAX_STR_LEN 256
// Количество слов
#define WORD_COUNT 1
// Минимальная длина строки
#define MIN_STR_LEN 1
// Ограничение для значений символов из таблицы ascii
#define MAX_ASCII_CODE 127
// Нулевой символ
#define NULL_SYMBOL 0
// Симолы в начале числа
#define START_SYMBOLS "+-."

/**
 * Функция для ввода строки
 */
short read_line(char *string)
{
    short return_code = EXIT_SUCCESS;
    int buffer;
    size_t i = 0;

    // Ввод символа с проверкой на то, что он в таблице символов и не равен концу файла/перехода на следующую строку
    while (return_code == EXIT_SUCCESS && (buffer = getchar()) != '\n' && buffer != EOF && i < MAX_STR_LEN)
        if (buffer <= MAX_ASCII_CODE)
            string[i++] = buffer;
        else
            return_code = ERROR_UNKNOWN_SYMBOL;

    // Проверка того, что после символов в количестве максимальной длины строки нет ещё сиволов и длина строки
    // больше минимального значения
    if (return_code == EXIT_SUCCESS && ((getchar() != EOF && i >= MAX_STR_LEN)))
        return_code = ERROR_STR_LEN;
    else if (return_code == EXIT_SUCCESS && i < MIN_STR_LEN)
        return_code = ERROR_STR_LEN_NOT_CRITIC;
    else if (return_code == EXIT_SUCCESS)
        string[i] = NULL_SYMBOL;

    return return_code;
}

/**
 * Функция для проверки того, что символ сожержится в строке
 */
short check_symbol_in_string(char symbol, char *word)
{
    size_t i = 0;
    short return_code = FALSE;

    while (i < strlen(word) && !return_code)
    {
        return_code = word[i] == symbol;
        i++;
    }

    return return_code;
}

/**
 * Функция для деления строки на слова и записи их в массив
 */
short split_string_into_words(char *string, char array[][MAX_STR_LEN + 1])
{
    size_t array_len = 0;
    short return_code = EXIT_SUCCESS;
    size_t start_position = 0;

    while (string[start_position] && isspace(string[start_position]))
        start_position++;
    
    while (string[start_position] && !isspace(string[start_position]))
    {
        array[0][array_len] = string[start_position];
        start_position++;
        array_len++;
    }

    while (string[start_position] && isspace(string[start_position]))
        start_position++;
    
    if (start_position > MAX_STR_LEN)
        return_code = ERROR_STR_LEN;

    if (return_code == EXIT_SUCCESS && start_position < strlen(string))
        return_code = ERROR_WORD_COUNT;

    if (return_code == EXIT_SUCCESS)
        array[0][array_len] = NULL_SYMBOL;

    return return_code;
}

/**
 * Проверка экпоненциального вида
 */
short check_exp_format(char *word, size_t stop_position, short from_dot)
{
    size_t return_code = TRUE, counter = 0;
    char *start = "+-";
    
    if (!from_dot)
        return_code = isdigit(word[stop_position - 1]);

    stop_position++;

    return_code = return_code && stop_position < strlen(word) && (check_symbol_in_string(word[stop_position], start) || isdigit(word[stop_position]));
    
    while (return_code && ++stop_position < strlen(word) && isdigit(word[stop_position]))
        counter++;

    return (return_code && (stop_position == strlen(word)) && isdigit(word[stop_position - 1]));
}

/**
 * Функция для проверки вещественного числа не экспоненциального вида
 */
short check_dot_format(char *word, size_t stop_position)
{
    size_t counter = 0;

    while (stop_position < strlen(word) && isdigit(word[++stop_position]))
        counter++;

    short checking_dot = (!(!isdigit(word[stop_position - 2]) && word[stop_position - 1] == '.'));
    checking_dot = checking_dot && ((stop_position == strlen(word) || (word[stop_position] == 'e' || word[stop_position] == 'E') ? check_exp_format(word, stop_position, TRUE) : FALSE));
    
    return checking_dot;
}

/**
 * Функция для формирования новой выходной строки
 */
short check_number(char *word)
{
    short return_code = TRUE;
    size_t i = 0, counter = 0;
    char *start = START_SYMBOLS;

    return_code = check_symbol_in_string(word[i], start) || isdigit(word[i]);
    short there_was_dot_start = !(word[i] == '.');
    
    while (return_code && i < strlen(word) && isdigit(word[++i]))
        counter++;
    
    if (return_code && i < strlen(word))
        if (word[i] == '.' && there_was_dot_start && (word[i - 1] == '+' || word[i - 1] == '-' || isdigit(word[i - 1])))
            return_code = check_dot_format(word, i);
        else if ((word[i] == 'e' || word[i] == 'E'))
            return_code = check_exp_format(word, i, FALSE);
        else
            return_code = FALSE;
    else if (strlen(word) == 1 && check_symbol_in_string(word[0], start))
        return_code = FALSE;

    return return_code;
}

int main(void)
{
    // Код возврата программы
    short exit_code = EXIT_SUCCESS;
    // Входная строка
    char input_string[MAX_STR_LEN + 1];

    // Целевой массив
    char array[MAX_STR_LEN][MAX_STR_LEN + 1];
    
    exit_code = read_line(input_string);

    exit_code = (exit_code == EXIT_SUCCESS ? split_string_into_words(input_string, array) : exit_code);
    
    // Проверка того, что единственное слово в массиве - число 
    if (exit_code == EXIT_SUCCESS)
    {
        printf("%s", (check_number(array[0]) ? "YES" : "NO"));
    }   
    else if (exit_code != ERROR_STR_LEN)
    {
        printf("NO");
        exit_code = EXIT_SUCCESS;
    }

    return exit_code;
}
