'''Задача 1 (просто) "Арифметика":
Напишите в начале программы однострочный комментарий: "1st program".
Выведите на экран(в консоль) результат: возведение числа 9 в степень 0.5, после умножение на 5.
Предполагаемый результат: 15.0'''

#1 st program
print(9**0.5*5)


'''Задача 2 (просто) "Логика":
Напишите в начале программы однострочный комментарий: "2nd program".
Убедитесь в том что 9.99 больше 9.98 и 1000 не равно 1000.1 одновременно, выведете результат на экран(в консоль)
 Предполагаемый результат: True'''

# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)

'''Задача 3 (средне) "Школьная загадка":
Напишите в начале программы однострочный комментарий: "3rd program".
Выведите на экран(в консоль) 2 умноженное на 2 плюс 2 без приоритета.
Выведите на экран(в консоль) 2 умноженное на 2 плюс 2 с приоритетом для сложения.
Выведите на экран(в консоль) результат сравнения этих двух выражений.
Предполагаемый результат (с использованием ==): False'''


# 3rd program

print(2 * 2 + 2)
print(2 * (2 + 2))
print(2 * 2 + 2 == 2 * (2 + 2))

'''Задача 4 (сложно) "Первый после точки":
Напишите в начале программы однострочный комментарий: "4th program".
Дана строка '123.456'.
Вывести на экран первую цифру после запятой - 4.'''

# 4th program
text = '123.456'
text = float(text) * 10
print(int(text % 10))