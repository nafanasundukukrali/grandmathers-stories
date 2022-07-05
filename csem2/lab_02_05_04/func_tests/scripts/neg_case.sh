#! /bin/bash
# Конкина А. Н., ИУ7-23Б
# Скрипт, принимающий в качетсве аргументов файл для подменны входного потока,
# И файл ключей к программе при необходимости

# Код возврата в случае, если файл из параметров не существует
FILE_NOT_EXISTS=2
# Не существует исполняемый файл программы
PROG_NOT_EXISTS=5
# Код возврата в случае успешного завершения работы программы и проверки valgrind
PROG_NOT_FAILED=1
# Код возврата в случае ошибки работы программы и ошибки проверки valgrind
ONLY_VALGRIND_ERROR=254
# Код в случае успешного завершения работы программы и ошибки valgrind
ALL_FAILED=4
# Код возврата в случае ошибки работы программы, но успешного прохода valgrind
PROG_FAILED=0

function valgrind_check {
    if [ -n "$3" ] && [ -f "$3" ]; then
        param=$(cat "$3")
	lost_param=$(valgrind --tool=memcheck --log-fd=9 9> valgrind.txt  ../../app.exe "$param" < "$1" 2 > "./not_predicted_error.txt")
    else
	lost_param=$(valgrind --tool=memcheck  --log-fd=9 9> valgrind.txt   ../../app.exe < "$1" 2> "./not_predicted_error.txt")
    fi
    res="$?"
    lost_param=("definitely lost" "indirectly lost" "possibly lost" "still reachable" "suppressed")
    for lost_name in "${lost_param[@]}"; do
        lost_name="${lost_name}: [0-9]*"
        lost_num=$(grep -o "$lost_name" "./valgrind.txt" | grep -o "[0-9]*" | head -n1)
        if [ -n "$lost_num" ] && [ "$lost_num" !=  "$PROG_FAILED" ]; then
            return $ONLY_VALGRIND_ERROR
        fi
    done
    return $PROG_FAILED
}

# Проверка существования первого файла
if [ -z "$1" ] || ! [ -f "$1" ]; then
    exit $FILE_NOT_EXISTS
fi

# Проверка существования исполнительного файла
if ! [ -f "../../app.exe" ]; then
    exit $PROG_NOT_EXISTS
fi

valgrind_result=0
if [ "$USE_VALGRIND" -eq 1 ]; then
    valgrind_check "$@"
    valgrind_result="$?"
elif [ -n "$3" ] && [ -f "$3" ]; then
    read -ra param <<< "$(cat "$3")"
    res=$(../../app.exe "${param[@]}" < "$1" 1> /dev/null  2> "./not_predicted_error.txt")
    res="$?"
else
    res=$(../../app.exe < "$1" 1> /dev/null 2> "./not_predicted_error.txt")
    res="$?"
fi

res_predicted=$(cat "./not_predicted_error.txt")
# Проверка того, что программа сработала корректно
if  [[ -n "$res_predicted" ||  "$res" -eq "$PROG_FAILED" ]] && [ "$valgrind_result" -ne "$ONLY_VALGRIND_ERROR" ]; then
    exit $PROG_NOT_FAILED
elif [[ -n "$res_predicted" || "$res" -eq "$PROG_FAILED" ]] && [ "$valgrind_result" -eq "$ONLY_VALGRIND_ERROR" ]; then
    exit $ALL_FAILED
elif [ "$valgrind_result" -eq "$ONLY_VALGRIND_ERROR" ]; then
    exit $ONLY_VALGRIND_ERROR
else
    exit $PROG_FAILED
fi
