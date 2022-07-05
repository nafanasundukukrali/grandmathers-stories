#! /bin/bash
# Конкина А. Н., ИУ7-23Б
# Скрипт для атвоматизации тестирования, при наличии скриптов для работы с позитивными и негативными тестами
# и папки с самими тестами

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
	   if [ -z "$2" ]; then
           	./pos_case.sh ../data/"$1"_"$enter_number"_in.txt ../data/"$1"_"$enter_number"_out.txt
	   else
           	./pos_case.sh ../data/"$1"_"$enter_number"_in.txt ../data/"$1"_"$enter_number"_out.txt "$2"
	   fi

	   # Проверка кода возврата
	   res="$?"
	   if ! [ "$res" -ne 0 ]; then
               right_counter=$(("$right_counter"+1))
	   fi
       # Работа с негативными тестами
       else
	   # Запуск в зависимости от наличия файла с параметрами для программы
	   if [ -z "$2" ]; then
               ./neg_case.sh ../data/"$1"_"$enter_number"_in.txt
	   else
               ./neg_case.sh ../data/"$1"_"$enter_number"_in.txt "$2"
           fi	

	   # Проверка кода возврата
	   res="$?"
	   if ! [ "$res" -ne 0 ]; then
               right_counter=$(("$right_counter"+1))
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

   # Возвращает количество всех тестов и пройдённых через пробел
   echo "$counter $right_counter"
}

# Обработка входных параметров
echo_param=false
path_of_param_file=""
for param in "$@"; do
    if [ "$param" == "-nq" ] || [ "$param" == "--not-quiet" ]; then
        echo_param=true
    elif [ -f "$param" ]; then
        path_of_param_file=$param
    else
        if $echo_param; then
            echo Position parameters error
	fi
	exit 255
    fi
done

# Замена IFS
IFS_OLD=$IFS
IFS=" "

# Проверка позитивных тестов 
if [ -n "$path_of_param_file" ]; then
    pos_result=$(checking_tests_with_prefix pos "$path_of_param_file")
else
    pos_result=$(checking_tests_with_prefix pos)
fi

# Обработка результатов 
read -ra pos_result <<< "$pos_result"
pos_counter=${pos_result[0]}
pos_right_counter=${pos_result[1]}
if $echo_param; then
    echo There was "$pos_counter" positive tests. The script had passed "$pos_right_counter"
fi

# Проверка негативных тестов
if [ -n "$path_of_param_file" ]; then
    neg_result=$(checking_tests_with_prefix neg "$path_of_param_file")
else
    neg_result=$(checking_tests_with_prefix neg)
fi

# Обработка результатов 
read -ra neg_result <<< "$neg_result"
neg_counter=${neg_result[0]}
neg_right_counter=${neg_result[1]}
if $echo_param; then
    echo There was "$neg_counter" negative tests. The script had passed "$neg_right_counter"
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
