def describe_person(name:str, age: int = 30 ) -> str:
    return f'name {name} age {age}'


name = input("Введите Ваше имя: ")
age = input("Введите Ваш возраст: ")
if age != "":
    age = int(age)
    result = describe_person(name, age)
else:
    result = describe_person(name)
print(result)