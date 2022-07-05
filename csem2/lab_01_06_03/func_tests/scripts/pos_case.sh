#! /bin/bash
# Конкина А. Н., ИУ7-23Б
# Скрипт, принимающий в качетсве аргументов файл для подменны входного потока,
# Эталонный файл с выводом и файл ключей к программе при необходимости

# Valgrind
USE_VALGRIND=false

# Проверка существования первого файла
if [ -z "$1" ] || ! [ -f "$1" ]; then
    exit 2
fi

# Проверка существования второго файла
if [ -z "$2" ] || ! [ -f "$2" ]; then
    exit 2
fi

# Проверка существования исполнительного файла
if ! [ -f "../../app.exe" ]; then
    exit 2
fi

# Проверка наличия файла с параметрами и вызов команды
if [ -n "$3" ] && [ -f "$3" ]; then
    param=$(cat "$3")
    if $USE_VALGRIND; then
    	result=$(valgrind --tool=memcheck ../../app.exe "$param" < "$1")
    else
        result=$(../../app.exe "$param" < "$1")
    fi	    
else
    if $USE_VALGRIND; then
        result=$(valgrind --tool=memcheck ../../app.exe < "$1")
    else
        result=$(../../app.exe < "$1")
    fi
fi

# Проверка того, что программа сработала корректно
res="$?"
if [ "$res" -ne 0 ]; then
    exit 3
else
    # Сравнение результатов
    echo "$result" > res_local.txt
    ./comparator.sh "$2" res_local.txt
    res="$?"
    rm res_local.txt
    if [ "$res" -ne 0 ]; then
        exit 1
    else
        exit 0
    fi
fi
