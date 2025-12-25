# Задание 1

import math

def calculate_root(num, err_msg):
    if num < 0:
        raise ValueError(err_msg)
    return math.sqrt(num)
try:
    num = int(input("Введите число: "))
    err_msg = "Число должно быть положительным"
    res = calculate_root(num, err_msg)
    print(res)
except ValueError as e:
    print(f"Ошибка: {e}")