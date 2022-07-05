#! /bin/bash
# Конкина А. Н., ИУ7-23Б
# Скрипт, принимающий в качетсве аргументов файл для подменны входного потока,
# И файл ключей к программе при необходимости

# Valgrind
USE_VALGRIND=false

# Проверка существования первого файла
if [ -z "$1" ] || ! [ -f "$1" ]; then
    exit 2
fi

# Проверка наличия файла с параметрами и вызов команды
if [ -n "$3" ] && [ -f "$3" ]; then
    param=$(cat "$3")
    if $USE_VALGRIND; then
        valgrind --tool=memcheck ../../app.exe "$param" < "$1"
	res="$?"
    else
        ../../app.exe "$param" < "$1" > /dev/null
	res="$?"
    fi
else
    if $USE_VALGRIND; then
        valgrind --tool=memcheck ../../app.exe < "$1"
	res="$?"
    else
        ../../app.exe < "$1" > /dev/null
	res="$?"
    fi
fi

# Проверка того, что программа сработала некорректно
if [ "$res" -gt 0 ]; then
    exit 0
else
    exit 1
fi
