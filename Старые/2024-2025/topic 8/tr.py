import numpy as np
import matplotlib.pyplot as plt

def generate_cosine_graph(step, x_min, x_max, output_file):
    """
    Генерирует график функции y = cos(x) с заданным шагом и сохраняет координаты в файл.
    
    :param step: Шаг изменения x
    :param x_min: Минимальное значение x
    :param x_max: Максимальное значение x
    :param output_file: Имя выходного файла для сохранения координат
    """
    # Генерация значений x и вычисление y = cos(x)
    x_values = np.arange(x_min, x_max + step, step)
    y_values = np.cos(x_values)
    
    # Запись координат в файл
    with open(output_file, "w", encoding="utf-8") as file:
        for x, y in zip(x_values, y_values):
            file.write(f"{x:.2f}\t{y:.2f}\n")
    print(f"Координаты записаны в файл '{output_file}'.")
    
    # Построение графика
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, label="y = cos(x)", color="blue", marker='o', markersize=4)
    
    # Настройка графика
    plt.title("График функции y = cos(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.axhline(0, color="black", linewidth=1.5)
    plt.axvline(0, color="black", linewidth=1.5)
    plt.legend()
    plt.show()

# Вызов функции
generate_cosine_graph(
    step=0.5,      # Шаг изменения x
    x_min=-10,     # Минимальное значение x
    x_max=10,      # Максимальное значение x
    output_file="cosine_coordinates.txt"
)