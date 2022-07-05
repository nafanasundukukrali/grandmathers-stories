#! /bin/bash
# Конкина А. Н., ИУ7-23Б
# Скрипт для атвоматизации тестирования, при наличии скриптов для работы с позитивными и негативными тестами
# и папки с самими тестами

export USE_VALGRIND=1

# Ошибка ввода параметров
PARAM_ERROR=254
SUCCESS=0

function checking_tests_with_prefix {
   # Функция для обхода всех тестов и использования их в качестве тестирования
   # Количество провильно пройденных тестов, тестов всего и акутальный номер интересуюещго теста
   right_counter=0
   counter=0
   enter_number="01"

   # Обработка каждого входного файла, проверка, что есть файл с выходными данными
   while [ -f ../data/"$1"_"$enter_number"_in.txt ]; do
       # Проверка наличия файла с выходными данными
       if [ "$1" == "pos" ] && ! [ -f ../data/"$1"_"$enter_number"_out.txt ]; then
           counter=$(("$counter"+1))
	   if [ $(("$counter"+1)) -gt 9 ]; then
	       enter_number=$(("$counter"+1))
       	   else
	       new_pos=$(("$counter"+1))
	       enter_number="0$new_pos"
       	   fi
  	   continue
       fi
       # Работа с позитивными тестами
       if [ "$1" == "pos" ]; then
	   # Запуск в зависимости от наличия файла с параметрами
	   if ! [ -f ../data/"$1"_"$enter_number"_arg.txt ]; then
		./pos_case.sh ../data/"$1"_"$enter_number"_in.txt ../data/"$1"_"$enter_number"_out.txt > /dev/null
	   else
		./pos_case.sh ../data/"$1"_"$enter_number"_in.txt ../data/"$1"_"$enter_number"_out.txt ../data/"$1"_"$enter_number"_arg.txt > /dev/null
	   fi

	   # Проверка кода возврата
	   res="$?"
	   if [ "$res" -eq "$SUCCESS" ] && [ $USE_VALGRIND -eq 1 ]; then
	       if $2; then
	           echo test pos_$enter_number: PASS, MEMORY OK
               fi
               right_counter=$(("$right_counter"+1))
	   elif [ "$res" == 3 ] && $2 && [ $USE_VALGRIND -eq 1 ]; then
               echo test pos_$enter_number: FAILED, MEMORY OK
	   elif [ "$res" == 4 ] && $2 && [ $USE_VALGRIND -eq 1 ]; then
               echo test pos_$enter_number: FAILED, MEMORY FAILED
	   elif [ "$res" == 255 ] && $2 && [ $USE_VALGRIND -eq 1 ]; then
               echo test pos_$enter_number: PASS, MEMORY FAILED
	   elif [ "$res" -eq "$SUCCESS" ]; then
               if $2; then
                   echo test pos_$enter_number: PASS
               fi
               right_counter=$(("$right_counter"+1))
           elif $2; then
               echo test pos_$enter_number: FAILED
	   fi
       # Работа с негативными тестами
       else
	   # Запуск в зависимости от наличия файла с параметрами для программы
	   if ! [ -f ../data/"$1"_"$enter_number"_arg.txt ]; then
               ./neg_case.sh ../data/"$1"_"$enter_number"_in.txt > /dev/null
	   else
               ./neg_case.sh ../data/"$1"_"$enter_number"_in.txt ../data/"$1"_"$enter_number"_arg.txt > /dev/null
           fi	

	   # Проверка кода возврата
	   res="$?"
           if [ "$res" -eq "$SUCCESS" ] && [ $USE_VALGRIND -eq 1 ]; then
               if $2; then
                   echo test neg_$enter_number: PASS, MEMORY OK
               fi
               right_counter=$(("$right_counter"+1))
           elif [ "$res" == 1 ] && $2 && [ $USE_VALGRIND -eq 1 ]; then
               echo test neg_$enter_number: FAILED, MEMORY OK
           elif [ "$res" == 4 ] && $2 && [ $USE_VALGRIND -eq 1 ]; then
               echo test neg_$enter_number: FAILED, MEMORY FAILED
           elif [ "$res" == 254 ] && $2 && [ $USE_VALGRIND -eq 1 ]; then
               echo test neg_$enter_number: PASS, MEMORY FAILED
           elif [ "$res" -eq "$SUCCESS" ]; then
               if $2; then
                   echo test neg_$enter_number: PASS
               fi
               right_counter=$(("$right_counter"+1))
           elif $2; then
               echo test neg_$enter_number: FAILED
           fi

       fi

       # Увеличение счётчика количества обработанных тестов и следующего номера теста
       counter=$(("$counter"+1))
       if [ "$(("$counter"+1))" -gt 9 ]; then
	   enter_number=$(("$counter"+1))
       else
	   new_pos=$(("$counter"+1))
	   enter_number="0$new_pos"
       fi
   done
}

# Обработка входных параметров
echo_param=false
for param in "$@"; do
    if [ "$param" == "-nq" ]; then
        echo_param=true
    else
        if $echo_param; then
            echo Position parameters error
	fi
	exit $PARAM_ERROR
    fi
done

# Замена IFS
IFS_OLD=$IFS
IFS=" "

# Проверка позитивных тестов 
counter=0
right_counter=0
checking_tests_with_prefix pos "$echo_param"

# Обработка результатов 
pos_counter=$counter
pos_right_counter=$right_counter
if $echo_param; then
    echo There were "$pos_counter" positive tests. The script had passed "$pos_right_counter"
fi

# Проверка негативных тестов
checking_tests_with_prefix neg "$echo_param"

# Обработка результатов 
neg_counter=$counter
neg_right_counter=$right_counter
if $echo_param; then
    echo There were "$neg_counter" negative tests. The script had passed "$neg_right_counter"
fi

# Общий результат
result=$(("$pos_counter"-"$pos_right_counter"+"$neg_counter"-"$neg_right_counter"))
if $echo_param && [ "$result" == "0" ]; then
    echo All tests have been passed!
elif $echo_param; then
    echo "$result" tests haven\'t been passed
fi

# Замена IFS на изначальный
IFS=$IFS_OLD

# Завершение работы скрипта
exit $result
