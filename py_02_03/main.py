from math import *


def main():
    def func(x):
        return eval(f)

    def method_of_bisections(x1, x2):
        x = (x1 + x2) / 2
        if abs(func(x)) < epsilon:
            return x
        if func(x1)*func(x) < 0:
            return method_of_bisections(x1, x)
        else:
            return method_of_bisections(x, x2)

    f = input('Введите функцию: ')
    a = float(input('Введите a: '))
    b = float(input('Введите b: '))
    epsilon = float(input('Введите эпсилон: '))
    print('Корень: ', method_of_bisections(a, b))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
