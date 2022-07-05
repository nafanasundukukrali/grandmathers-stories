#! /bin/bash

# Создание объектного файла с 3 уровнем отладочной информации
gcc -std=c99 -c -Wall -Werror -Wpedantic -Wextra -Wfloat-equal -Wfloat-conversion -Wvla  main.c -g3

# Компоновка
gcc  -o app.exe  main.o -lm 
