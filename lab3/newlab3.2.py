def write_text(write, mode=None):
    if write == 'написать':
        with open('user_input.txt','w') as file:
            file.write(input('Введите текст '))
            return f'Текст записан'
    elif write == 'дописать':
        if line1 == 'с новой':
            with open('user_input.txt','a') as file:
                file.write('\n' + input('Введите текст '))
                return f'Текст дописан с новой строки'
        elif line1 == 'продолжить':
            with open('user_input.txt','a') as file:
                file.write(input('Введите текст '))
                return f'Текст дописан'
        else:
            return f'нет варианта выбора {line1} '
    else:
        return f'нет варианта выбора {write} '
write = input('вы хотите написать новый текст или дописать старый? (написать/дописать) ')
if write == 'дописать':
    line1=input('с новой строки или продолжить? (с новой/продолжить) ')
    print(write_text(write,line1))
else:
    print(write_text(write))