#! /bin/bash

# Компиляция
gcc -std=c99 -c -Wall -Werror  main.c

# Компоновка
gcc  -o  app.exe  main.o -lm
