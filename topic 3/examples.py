# Синтаксис цикла while
while условие:
    # тело цикла
    инструкция1
    инструкция2

# Проверка пароля
saved_pwd = "right_password"
pwd = input("Введите пароль для входа: ")
while pwd != saved_pwd:
    pwd = input("Введите пароль для входа: ")
print("Пароль верный. Вход разрешён.")

# Счетчик от 1 до 10
i = 1
while i <= 10:
    print(i)
    i += 1  # увеличиваем счётчик на 1

# Подсчёт количества цифр числа
n = int(input("Введите натуральное число: "))
length = 0
while n > 0:
    n //= 10      # отбрасываем последнюю цифру
    length += 1   # увеличиваем счётчик цифр
print(f"Количество цифр: {length}")

# Без моржового оператора:
name = input("Введите имя: ")
while name != "СТОП":
    print(f"Привет, {name}!")
    name = input("Введите имя: ")
print("Программа завершена.")

# С моржовым оператором:
while (name := input("Введите имя: ")) != "СТОП":
    print(f"Привет, {name}!")
print("Программа завершена.")

# Синтаксис цикла for:
for переменная in итерируемый_объект:
    # тело цикла
    инструкция1
    инструкция2

# Перебор списка
colors = ["красный", "синий", "зелёный"]
for color in colors:
    print(color)

# Перебор строки
for letter in "Python":
    print(letter)

# Вывод чётных чисел
n = int(input("Введите n: "))
for i in range(0, n + 1, 2):
    print(i)

# Обратный отсчёт
for i in range(5, 0, -1):
    print(i)
print("Поехали!")

# Поиск первого чётного числа
numbers = [1, 3, 7, 10, 5]
for num in numbers:
    if num % 2 == 0:
        print(f"Найдено чётное число: {num}")
        break  # цикл прекращается

# while: бесконечный цикл с выходом
total = 0
while True:
    number = int(input("Введите число (отрицательное для выхода): "))
    if number < 0:
        break
    total += number
print(f"Сумма: {total}")

# Пример: Вывод только чётных чисел
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 != 0:
        continue  # пропускаем нечётные
    print(f"Чётное число: {num}")

# Пример: Поиск числа в списке
numbers = [1, 3, 5, 7, 9]
search_for = 4

for num in numbers:
    if num == search_for:
        print(f"Число {search_for} найдено!")
        break
else:
    print(f"Число {search_for} не найдено в списке.")

# Пример бесконечного цикла с задержкой:
#import time
#while True:
#    print("Программа работает. Нажмите Ctrl+C для остановки.")
#    time.sleep(2)  # задержка в 2 секунды

# Вывод элементов двумерного списка
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:        # внешний цикл по строкам
    for element in row:   # внутренний цикл по элементам строки
        print(element, end=" ")
    print()  # переход на новую строку после каждой строки матрицы

# Таблица умножения
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} × {j} = {i * j}")
    print("-" * 20)  # разделитель между таблицами для разных i

# Поиск элемента во вложенном списке
groups = [["Анна", "Иван"], ["Пётр", "Мария", "Елена"], ["Алексей"]]
search_name = "Мария"

for group in groups:
    for name in group:
        if name == search_name:
            print(f"Найдено в группе {group}")
            break  # выход из внутреннего цикла
    else:
        continue  # выполняется, если внутренний цикл не нашёл
    break  # выход из внешнего цикла, если нашли

