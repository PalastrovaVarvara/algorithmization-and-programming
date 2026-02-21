## Простой условный оператор if
#
#age = int(input("Сколько вам лет? "))
#if age >= 21:
#    print("Здорово!")  # Выполнится только если age >= 21
#print("Программа продолжается")  # Выполнится всегда
#
## Конструкция if-else: два пути развития
#
#y = 4
#if y > 5:
#    print("y больше 5")
#else:
#    print("y не больше 5")  # Выполнится, так как 4 > 5 ложно
#
#age = int(input("Введите ваш возраст: "))
#if age >= 18:
#    print("Вы совершеннолетний")
#else:
#    print("Иди делай уроки")
#
## Множественный выбор: конструкция if-elif-else
#
#x, y = 5, -8
#if x > 0 and y > 0:
#    print("первая четверть")
#else:
#    if x < 0 and y > 0:
#        print("вторая четверть")
#    else:
#        if x < 0 and y < 0:
#            print("третья четверть")
#        else:
#            print("четвертая четверть")
#
#x, y = 5, -8
#if x > 0 and y > 0:
#    print("первая четверть")
#elif x < 0 and y > 0:
#    print("вторая четверть")
#elif x < 0 and y < 0:
#    print("третья четверть")
#else:
#    print("четвертая четверть")
#
#score = 85
#if score >= 90:
#    print("Оценка A")
#elif score >= 75:
#    print("Оценка B")
#elif score >= 65:
#    print("Оценка C")
#else:
#    print("Оценка D")
#
#
## Вложенные условные конструкции
#
#age = 25
#if age >= 18:
#    print("Добро пожаловать в клуб!")
#    if age >= 21:
#        print("Можете заказывать алкогольные напитки")
#    else:
#        print("Алкоголь запрещен")
#else:
#    print("Извините, вход только с 18 лет")
#
#
## Что может быть условием?
#
## Проверка принадлежности диапазону
#x = 15
#if x >= 0 and x < 100:
#    print("x в диапазоне [0, 99]")
#
## Python позволяет упрощённую запись
#if 0 <= x < 100:
#    print("x в диапазоне [0, 99]")  # Аналогично
#
## Проверка кредитоспособности
#age = 35
#salary = 60000
#if age >= 21 and age <= 65 and salary >= 30000:
#    print("Кредит одобрен")
#else:
#    print("В кредите отказано")
#
#
## Проверка погоды
#weather = "дождь"
#if weather == "дождь" or weather == "снег" or weather == "град":
#    print("Лучше остаться дома")
#else:
#    print("Хорошая погода для прогулки")
#
#
## Проверка истинности
#items = {}
## Вместо
#if len(items) > 0:
#    print("Список не пуст")
#
## Можно писать (если items не пуст)
#if items:
#    print("Список не пуст")
#
#
## Тернарный оператор (условное выражение)
## Обычная запись
#number = 10
#if number > 0:
#    result = "Положительное"
#else:
#    result = "Не положительное"
#
## Компактная запись
#result = "Положительное" if number > 0 else "Не положительное"
#
## Определение статуса пользователя
#user_points = 150
#status = "VIP" if user_points >= 100 else "Обычный"
#
## Установка скидки
#purchase_amount = 5000
#discount = 10 if purchase_amount > 3000 else 5
#
## Проверка чётности
#num = 7
#parity = "чётное" if num % 2 == 0 else "нечётное"
#
## Лучшие практики написания условий
### Используйте "guard clauses" для уменьшения вложенности
#### Плохо
def shipping_cost(country, items):
    if country is not None:
        if len(items) > 0:
            if len(items) > 10:
                return 0
            else:
                return 5
        else:
            return 0
    else:
        raise ValueError("invalid country")
print(shipping_cost("US", [2,5,6]))
    
### Хорошо
def shipping_cost(country, items):
    if country is None:
        raise ValueError("invalid country")
    
    if not items:  # Пустая корзина
        return 0
    
    if country == "US":
        return 0 if len(items) > 10 else 5
    
    return 20  # Другие страны
print(shipping_cost("US", [2,5,6]))
print(shipping_cost("RF", [2,5,6]))

# Будьте явны в проверках
value = 0
# Плохо
if not value:
    result = value
    # Это может сработать и для 0, и для False, и для пустой строки

# Хорошо
if value is None:
    result = value
    # Только если value действительно None

# Используйте двойные неравенства для диапазонов
x = 10
# Вместо
if x >= 0 and x < 100:
    result = x
