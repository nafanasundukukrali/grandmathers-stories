/**
 * Программа для разделения вхдной строки на слова и формирования новой строки со словами в обратном
 * порядке и уникальными буквами
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Коды возврата ошибочного завершения работыы программы
// Длина стороки меньше минимлаьного значения или больше максимального
#define ERROR_STR_LEN 1
// Длина слова больше максимального значения
#define ERROR_WORD_LEN 2
// Был встречен неизвестный символ в строке
#define ERROR_UNKNOWN_SYMBOL 3
// Количество слов равно нулю
#define ERROR_WORD_COUNT 4

#define TRUE 1
#define FALSE 0

// максимальное количество символов с строке
#define MAX_STR_LEN 256
// Максимальное количество символов в слове
#define MAX_WORD_LEN 16
// Минимальное количество слов
#define MIN_WORD_COUNT 2
// Минимальная длина строки
#define MIN_STR_LEN 1
// Ограничение для значений символов из таблицы ascii
#define MAX_ASCII_CODE 127
// Нулевой симбол
#define NULL_SYMBOL 0
// Символы разделения для строки
#define PUNCTUATION_SYMBOLS ",;:-.!? "
// Код пробела в ascii
#define SPACE 32

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
    if (return_code == EXIT_SUCCESS && ((getchar() != EOF && i >= MAX_STR_LEN) || i < MIN_STR_LEN))
        return_code = ERROR_STR_LEN;
    else
        string[i] = NULL_SYMBOL;

    return return_code;
}

/**
 * Функция для прверки является ли символ разделителем (и что не тире в слове)
 */
short check_split_element(const char *element)
{
    return ((ispunct(*element) || isspace(*element) || isblank(*element) || !*element) ? TRUE : FALSE); 
}

/**
 * Функция для деления строки на слова и записи их в массив
 */
short split_string_into_words(char *string, char array[][MAX_WORD_LEN + 1], size_t *array_len)
{
    char string_symbols[] = PUNCTUATION_SYMBOLS;
    short return_code = EXIT_SUCCESS;
    char *buffer = strtok(string, string_symbols);
    
    while (buffer && return_code == EXIT_SUCCESS)
    {
        if ((strlen(buffer) > 1 && strlen(buffer) <= MAX_WORD_LEN) || (strlen(buffer) == 1 && !check_split_element(buffer)))
        {
            strncpy(array[*array_len], buffer, strlen(buffer));
            array[*array_len][strlen(buffer)] = NULL_SYMBOL;
            *array_len += 1;
        }
        
        if (strlen(buffer) > MAX_WORD_LEN)
            return_code = ERROR_WORD_LEN;
        else
            buffer = strtok(NULL_SYMBOL, string_symbols);
    }

    // Проврека, что массив не пустой
    if (return_code == EXIT_SUCCESS && *array_len < MIN_WORD_COUNT)
        return_code = ERROR_WORD_COUNT;

    return return_code;
}

/**
 * Функция для удаления символа из строки на позиции position
 */
void delete_charecter(char *word, size_t position)
{
    size_t i = 0;

    for (i = position; i < strlen(word) - 1; i++)
        word[i] = word[i + 1];

    word[i] = NULL_SYMBOL;
}

/**
 * Функция поиска повторов букв и удаления их
 */
void clear_same_charecters(char *word)
{
    size_t position = -1;

    while (++position < strlen(word))
    {
        size_t i = -1;
        short same = FALSE;

        while (same == FALSE && ++i < position)
            if (word[i] == word[position])
            {
                delete_charecter(word, position);
                same = TRUE;
                position--;
            }
    }
}

/**
 * Функция для прохода по всем словам в массиве и удаления из них повторений букв
 */
void find_and_del_same_words_chr(char array[][MAX_WORD_LEN + 1], size_t *array_len)
{
    size_t position = -1;

    while (++position < *array_len)
        clear_same_charecters(array[position]);
}

/**
 * Функция для перестановки двух слов в массиве
 */
void swap_words_in_array(char array[][MAX_WORD_LEN + 1], const size_t position1, const size_t position2)
{
    char buffer[MAX_WORD_LEN];
    strncpy(buffer, array[position1], MAX_WORD_LEN);
    strncpy(array[position1], array[position2], MAX_WORD_LEN);
    strncpy(array[position2], buffer, MAX_WORD_LEN);
}

/**
 * Фукнция для вставки слова в строку
 */
void input_word_into_string_start(char *string, const char *word)
{
    size_t i;
    
    for (i = 0; i < strlen(word); i++)
        string[i] = word[i];

    string[i] = NULL_SYMBOL;
    string[i + 1] = NULL_SYMBOL;
}

/**
 * Функция для формирования новой выходной строки
 */
short make_new_string(char array[][MAX_WORD_LEN + 1], const size_t array_len, char *new_string)
{
    short return_code = EXIT_SUCCESS;
    char *last_word = array[array_len - 1];
    size_t result_count = 0;
    size_t start_position = array_len - 2;
    
    while (start_position < array_len && !strncmp(array[start_position], last_word, MAX_WORD_LEN))
        start_position--;    
    
    if (start_position < array_len)
    {
        result_count++;
        input_word_into_string_start(new_string, array[start_position]);
    }

    for (size_t i = start_position - 1; i < array_len; i--)
        if (strncmp(array[i], last_word, MAX_WORD_LEN))
        {
            result_count++;
            new_string[strlen(new_string) + 1] = NULL_SYMBOL;
            new_string[strlen(new_string)] = SPACE;
            strncat(new_string, array[i], strlen(array[i]));
            new_string[strlen(new_string)] = NULL_SYMBOL;
        }

    if (!result_count)
        return_code = ERROR_WORD_COUNT;

    return return_code;
}

int main(void)
{
    // Код возврата программы
    short exit_code = EXIT_SUCCESS;
    // Входная строка
    char input_string[MAX_STR_LEN + 1];
    // Длина массива
    size_t array_len = 0;

    // Целевой массив
    char array[MAX_STR_LEN][MAX_WORD_LEN + 1];
    
    exit_code = read_line(input_string);
    exit_code = (exit_code == EXIT_SUCCESS ? split_string_into_words(input_string, array, &array_len) : exit_code);
    
    //    Удаление лишних слови сортировка, вывод массива
    if (exit_code == EXIT_SUCCESS)
    {
        find_and_del_same_words_chr(array, &array_len);
        char new_string[MAX_STR_LEN];
        exit_code = make_new_string(array, array_len, new_string);
        
        if (exit_code == EXIT_SUCCESS)
            printf("Result: %s\n", new_string);
    }

    return exit_code;
}
