/**
 * Программа для находения подъёзда и этажа девятиэтажного дома по номеру квартиры
 */
#include <stdio.h>

// Код завершения работы программы без ошибок
#define SUCCESS 0

// Количество квартир в одном подъезде
#define ONE_ENTRANCE_ROOMS 36

int main(void)
{
    // Номер квартиры
    int room_number;

    // Ввод номера квартиры
    printf("Input room number: ");
    scanf("%d", &room_number);

    // Вычисление подъезда и этажа
    int entrance = (room_number - 1) / ONE_ENTRANCE_ROOMS + 1;
    int floor = (room_number - 1) % ONE_ENTRANCE_ROOMS / 4 + 1;

    // Вывод номера подъезда и этажа
    printf("Entrance: %d \nRoom number: %d ", entrance, floor);

    // Код успешного завершения работы програмыы
    return SUCCESS;
}

