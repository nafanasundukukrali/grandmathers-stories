/**
 * Программа для упаковки четырёх байт в четырёхбайтовое беззнаковое число и 
 * распоковки обратно.
 */

#include <stdio.h>
#include <math.h>
#include <stdint.h>

// Код успешного завершения работы программы
#define SUCCESS 0
// Код завершение работы с  ошибкой
#define ERROR 1

// 32 бита
#define POW (uint32_t) 1 << 31
// 8 бит
#define EIGHT_BITS (uint32_t) 255
// Для перемещения на позицию первого четвёртого байта и наоборот
#define FIRST_BYTE_POS 24u
// Для перемещения на позицию второго четвёртого байта и наоборот
#define SECOND_BYTE_POS 16u
// Для перемещения на позицию третьего байта и наоборот
#define THIRD_BYTE_POS 8u

void print_bin_from_dec(uint32_t input_value)
{
    /**
     * Функция для вывода двоичной формы записи целого беззнакового числа.
     * input_value - значение интересующего целого беззнакового числа
     */
   
    //Делаем маску на 1 бит и сдвигаем её на 31 бит
    uint32_t pow = POW;

    // Пока у нас маска не становится равной 0
    while (pow)
    {
        // Смотрим, есть ли бит на этой "позиции" в безнаковом числе
        if (input_value & pow)
            // Если есть, то выводим единицу
            printf("1");
        else
            // Если нет, то выводим 0
            printf("0");
	// Сдвишаем маску на 1 бит вправо
        pow >>= 1;
    }
}

uint32_t get_result_of_bytes_packing(uint32_t first_byte, uint32_t second_byte, uint32_t third_byte, uint32_t fourth_byte)
{
    /**
    * Функция для получения упаковкий 4 байт  с помощью побитового умножения с маской и сдвига влево на
    * необходимое количество байт
    */
    return ((fourth_byte & EIGHT_BITS) << FIRST_BYTE_POS) + ((third_byte & EIGHT_BITS) << SECOND_BYTE_POS) + ((second_byte & EIGHT_BITS) << THIRD_BYTE_POS) + (first_byte & EIGHT_BITS);
}

uint32_t get_byte_from_packing_4_bytes(uint32_t packed_unsigned_int, int byte_number)
{
    /**
    * Функция для получения байта под номером byte_number из последоательности 4 байтов распоковки путём побитового умножения со сдвинутой маской и сдвига на позицию
    * первого байта
    */
    if (byte_number == 1)
        // 1 байт
        return (packed_unsigned_int & (EIGHT_BITS << FIRST_BYTE_POS)) >> FIRST_BYTE_POS;
    else if (byte_number == 2)
        // 2 байт
        return (packed_unsigned_int & (EIGHT_BITS << SECOND_BYTE_POS)) >> SECOND_BYTE_POS;
    else if (byte_number == 3)
        // 3 байт
        return (packed_unsigned_int & (EIGHT_BITS << THIRD_BYTE_POS)) >> THIRD_BYTE_POS;
    // 4 байт
    return packed_unsigned_int & EIGHT_BITS;
}

void work_with_input_bytes(uint32_t first_byte, uint32_t second_byte, uint32_t third_byte, uint32_t fourth_byte)
{
    /**
     * Функция для работы с полученными четырьмя байтами
     * Входнеы данные: четыре байта
     */

    // Получение упаковки
    uint32_t packed_unsigned_int = get_result_of_bytes_packing(first_byte, second_byte, third_byte, fourth_byte);
    
    // Распоковка
    // Первый байт 
    uint32_t new_first_byte = get_byte_from_packing_4_bytes(packed_unsigned_int, 1);
    // Второй байт
    uint32_t new_second_byte = get_byte_from_packing_4_bytes(packed_unsigned_int, 2);
    // Третий байт
    uint32_t new_third_byte = get_byte_from_packing_4_bytes(packed_unsigned_int, 3);
    // Четвёртый байт
    uint32_t new_fourth_byte = get_byte_from_packing_4_bytes(packed_unsigned_int, 4);

    // Вывод результата обработки входных байтов
    printf("Result: "); 
    // Вывод упаковки в двоичной записи
    print_bin_from_dec(packed_unsigned_int);
    // Вывод распоковки
    printf(" %u %u %u %u", new_first_byte, new_second_byte, new_third_byte, new_fourth_byte);
}

int main(void)
{
    // Входные байты пользователя
    uint32_t first_byte, second_byte, third_byte, fourth_byte;
    
    // Ввод байтов с проверкой того, что все они введены корректно
    printf("Input bytes with spaces between: ");
    if (scanf("%u%u%u%u", &fourth_byte, &third_byte, &second_byte, &first_byte) != 4)
    {
        // Байты введены некорретно, возвращаем код ошбки и выводим сообщение об ошибке
        printf("Error: input value not unsigned integer");
        return ERROR;
    }

    // Обработка входных данных
    work_with_input_bytes(first_byte, second_byte, third_byte, fourth_byte);
    
    // Успешное завершение работы программы
    return SUCCESS;
}


