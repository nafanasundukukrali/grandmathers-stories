/**
 * Программа для нахождения максимального из чисел в потоке ввода и вывода его
 * в потоке вывода
 */

#include <stdio.h>
#include <stdlib.h>
#include "process.h"

int main(void)
{
    int return_code = EXIT_SUCCESS;

    return_code = process(stdin, stdout);

    return return_code;
}
