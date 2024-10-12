#name = input("Введите ваше имя: ")
#print("Привет, " + name)

from datetime import datetime

current_time = datetime.now()  # получение текущего времени
print(current_time)  # вывод текущей даты и времени

# Пример форматирования даты
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Текущая дата и время: {formatted_time}")