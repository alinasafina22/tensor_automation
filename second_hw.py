import math

"""
1. Дано 1 число - сторона квадрата. Напишите программу, которая рассчитает 3 значения: периметр квадрата,
площадь квадрата и диагональ квадрата."""


def square(side):
    perimetr = 4 * side
    area = side ** 2
    diagonal = round(side * math.sqrt(2), 2)
    return perimetr, area, diagonal


'''
2. Дано квадратное уравнение ах2 + bx + с = 0. Дискриминант уравнения должен быть больше О. Напишите программу,
которая найдет корни квадратного уравнения и округлит их до 2 знаков после запятой.
'''


def root(a, b, c):
    disc = b ** 2 - 4 * a * c
    if disc < 0:
        return 'Действующих корней нет'
    elif disc == 0:
        return round(-b / (2 * a), 2)
    else:
        x1 = round(((-b) + math.sqrt(disc)) / (2 * a), 2)
        x2 = round((-b - math.sqrt(disc)) / (2 * a), 2)
        return x1, x2


'''
3. Дано 2 строки. Напишите программу, которая объединит эти две строки в одну и разделит их пробелом,
а также поменяет местами первые два символа первой строки на первые два символа второй строки и наоборот.
'''


def string_concatenation(str1, str2):
    final_str = str1.replace(str1[:2], str2[:2]) + ' ' + str2.replace(str2[:2], str1[:2])
    return final_str


'''
4. Дан абсолютный путь до файла. Вывести название файла без расширения, названия диска и корневую папку.
'''


def file_name(path):
    name_file = path.split('\\')[-1]
    name = name_file[:name_file.rfind('.')]
    disk_name = path.split(':')[0]
    root_dir = path.split('\\')[1]
    return f'Это название файла: {name}, это диск: {disk_name}, это корневая папка: {root_dir}'


'''
5. Дано 2 числа а и b. Используя форматирование строк, выведите на экран их сумму и произведение
в форматах 'a + b = c' и 'a * b = c'.
'''


def string_format(a, b):
    return f'{a} + {b} = {a + b}, {a} * {b} = {a * b}'


'''
6. Дана строка. Напишите программу удаления символов, которые имеют нечетные значения индекса заданной строки.
'''


def delete_odd_symbols(str3):
    return str3[::2]


'''
7. Дано 2 строки из неповторяющихся символов: первая строка длиной 3 символа, вторая точно содержит
символы первой строки в любом порядке. Напишите программу, не используя циклы и условия, которая находит
срез минимальной длины во второй строке, который будет содержать все символы первой строки.
'''


def find_string(str1, str2):
    index_array = [str2.find(str1[0]), str2.find(str1[1]), str2.find(str1[2])]
    index_array.sort()
    print(index_array)
    return str2[index_array[0]:index_array[2]+1]


print(square(2))
print(root(5, 3, -26))
print(string_concatenation('Это первая строка', 'А тут вторая'))
print(file_name('C:\Thecode\Media\ст.ат.ья.txt'))
print(string_format(4, 5))
print(delete_odd_symbols('01234567890'))
print(find_string('and', 'qwerrtyuiioplkjhgfdsazxcvbnm,'))
