'''2. Работа со словарями:
  - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
Например: Имя(str)-Год рождения(int).
  - Выведите на экран словарь my_dict.
  - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
  - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
 - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
  - Выведите на экран словарь my_dict.'''

# my_dict = {'Alex':1999, 'John':1972, 'Niko':1991, 'Max':1993}
# print(my_dict)
# print(my_dict['Niko'])
# print(my_dict.get('Alan'))

# my_dict.update({'Joseph':1995, "Harry":1998 })
# name = my_dict.pop('Max')
# print(name)
# print(my_dict)

'''3. Работа с множествами:
  - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
  - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
  - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
  - Удалите один любой элемент из множества my_set.
  - Выведите на экран измененное множество my_set.'''

my_set = {192, 432, 5555, 3462, 1923, 5555, 432, True, 'settes'}
print(my_set)
my_set.update({333, 456})
my_set.discard(5555)
print(my_set)