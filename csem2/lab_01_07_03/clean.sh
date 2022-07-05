#! /bin/bash

function check_if_dir_exists {
    # Функция для проверки, существует ли диреткория по указанному пути
    if [ ! -d "$1" ]; then
       echo Error: "$1" directory is not exist
       exit 2
    fi
}

# Файлы, которые могут находиться на верхнем уровне проекта
RIGHT_FIRST_LEVEL_FILES_NAMES=("main.c" "main.o" "app.exe" "build_release.sh" "build_debug.sh" "clean.sh")

# Обходим каждый файл среди файлов верхнего уровня проекта
for file in *; do
    # Счётчик совпадения имён
    # 0 - наименования файла нет среди корректных
    # 1 - имя файла есть среди корректных
    counter=0
    for right_name in "${RIGHT_FIRST_LEVEL_FILES_NAMES[@]}"; do
        if [ "$right_name" == "$file" ]; then
	    counter="$((counter+1))"
	    RIGHT_FILES_COUNTER="$((RIGHT_FILES_COUNTER+1))"
        fi
    done

    # Если счётчик равн 0 и файл является файлом, то он удаляется
    if [ $counter -eq 0 ] && [ -f "$file" ]; then
        rm -f "$file"
	continue
    fi
    
    # Удаление лишних папок проекта, если файл является директорией
    if [ "$file" != "func_tests" ] && [ -d "$file" ]; then
        rm -fr "$file"
    fi
done

# Проверка на то, что директория func_tests существует
check_if_dir_exists "func_tests"

# Обходим каждый файл директории func_tests и удаляем лишние
for file in ./func_tests/*; do
    # Название файла
    filename=$(basename -- "$file")
        
    # Удаление файла, если он не readme.md
    if [ -f "$file" ] && [ "$filename" != "readme.md" ]; then
        rm -f "$file"
    fi
    
    # Удаление директории, если она не scripts и не data
    if [ -d "$file" ] && [ "$file" != "./func_tests/scripts" ] && [ "$file" != "./func_tests/data" ]; then
        rm -rf "$file"
    fi
done

# Убеждаемся, что дректория scripts существует
check_if_dir_exists "./func_tests/scripts"

for file in ./func_tests/scripts/*; do
    # Название файла
    filename=$(basename -- "$file")

    # Удаление всех файлов, не подходящие под шаблон наименований четырёх скриптов
    if [ -f "$file" ] && [ "$filename" != "func_tests.sh" ] && [ "$filename" != "neg_case.sh" ] && [ "$filename" != "pos_case.sh" ] && [ "$filename" != "comparator.sh" ] && [ "$filename" != "comparator_1.sh" ]; then
        rm -f "$file"
    fi
    
    # Удаление лишних директорий
    if [ -d "$file" ]; then
        rm -fr "$file"
    fi
done

# Убеждаемся, что директория data существует
check_if_dir_exists "./func_tests/data"

for file in ./func_tests/data/*; do
    # Название файла
    filename=$(basename -- "$file")

    # Удаление всех пложенных лишних директорий внутри проекта
    if [ -d "$file" ]; then
        rm -fr "$file"
	continue
    fi

    # Удаление всех файлов, не попадающих под шаблоны тестов, определённых ТЗ
    if ! echo "$filename" | grep -Eq "^(pos|neg)_[0-9]{2}_(in|out)\.txt"; then
        rm -f "$file"
	continue
    fi
done