# Пишите
if 0 <= x < 100:
    result = x

# Группируйте сложные условия с помощью скобок
first_letter = "a" 
last_letter = "я"

if (first_letter == "а" or first_letter == "А") and (last_letter == "я" or last_letter == "Я"):
    print("Верно")


# Простые литеральные шаблоны

def get_http_status_message(code):
    match code:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 301:
            return "Moved Permanently"
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return f"Unknown status code: {code}"

print(get_http_status_message(404))  # Not Found
print(get_http_status_message(418))  # Unknown status code: 418

color = input("Введите цвет светофора: ")
match color:
    case 'красный':
        print('Стоп.')
    case 'жёлтый':
        print('Внимание!')
    case 'зелёный':
        print('Можно ехать.')
    case _:
        print('Некорректное значение.')


# Объединение шаблонов (or-patterns)
def classify_day(day):
    match day.lower():
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Будний день"
        case "saturday" | "sunday":
            return "Выходной"
        case _:
            return "Неверный день"

print(classify_day("Saturday"))  # Выходной
print(classify_day("Wednesday")) # Будний день

# Захват переменных в шаблонах

def parse_command(command):
    match command.split():
        case ["quit"]:
            return "Завершение программы"
        case ["hello", name]:
            return f"Привет, {name}!"
        case ["add", x, y]:
            return f"Сумма: {int(x) + int(y)}"
        case _:
            return "Неизвестная команда"

print(parse_command("hello Alice"))  # Привет, Alice!
print(parse_command("add 3 5"))      # Сумма: 8
print(parse_command("quit"))         # Завершение программы


# Важное различие: константы vs захват

QUIT = "quit"  # Константа

user_input = "quit"
match user_input:
    case QUIT:  # ОШИБКА! Это захват в переменную QUIT, а не сравнение с константой!
        print("Этот код выполнится всегда")


class Commands:
    QUIT = "quit"
    HELP = "help"

user_input = "quit"
match user_input:
    case Commands.QUIT:  # Сравнение с константой
        print("Завершение")
    case Commands.HELP:
        print("Справка")

# Шаблоны последовательностей
## Пример: работа с точками на плоскости

def process_point(point):
    match point:
        case (0, 0):
            return "Начало координат"
        case (x, 0):
            return f"На оси X в точке {x}"
        case (0, y):
            return f"На оси Y в точке {y}"
        case (x, y):
            return f"Точка ({x}, {y})"
        case _:
            return "Неверный формат точки"

print(process_point((0, 0)))   # Начало координат
print(process_point((5, 0)))   # На оси X в точке 5
print(process_point((3, 7)))   # Точка (3, 7)

## Шаблоны с произвольной длиной (*)

def analyze_sequence(seq):
    match seq:
        case []:
            return "Пустая последовательность"
        case [single]:
            return f"Один элемент: {single}"
        case [first, second]:
            return f"Пара: {first}, {second}"
        case [first, *middle, last]:
            return f"Первый: {first}, последний: {last}, середина: {len(middle)} элементов"

print(analyze_sequence([]))              # Пустая последовательность
print(analyze_sequence([42]))            # Один элемент: 42
print(analyze_sequence([1, 2, 3, 4, 5])) # Первый: 1, последний: 5, середина: 3 элементов

## Вложенные шаблоны последовательностей

def process_matrix_row(row):
    match row:
        case [[a, b], [c, d]]:
            return f"Блок 2x2: {a}, {b}, {c}, {d}"
        case [first_row, *rest]:
            return f"Первая строка: {first_row}, осталось строк: {len(rest)}"

print(process_matrix_row([[1, 2], [3, 4]])) # Блок 2x2: 1, 2, 3, 4

# Шаблоны отображений (словарей)
## Пример: обработка API-ответов
def handle_api_response(response):
    match response:
        case {"status": "success", "data": data}:
            return f"Успех! Данные: {data}"
        case {"status": "error", "message": msg}:
            return f"Ошибка: {msg}"
        case {"status": "error", "code": code, "message": msg}:
            return f"Ошибка {code}: {msg}"
        case {"status": status}:
            return f"Неизвестный статус: {status}"
        case _:
            return "Неверный формат ответа"

print(handle_api_response({"status": "success", "data": [1, 2, 3]})) # Успех! Данные: [1, 2, 3]

print(handle_api_response({"status": "error", "message": "Not found"})) # Ошибка: Not found