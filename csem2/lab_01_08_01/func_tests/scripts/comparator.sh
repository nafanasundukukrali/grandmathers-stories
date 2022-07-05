#! /bin/bash

# Конкина А. Н., ИУ7-23Б
# Скрипт для нахождения подстрок после слова Result: и сравнения результатов в двух файлах

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
first_data=$(cat "$1")

# Содержимое второго файла
second_data=$(cat "$2")

# Нахождение числа отделённого пробелами в обоих текстах
first_data=$(echo "$first_data" | grep -Eo "Result: .*")
second_data=$(echo "$second_data" | grep -Eo "Result: .*")

# Сравнение полученных строк
if [ -n "$first_data" ] && [ "$first_data" == "$second_data" ]; then
    exit 1
else
    exit 0
fi
