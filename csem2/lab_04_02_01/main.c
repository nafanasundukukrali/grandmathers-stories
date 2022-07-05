/**
 * Программа для разделения вхдной строки на слова и вывода слов в лексиграфическом порядке
 */

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

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
// Минимальная длина строки
#define MIN_STR_LEN 1
// Ограничение для значений символов из таблицы ascii
#define MAX_ASCII_CODE 127
// Нулеой символ
#define NULL_SYMBOL 0

/**
 * Функция для ввода строки
 */
short read_line(char *string)
{
    short return_code = EXIT_SUCCESS;
    int buffer;
    size_t i = 0;

    printf("Input stringing: ");
    
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
    return ((ispunct(*element) || isspace(*element) || isblank(*element) || *element == '\0') ? TRUE : FALSE); 
}

/**
 * Функция для "вырезки" слова из строки и добавления его в строку word
 */
void get_word_from_string(char *start, char *end, char *word)
{
    while (start != end)
    {
        *word = *start;
        word ++;
        start ++;
    }

    *word = NULL_SYMBOL;
}

/**
 * Функция для деления строки на слова и записи их в массив
 */
short split_string_into_words(char *string, char array[][MAX_WORD_LEN + 1], size_t *array_len)
{
    char *start_position = NULL, *end_position = string - 1;
    *array_len = 0;
    short return_code = EXIT_SUCCESS, end_check = FALSE;
    
    // Обход всех символов строки до нулевого символа   
    while (!end_check && return_code == EXIT_SUCCESS) 
    {
        end_position ++;
        
        // Проверка того, что найден позиция знака припянания
        if (check_split_element(end_position) && start_position != NULL && end_position - start_position > 0)
            if ((end_position - start_position) >= MAX_WORD_LEN + 1)
            {
                // Найдено слово, в котором количество символом больше максимальной длины слова
                return_code = ERROR_WORD_LEN;
            }
            else
            {
                // Получение слова
                get_word_from_string(start_position, end_position, array[*array_len]);
                start_position = NULL;
                *array_len += 1;
            }
	// Стартовая позиция каждый раз отсчитывается от первой встречи эндом символа цифры/буквы после 
	// последнего присваивания
        else if (start_position == NULL && !check_split_element(end_position))
            start_position = end_position;

        end_check = *end_position == NULL_SYMBOL;
    }
    
    // Проврека, что массив не пустой
    if (!*array_len)
        return_code = ERROR_WORD_COUNT;

    return return_code;
}

/**
 * Функция для сравнения двух слов
 */
short compare_words(char *word1, char *word2)
{
    while (*word2 && *word1 && *word1 == *word2)
    {
        word1++;
        word2++;
    }

    return (*word1 == *word2);
}

/**
 * Функция для удаления строки из массива
 */
void delete_word(char array[][MAX_WORD_LEN + 1], size_t position, size_t *array_len)
{
    position--;

    while (++position < *array_len - 1)
        strncpy(array[position], array[position + 1], MAX_WORD_LEN);

    *array_len -= 1;
}

/**
 * Функция для удаления не уникальных строк из массива
 */
void find_and_del_same_words(char array[][MAX_WORD_LEN + 1], size_t *array_len)
{
    size_t position = 0;

    while (position < *array_len - 1)
    {
        size_t i = position + 1;
      
        while (i < *array_len)
            if (compare_words(array[i], array[position]))
                delete_word(array, i, array_len);
            else
                i++;

        position++;
    }
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
 * Функция для сортировки слов в массиве пузырьком
 */
void bubble_sort_array(char array[][MAX_WORD_LEN + 1], const size_t array_len)
{
    for (size_t i = 0; i < array_len - 1; i++)
        for (size_t j = 0; j < array_len - 1; j++)
            if (strncmp(array[j], array[j + 1], MAX_WORD_LEN) > 0)
                swap_words_in_array(array, j, j + 1);
}

int main(void)
{
    // Код возврата программы
    short exit_code = EXIT_SUCCESS;
    // Входная строка
    char input_string[MAX_STR_LEN + 1];
    // Длина массива
    size_t array_len;
    // Целевой массив
    char array[MAX_STR_LEN][MAX_WORD_LEN + 1];
    
    // Ввод строки
    exit_code = read_line(input_string);
    // Нахождение строк и заполнение массива
    exit_code = (exit_code == EXIT_SUCCESS ? split_string_into_words(input_string, array, &array_len) : exit_code);
    
    // Удаление лишних слови сортировка, вывод массива
    if (exit_code == EXIT_SUCCESS)
    {
        find_and_del_same_words(array, &array_len);
        bubble_sort_array(array, array_len);
        printf("Result: ");

        for (size_t i = 0; i < array_len; i++)
            printf("%s ", array[i]);
    }

    return exit_code;
}
