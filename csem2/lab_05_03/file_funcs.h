#ifndef FILEFUNCS_H
#define FILEFUNCS_H

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <time.h>

#define ERROR_OPEN_FILE 11
#define ERROR_GET_NUMBER_BY_POS 12
#define ERROR_FILE_DATA 13
#define ERROR_WRITE_NUMBER_BY_POS 14
#define ERROR_CLOSE_FILE 15

#define FALSE 0
#define TRUE 1

#define READ_WRITE_COUNT 1
#define VALUE_SIZE sizeof(int)

FILE *check_input_file(const char *file, const short create_option);

short print_numbers_command(FILE *file);

short create_file_command(FILE *file, size_t count);

short get_numbers_from_file(FILE *file, int *numbers_array, const size_t size);

short put_number_by_pos(FILE *file, const int pos, const int value);

size_t get_file_size(FILE *file);

#endif
