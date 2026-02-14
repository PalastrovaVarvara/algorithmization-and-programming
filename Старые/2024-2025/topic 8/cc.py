import matplotlib.pyplot as plt
import random
import math

def generate_points_within_circle(radius, count, output_file):
    """
    Генерирует точки внутри круга радиуса R и записывает их координаты в файл.
    
    :param radius: Радиус круга (в пикселях)
    :param count: Количество точек
    :param output_file: Имя выходного файла
    """
    points = []
    for _ in range(count):
        while True:
            # Генерация случайных координат в квадрате [-R, R]
            x = random.uniform(-radius, radius)
            y = random.uniform(-radius, radius)
            # Проверка, находятся ли координаты внутри круга
            if math.sqrt(x**2 + y**2) <= radius:
                points.append((x, y))
                break
    
    # Запись координат в файл
    with open(output_file, "w", encoding="utf-8") as file:
        for x, y in points:
            file.write(f"{x:.2f}\t{y:.2f}\n")
    print(f"Координаты записаны в файл '{output_file}'.")
    
    # Построение графика
    plt.figure(figsize=(8, 8))
    
    # Рисуем оси координат
    plt.axhline(0, color='black', linewidth=1.5)  # Горизонтальная ось
    plt.axvline(0, color='black', linewidth=1.5)  # Вертикальная ось
    
    # Рисуем большой круг
    circle = plt.Circle((0, 0), radius, color="lightgrey", alpha=0.5, zorder=1)
    plt.gca().add_patch(circle)
    
    # Добавляем кружки
    for x, y in points:
        plt.scatter(x, y, s=100, color="skyblue", edgecolor="black", zorder=5)
    
    # Настройка графика
    plt.xlim(-radius, radius)
    plt.ylim(-radius, radius)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.title("Случайные точки внутри круга")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.gca().set_aspect('equal', adjustable='box')  # Круг сохраняет пропорции
    plt.show()

# Вызов функции
generate_points_within_circle(
    radius=10,  # Радиус круга
    count=50,   # Количество точек
    output_file="circle_points.txt"
)