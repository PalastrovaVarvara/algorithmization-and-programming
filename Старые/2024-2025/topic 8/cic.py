import matplotlib.pyplot as plt
import random

def generate_random_circles_and_save(x_min, x_max, y_min, y_max, count, output_file):
    """
    Генерирует кружки с случайными координатами и записывает их в файл.
    
    :param x_min: Минимальное значение координаты X
    :param x_max: Максимальное значение координаты X
    :param y_min: Минимальное значение координаты Y
    :param y_max: Максимальное значение координаты Y
    :param count: Количество кружков
    :param output_file: Имя выходного текстового файла
    """
    # Генерация случайных координат
    circles = []
    for _ in range(count):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        circles.append((x, y))
    
    # Запись координат в текстовый файл
    with open(output_file, "w", encoding="utf-8") as file:
        for x, y in circles:
            file.write(f"{x:.2f}\t{y:.2f}\n")
    print(f"Координаты записаны в файл '{output_file}'.")
    
    # Построение графика
    plt.figure(figsize=(8, 8))
    
    # Рисуем оси координат
    plt.axhline(0, color='black', linewidth=1.5)  # Горизонтальная ось
    plt.axvline(0, color='black', linewidth=1.5)  # Вертикальная ось
    
    # Добавляем кружки
    for x, y in circles:
        plt.scatter(x, y, s=100, color="skyblue", edgecolor="black", zorder=5)
    
    # Настройка графика
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.title("Случайные кружки на координатной плоскости")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

# Вызов функции
generate_random_circles_and_save(
    x_min=0, x_max=50, 
    y_min=0, y_max=50, 
    count=1000, 
    output_file="random_coordinates.txt"
)