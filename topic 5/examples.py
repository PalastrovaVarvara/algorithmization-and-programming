def greet():
    print("Привет, мир!")

# Вызов функции
greet()  # Выведет: Привет, мир!

def show_menu():
    print("=== Меню программы ===")
    print("1. Начать игру")
    print("2. Правила")
    print("3. Выход")

# Использование
show_menu()  # При каждом вызове будет выводиться меню

def greet_user(name):
    print(f"Привет, {name}!")

greet_user("Анна")   # Выведет: Привет, Анна!
greet_user("Иван")   # Выведет: Привет, Иван!

def print_sum(a, b):
    print(f"Сумма {a} и {b} равна {a + b}")

print_sum(5, 3)      # Выведет: Сумма 5 и 3 равна 8
print_sum(10, 25)    # Выведет: Сумма 10 и 25 равна 35

def add(a, b):
    result = a + b
    return result

# Сохраняем результат в переменную
summa = add(5, 3)
print(summa)  # 8

# Используем результат непосредственно
print(add(10, 20) * 2)  # 60

def only_even(numbers):
    for x in numbers:
        if x % 2 != 0:
            return False  # Нашли нечётное — сразу возвращаем False
    return True  # Все числа чётные

print(only_even([2, 4, 6]))  # True
print(only_even([2, 3, 6]))  # False

def do_nothing():
    pass

result = do_nothing()
print(result)  # None

# Функция print() тоже возвращает None
print(print("Привет"))  # Привет\nNone


def get_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return total, count, average  # Возвращаем три значения

# Результат можно принять как кортеж
stats = get_stats([1, 2, 3, 4, 5])
print(stats)  # (15, 5, 3.0)

# Или распаковать в отдельные переменные
total, count, avg = get_stats([1, 2, 3, 4, 5])
print(f"Сумма: {total}, количество: {count}, среднее: {avg}")


mage = "I use my best spell for protection."
archer = "My people are ready! What's next?"
enemy = "AAAAaaarrrrrggghhhhh"

# Проверка для Mage
if len(mage) == 0:
    print("Строка пуста!")
else:
    if mage[-1] in "!.?":
        print(True)
    else:
        print(False)


def exam_string(string):
    """Проверяет, что строка не пуста и оканчивается знаком препинания"""
    if len(string) == 0:
        print("Строка пуста!")
        return None
    else:
        return string[-1] in "!.?"

mage = "I use my best spell for protection."
archer = "My people are ready! What's next?"
enemy = "AAAAaaarrrrrggghhhhh"

print(exam_string(mage))   # True
print(exam_string(archer)) # True
print(exam_string(enemy))  # False


def user_info(name, age, city):
    print(f"Имя: {name}, Возраст: {age}, Город: {city}")

# Позиционная передача — порядок важен!
user_info("Анна", 25, "Москва")  # Имя: Анна, Возраст: 25, Город: Москва
user_info("Москва", 25, "Анна")  # Ошибка логики — порядок нарушен!

def user_info(name, age, city):
    print(f"Имя: {name}, Возраст: {age}, Город: {city}")

# Именованная передача — порядок не важен
user_info(age=25, city="Москва", name="Анна")
# Имя: Анна, Возраст: 25, Город: Москва


def greet(name, greeting="Здравствуйте"):
    print(f"{greeting}, {name}!")

greet("Анна")                    # Здравствуйте, Анна!
greet("Иван", "Привет")          # Привет, Иван!
greet(name="Пётр", greeting="Добрый вечер")  # Добрый вечер, Пётр!


def describe_pet(name, animal_type="собака", age=None):
    print(f"Это {animal_type} по имени {name}")
    if age:
        print(f"Возраст: {age} лет")

# Разные способы вызова
describe_pet("Рекс")                          # позиционный + значения по умолчанию
describe_pet("Мурка", "кошка")                 # два позиционных
describe_pet("Кеша", animal_type="попугай")     # позиционный + именованный
describe_pet(animal_type="хомяк", name="Хома") # все именованные


def change_number(x):
    x = x + 10
    print(f"Внутри функции: {x}")  # 15

num = 5
change_number(num)
print(f"Снаружи функции: {num}")   # 5 — не изменилось!


def add_element(lst):
    lst.append(100)
    print(f"Внутри функции: {lst}")  # [1, 2, 3, 100]

my_list = [1, 2, 3]
add_element(my_list)
print(f"Снаружи функции: {my_list}")  # [1, 2, 3, 100] — изменилось!

def reassign_list(lst):
    lst = [100, 200, 300]  # Создаём новый локальный список
    print(f"Внутри функции: {lst}")  # [100, 200, 300]

my_list = [1, 2, 3]
reassign_list(my_list)
print(f"Снаружи функции: {my_list}")  # [1, 2, 3] — не изменилось!

# Области видимости переменных

