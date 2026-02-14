import random 

## Списки
### Пример создания списка
#my_list = [1, 2, 3, 4, 5]
#print(my_list)
#
### Добавление элемента в список
#my_list.append(6)
#print(my_list)
#
### Удаление элемента из списка
#my_list.remove(3)
#print(my_list)
#
### Доступ к элементу по индексу
#print(my_list[2])
#
#
## Словарь 
### Пример создания словаря
#my_dict = {
#    'name': 'Alice', 
#    'age': 25, 
#    'city': 'New York'
#    }
#print(my_dict)
#
#
### Добавление новой пары ключ-значение
#my_dict['email'] = 'alice@example.com'
#print(my_dict)
#
### Удаление пары ключ-значение
#del my_dict['age']
#print(my_dict)
#
### Доступ к значению по ключу
#print(my_dict['name'])
#
##Кортежи 
### Пример создания кортежа
#my_tuple = (1, 2, 3, 4, 5)
#print(my_tuple)
#
### Доступ к элементу по индексу
#print(my_tuple[2])
#
## Попытка изменить элемент (вызовет ошибку)
#my_tuple[2] = 10
#
## Множество
### Пример создания множества
#my_set = {1, 2, 3, 4, 5}
#print(my_set)
#
### Добавление элемента в множество
#my_set.add(6)
#print(my_set)
#
### Удаление элемента из множества
#my_set.remove(3)
#print(my_set)
#
### Проверка наличия элемента в множестве
#print(4 in my_set)

#Поиск максимального элемента в списке

#array = [random.randint(0, 100) for x in range(10)]
#max_val = array[0]
#min_val = array[0]
#for item in array:
#    if item > max_val:
#        max_val = item
#    if item < min_val:
#        min_val = item
#
#print(array)
#print(max_val)
#print(min_val)
#print(max(array))
#Проверка на палиндром
#val = 'dom'
#rev = val[::-1]
#if val == rev:
#    print('Палиндром')
#else:
#    print('Не палиндром')
#print(val)
#print(rev) 
##Реверс строки

#Сумма элементов списка
array = [random.randint(0, 100) for x in range(10)]
sum = 0
K_elm = 0
for item in array: 
    sum += item 
    K_elm += 1
    print(item)
print(array)
#print(sum(array))
print(len(array))

print(sorted(array))