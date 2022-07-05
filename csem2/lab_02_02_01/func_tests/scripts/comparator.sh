#! /bin/bash

# Конкина А. Н., ИУ7-23Б
# Скрипт для сравнения последовательностей целых чисел

# Код возврата того, что файл не существует
FILE_NOT_EXISTS=2
# Код возврата несовпадения данных целевых файлов
DATA_NOT_SAME=1
# КОд возврата успешного сравнения данных файлов
SUCCESS=0

# Првоерка существования файла, введённого в качестве первого позиционного параметра
if ! [ -f "$1" ]; then
    echo Error: file "$1" does not exist
    exit $FILE_NOT_EXISTS
fi

# Проверка существования второго файла
if ! [ -f "$2" ]; then
    echo Error: file "$2" does not exist
    exit $FILE_NOT_EXISTS
fi

# Содержимое первого файла
first_data=$( tr '[:blank:]' "\n" < "$1" | grep -Eo "[+-]?[0-9]*[.,]?[0-9]+")

# Содержимое второго файла
second_data=$( tr '[:blank:]' "\n" < "$2" | grep -Eo "[+-]?[0-9]*[.,]?[0-9]+")

# Сравнение длины полученных масивов
if [ "${#first_data[@]}" -ne "${#second_data[@]}" ] || [ "${#first_data[@]}" == "0" ]; then
    exit $DATA_NOT_SAME
fi

# Сравнение массивов
if ! [ "${first_data[*]}" ==  "${second_data[*]}" ]; then
    exit $DATA_NOT_SAME
fi

exit $SUCCESS

