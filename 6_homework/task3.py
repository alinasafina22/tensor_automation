# Создаем глобальные переменные

# Напишите функцию с именем create_global
# Эта функция должна создавать глобальную переменную с именем TOTAL и присваивать ей значение x.

def create_global(x):
    # Здесь нужно написать код
    global TOTAL
    TOTAL = x
    return x


test_data = [1, 'hello', (1, 2, 3)]

for i in test_data:
    create_global(i)
    assert TOTAL == i, f'Значение переменной TOTAL должно быть равно {i}'

print('Все ок')