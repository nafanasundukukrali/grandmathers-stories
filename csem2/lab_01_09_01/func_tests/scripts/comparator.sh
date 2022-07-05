#! /bin/bash

# Конкина А. Н., ИУ7-23Б
# Скрипт для сравнения последовательностей целых чисел

# Првоерка существования файла, введённого в качестве первого позиционного параметра
if ! [ -f "$1" ]; then
    echo Error: file "$1" does not exist
    exit 2
fi

# Проверка существования второго файла
if ! [ -f "$2" ]; then
    echo Error: file "$2" does not exist
    exit 2
fi

# Содержимое первого файла
first_data=$(cat "$1" | tr [:blank:] \n | grep -Eo "[+-]?[0-9]*[.,]?[0-9]+" | sort -n)

# Содержимое второго файла
second_data=$(cat "$2" | tr [:blank:] \n | grep -Eo "[+-]?[0-9]*[.,]?[0-9]+" | sort -n)

# Сравнение длины полученных масивов
if [ "${#first_data[@]}" -ne "${#second_data[@]}" ] || [ "${#first_data[@]}" == "0" ]; then
    exit 1
fi

# Сравнение массивов
if ! [ "${first_data[*]}" ==  "${second_data[*]}" ]; then
    exit 1
else
    exit 0
fi
