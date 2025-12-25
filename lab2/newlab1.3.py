def max_of_two(user_input1, user_input2):
    if user_input1 > user_input2:
        return f"Большее число: {user_input1}"
    elif user_input2 > user_input1:
        return f"Большее число: {user_input2}"
    else:
        return f"Большее число: {user_input1} = {user_input2}"
print("Введите 2 разных числа")
user_input1 = input("Введите число 1: ")
user_input2 = input("Введите число 2: ")
result = max_of_two(user_input1, user_input2)
print(result)