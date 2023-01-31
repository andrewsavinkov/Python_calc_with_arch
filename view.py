commands=['Посчитать на калькуляторе',
          'Закрыть калькулятор']

def welcome_menu() -> int:
    print('Главное меню:\t')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}.{item}')
    choice = int(input('Выберите пункт меню: '))
    return choice

def user_input():
    example=input('Введите выражение: ')
    return example

def show_result(input_string):
    print(input_string)