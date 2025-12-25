def is_prime_number(num):
    num = int(num)
    if num <= 0:
        return False
    if num == 2:
        return True
    max_div = int(num ** 0.5)
    start = 3
    step = 2
    for i in range(start, max_div + 1, step):
        if num % i == 0:
            return False
    else:
        return True


num = input("Введмте число: ")
res = is_prime_number(num)
print(res)
