print("Введите 2 разных числа")
user_input1 = input("Введите число 1: ")
user_input2 = input("Введите число 2: ")
if user_input1 > user_input2:
    print("Большее число: ", user_input1)
elif user_input2 > user_input1:
    print("Большее число: ", user_input2)
else:
    print(user_input1, "=", user_input2)