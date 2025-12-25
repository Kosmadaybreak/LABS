def square(num):
    num = int(num)
    num = num ** 2
    return f"Квадрат: {num}"


num = input("Введите число: ")
result = square(num)
print(result)
