from modul import multiply
from modul import is_even
from modul import reverse_string
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
res = multiply(a, b)
print(res)

number = int(input("Введите число: "))
res1 = is_even(number)
print(res1)

user_str = "Что люблю? Голубцы? Давай 3!"
res2 = reverse_string(user_str)
print(res2)