def my_func():
    y = 10  # локальная переменная
    print(f"Внутри функции: {y}")

my_func()  # Внутри функции: 10
# print(y)  # Ошибка! NameError: name 'y' is not defined


x = 5  # глобальная переменная

def show_global():
    print(f"Внутри функции: {x}")  # можно читать глобальные переменные

show_global()  # Внутри функции: 5
print(f"Снаружи: {x}")  # Снаружи: 5


x = "глобальная"

def outer():
    x = "внешняя"
    def inner():
        x = "внутренняя"
        print(x)  # Поиск начинается с Local — находит "внутренняя"
    inner()
    print(x)  # Поиск в outer — находит "внешняя"

outer()
print(x)  # Поиск в глобальной области — находит "глобальная"


x = 10  # глобальная

def change_x():
    x = 20  # создаётся локальная переменная!
    print(f"Внутри функции: {x}")  # 20

change_x()
print(f"Снаружи: {x}")  # 10 — глобальная не изменилась!


x = 10  # глобальная

def change_x():
    global x  # объявляем, что будем работать с глобальной x
    x = 20
    print(f"Внутри функции: {x}")  # 20

change_x()
print(f"Снаружи: {x}")  # 20 — глобальная изменилась!


def outer():
    count = 0
    
    def inner():
        nonlocal count  # говорим, что count берётся из внешней функции
        count += 1
        return count
    
    return inner

counter = outer()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3


def sum_all(*args):
    print(f"Тип args: {type(args)}")  # <class 'tuple'>
    print(f"Аргументы: {args}")
    return sum(args)

print(sum_all(1, 2, 3))        # Сумма: 6
print(sum_all(5, 10, 15, 20))  # Сумма: 50
print(sum_all(42))              # Сумма: 42


def print_info(**kwargs):
    print(f"Тип kwargs: {type(kwargs)}")  # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Анна", age=25, city="Москва")
# name: Анна
# age: 25
# city: Москва

print_info(product="Ноутбук", price=75000, in_stock=True)


def complex_function(a, b, c=10, *args, option=True, **kwargs):
    print(f"a={a}, b={b}, c={c}")
    print(f"args: {args}")
    print(f"option: {option}")
    print(f"kwargs: {kwargs}")

complex_function(1, 2, 3, 4, 5, 6, option=False, x=100, y=200)
# a=1, b=2, c=3
# args: (4, 5, 6)
# option: False
# kwargs: {'x': 100, 'y': 200}


def factorial(n):
    """Вычисляет факториал числа n (n!).
    
    Аргументы:
        n (int): Неотрицательное целое число
        
    Возвращает:
        int: Факториал числа n
        
    Исключения:
        ValueError: Если n < 0
    """
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определён")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Доступ к документации
print(factorial.__doc__)
help(factorial)

# Рекурсия
def factorial(n):
    # Базовый случай
    if n <= 1:
        return 1
    
    # Рекурсивный шаг
    return n * factorial(n - 1)

print(factorial(5))  # 120
print(factorial(0))  # 1


def fibonacci(n):
    """Возвращает n-е число Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Первые 10 чисел Фибоначчи
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")


# Обычная функция
def square(x):
    return x ** 2

# Лямбда-функция
square_lambda = lambda x: x ** 2

print(square(5))        # 25
print(square_lambda(5)) # 25

# Лямбда с несколькими параметрами
add = lambda a, b: a + b
print(add(3, 7))  # 10

# Лямбда без параметров
greet = lambda: "Hello, World!"
print(greet())  # Hello, World!


students = [
    {"name": "Анна", "grade": 85},
    {"name": "Иван", "grade": 92},
    {"name": "Мария", "grade": 78}
]

# Сортировка по оценкам
sorted_by_grade = sorted(students, key=lambda student: student["grade"])
print(sorted_by_grade)

# Сортировка по длине имени
words = ["python", "java", "c", "javascript"]
sorted_by_len = sorted(words, key=lambda word: len(word))
print(sorted_by_len)  # ['c', 'java', 'python', 'javascript']


# map — применение функции к каждому элементу
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# filter — отбор элементов по условию
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# reduce — последовательное применение функции
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120 (1*2*3*4*5)


def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

# Присваивание переменной
my_func = shout
print(my_func("Hello"))  # HELLO

# Хранение в списке
functions = [shout, whisper]
for func in functions:
    print(func("Hello"))  # HELLO\nhello

# Передача как аргумент
def apply(func, value):
    return func(value)

print(apply(shout, "test"))   # TEST
print(apply(whisper, "TEST")) # test

# Возврат из функции
def get_operation(operation):
    if operation == "double":
        return lambda x: x * 2
    elif operation == "square":
        return lambda x: x ** 2

double = get_operation("double")
print(double(5))  # 10

square = get_operation("square")
print(square(5))  # 25