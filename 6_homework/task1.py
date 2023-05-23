# Глобальные перемены.

# Имеется следующие переменные,
# определенные в глобальной области видимости модуля:
# number = 1
# string = 'Hello'
# Напишите и вызовите функцию, которая будет изменять эти переменные, на следующие значения:
# number = 5
# string = 'Hello, dear friend'

number = 1
string = 'Hello'


def global_changes():
    # Здесь нужно написать код
    global number, string
    number = 5
    string = 'Hello, dear friend'


global_changes()

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ
assert number == 5, 'Переменная number должна иметь значение 5'
assert string == 'Hello, dear friend', 'Переменная number должна иметь значение Home, sweet home'

print('Все ок')
