def format_text(filename, format):
    try:
        if format == 'целиком':
            with open(filename, 'r') as file:
                return file.read()
        elif format == 'построчно':
            with open(filename, 'r') as file:
                lines = file.readlines()
                line_number = int(input('какой номер строки вы хотите вывести?'))
            if 1 <=line_number<=len(lines):
                return f'Строка {line_number}: {lines[line_number-1]}'
            else:
                return f'в файле только {len(lines)} строк'
        else:
            return f'нет варианта выбора {format}'
    except FileNotFoundError:
        return False
filename = input("Введите название файла")
format = input('как вы хотите увидеть текст?(целиком или построчно)')
print(format_text(filename, format))
