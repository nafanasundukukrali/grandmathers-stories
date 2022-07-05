#! /bin/bash
# Конкина А. Н., ИУ7-23Б
# Скрипт, принимающий в качестве аргументов файл для подмены входного потока,
# Эталонный файл с выводом и файл ключей к программе при необходимости

# Код возврата в случае, если файл из параметров не существует
FILE_NOT_EXISTS=2
# Не существует исполняемый файл программы
PROG_NOT_EXISTS=5
# Код возврата в случае успешного завершения работы программы и проверки valgrind
SUCCESS=0
# Код возврата в случае успешного завершения работы программы, но ошибки проверки valgrind
ONLY_VALGRIND_ERROR=255
# Код возврата в случае ошибки работы программы, но успешной проверки valgrind
ONLY_PROG_ERROR=3
# Код возврата в случае ошибки работы программы и ошибки проверки valgrind
ALL_FAILED=4

# Функция проверки valgrind
function valgrind_check {
    if [ -n "$3" ] && [ -f "$3" ]; then
	param=$(cat "$3")
	lost_param=$(valgrind --tool=memcheck --log-fd=9 9> valgrind.txt  ../../app.exe "$param" < "$1" 1> "./test_data_file.txt" 2> "./test_error_file.txt")
    else
	lost_param=$(valgrind --tool=memcheck --log-fd=9 9> valgrind.txt  ../../app.exe < "$1" 1> "./test_data_file.txt" 2> "./test_error_file.txt")
    fi
    lost_param=("definitely lost" "indirectly lost" "possibly lost" "still reachable" "suppressed")
    for lost_name in "${lost_param[@]}"; do
        lost_name="${lost_name}: [0-9]*"
        lost_num=$(grep -o "$lost_name" "./valgrind.txt" | grep -o "[0-9]*" | head -n1)
        if [ -n  "$lost_num" ] && [ "$lost_num" !=  "$SUCCESS" ]; then
            return $ONLY_VALGRIND_ERROR
        fi
    done
    return $SUCCESS
}

# Проверка существования первого файла
if [ -z "$1" ] || ! [ -f "$1" ]; then
    exit $FILE_NOT_EXISTS
fi

# Проверка существования второго файла
if [ -z "$2" ] || ! [ -f "$2" ]; then
    exit $FILE_NOT_EXISTS
fi

# Проверка существования исполнительного файла
if ! [ -f "../../app.exe" ]; then
    exit $PROG_NOT_EXISTS
fi

# Проверка наличия файла с параметрами и вызова команды
valgrind_result=0
res="$?"
if [ "$USE_VALGRIND" -eq 1 ]; then
    valgrind_check "$@"
    valgrind_result="$?"
elif  [ -n "$3" ] && [ -f "$3" ]; then
    read -ra param <<< "$(cat "$3")"
    res=$(../../app.exe "${param[@]}" < "$1" 2> "./test_error_file.txt" 1> "./test_data_file.txt")  
    res="$?"
else    
    res=$(../../app.exe < "$1" 2> "./test_error_file.txt" 1> "./test_data_file.txt")
    res="$?"
fi

# Проверка того, что программа сработала корректно
res="$?"
if [[ -s "./test_error_file.txt" || "$res" -ne "$SUCCESS" ]] && [ "$valgrind_result" -ne "$ONLY_VALGRIND_ERROR" ]; then
    exit $ONLY_PROG_ERROR
elif [[ -s "./test_error_file.txt" || "$res" -ne "$SUCCESS" ]] && [ "$valgrind_result" -eq "$ONLY_VALGRIND_ERROR" ]; then
    exit $ALL_FAILED
else
    # Сравнение результатов
    ./comparator.sh "$2" "./test_data_file.txt"
    res="$?"
    if [ "$res" -ne "$SUCCESS" ] && [ "$valgrind_result" -eq "$ONLY_VALGRIND_ERROR" ]; then
        exit $ALL_FAILED
    elif [ "$res" -ne "$SUCCESS" ] && [ "$valgrind_result" -ne "$ONLY_VALGRIND_ERROR" ]; then
        exit $ONLY_PROG_ERROR
    elif [ "$res" -eq "$SUCCESS" ] && [ "$valgrind_result" -eq "$ONLY_VALGRIND_ERROR" ]; then
        exit $ONLY_VALGRIND_ERROR
    else
        exit $SUCCESS
    fi
fi
