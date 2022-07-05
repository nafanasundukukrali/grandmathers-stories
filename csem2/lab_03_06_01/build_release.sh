#! /bin/bash

# Компиляция
gcc -std=c99 -c -Wall -Werror -Wpedantic -Wextra -Wfloat-equal -Wfloat-conversion -Wvla -O3  main.c

# Компоновка
gcc  -o  app.exe  main.o -lm
