#ifndef IO_CHECK_H
#define IO_CHECK_H

#include <stdio.h>
#include <stdlib.h>

// Ошибка открытия файла
#define ERROR_OPEN_FILE 1
/// Ошибка закрытия файла
#define ERROR_CLOSE_FILE 5

FILE *check_input_file(char *file);

#endif
