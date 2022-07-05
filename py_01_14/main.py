import random
import time

def method_of_inserts_with_barrier(input_list: list):
    input_list = [0] + input_list
    for i in range(1, len(input_list)):
        input_list[0] = input_list[i]
        j = i - 1
        while input_list[0] < input_list[j]:
            input_list[j + 1] = input_list[j]
            j = j - 1
        input_list[j + 1] = input_list[0]
    return input_list[1:]


def time_of_sort(input_list: list):
    start = time.perf_counter()
    method_of_inserts_with_barrier(input_list)
    stop = time.perf_counter()
    return stop - start


input_len = input('Введите количество элементов пользовательского массива: ')
while not input_len.isdigit():
    user_answer = input('Количество элементов пользовательского массива введено некорректно. Повторите ввод? [Д/Н]: ')
    if user_answer == 'Д':
        input_len = input('Введите количество элементов пользовательского массива: ')
    elif user_answer == 'Н':
        print('Операция прервана.')
        exit(1)
    else:
        print('Введёт некорректный пользовательский ответ.')
input_list = []
input_len = int(input_len)
for i in range(input_len):
    input_value = input(f'Введите {i+1} элемент списка: ')
    while not (input_value.isdigit() if input_value and input_value[0] != '-' else False if not input_value else input_value[1:].isdigit()):
        user_answer = input(
            'Элемент пользовательского списка введен некорректно. Повторите ввод? [Д/Н]: ')
        if user_answer == 'Д':
            input_value = input(f'Введите {i+1} элемент списка: ')
        elif user_answer == 'Н':
            print('Операция прервана.')
            exit(1)
        else:
            print('Введёт некорректный пользовательский ответ.')
    input_list.append(int(input_value))
print('Сортировка пользовательского массива:')
print(*method_of_inserts_with_barrier(input_list))
input_numbers = []
for i in range(3):
    input_first_len = input(f'Введите количество элементов {i+1} списка: ')
    while not input_first_len.isdigit():
        user_answer = input(f'Количество элементов {i+1} списка введено некорректно. Повторите ввод? [Д/Н]: ')
        if user_answer == 'Д':
            input_first_len = input(f'Введите количество элементов {i+1} списка: ')
        elif user_answer == 'Н':
            print('Операция прервана.')
            exit(1)
        else:
            print('Введёт некорректный пользовательский ответ.')
    input_numbers.append(int(input_first_len))
# Время сортировки сортированного списка
assorted_lists_results = []
for i in range(3):
    assorted_list = [j+1 for j in range(input_numbers[i])]
    assorted_lists_results.append(time_of_sort(assorted_list))
# Время сортировки рандомного списка
random_lists_results = []
for i in range(3):
    random_list = [random.randint(-input_numbers[i], input_numbers[i]) for j in range(input_numbers[i])]
    random_lists_results.append(time_of_sort(random_list))
# Время сортировки обратно упорядоченного списка
unsorted_lists_results = []
for i in range(3):
    unsorted_list = [input_numbers[i]-j for j in range(input_numbers[i])]
    unsorted_lists_results.append(time_of_sort(unsorted_list))
print()
print('|'+'-'*135+'|')
print('|'+' '*33+'|'+'{:^33}'.format(input_numbers[0])+'|'+'{:^33}'.format(input_numbers[1])+'|'+'{:^33}'.format(input_numbers[2])+'|')
print('|'+'-'*135+'|')
print('|' + '{:^33}'.format('Упорядоченный список')+'|'+'{:^33.7f}'.format(assorted_lists_results[0])+'|'+'{:^33.7f}'.format(assorted_lists_results[1])+'|'+'{:^33.7f}'.format(assorted_lists_results[2])+'|')
print('|'+'-'*135+'|')
print('|' + '{:^33}'.format('Случайный список')+'|'+'{:^33.7f}'.format(random_lists_results[0])+'|'+'{:^33.7f}'.format(random_lists_results[1])+'|'+'{:^33.7f}'.format(random_lists_results[2])+'|')
print('|'+'-'*135+'|')
print('|' + '{:^33}'.format('Упорядоченный в обратном порядке')+'|'+'{:^33.7f}'.format(unsorted_lists_results[0])+'|'+'{:^33.7f}'.format(unsorted_lists_results[1])+'|'+'{:^33.7f}'.format(unsorted_lists_results[2])+'|')
print('|'+'-'*135+'|')




