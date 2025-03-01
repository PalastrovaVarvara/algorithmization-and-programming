# Построить оси координат и заполнить поле графика кружками со случайными координатами, 
# сгенерированные координаты необходимо записать в текстовый файл и разделить их знаком табуляции
import matplotlib.pyplot as plt #pip install matplotlip
import random
import math
import numpy as np

def generate_cicrcles (x_min, x_max, y_min, y_max, count, output_file): 
    cicles = []
    for _ in range(count): 
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        cicles.append((x, y))

    with open(output_file, "w", encoding="utf-8") as file:
        for x, y in cicles:
            file.write(f"{x:.2f}\t{y:.2f}\n") 
    print(f"Координаты записаны в файл 'output_file'. ")   

    plt.figure(figsize = (8, 8))

    plt.axhline(0, color='black', linewidth = 1.5)
    plt.axvline(0, color='black', linewidth = 1.5)

    for x, y in cicles:
        plt.scatter(x, y, s=100, color = "skyblue", edgecolor = "black", zorder = 5)

    plt.xlim(x_min, x_max)
    plt.xlim(y_min,y_max)
    plt.grid(True, linestyle = "--", alpha = 0.5)
    plt.title("Случайные координаты на координатной плоскосити") 
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

#generate_cicrcles(
#   x_min = 0,
#   x_max= 50,
#   y_min = 0,
#   y_max = 50,
#   count = 1000,
#   output_file='generate_cicrcles.txt')
    
# Заполнить поле графика кружочками, расположенными в большом круге, 
# центром которого является центр плоскости. Пусть R - размер радиуса большого круга в пикселях, 
# в котором разрешены отображения пикселей
def generate_r(radius, count, output_file):
    points = []
    for _ in  range(count):
        while True:
            x = random.uniform(- radius, radius)
            y = random.uniform(- radius, radius)
            if math.sqrt(x**2 + y**2) <= radius:
                points.append((x, y))
                break

    with open(output_file, "w", encoding="utf-8") as file:
            for x, y in points:
                file.write(f"{x:.2f}\t{y:.2f}\n") 
    print(f"Координаты записаны в файл 'output_file'. ") 

    plt.figure(figsize = (8, 8))

    plt.axhline(0, color='black', linewidth = 1.5)
    plt.axvline(0, color='black', linewidth = 1.5)

    circle = plt.Circle((0,0), radius, color = "lightgrey", alpha = 0.5, zorder = 1)
    plt.gca().add_patch(circle)

    for x, y in points:
        plt.scatter(x, y, s=100, color = "skyblue", edgecolor = "black", zorder = 5)

    plt.xlim(- radius, radius)
    plt.xlim(- radius, radius)
    plt.grid(True, linestyle = "--", alpha = 0.5)
    plt.title("Случайные координаты в круге") 
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.gca().set_aspect('equal', adjustable = 'box')
    plt.show()

#generate_r(
#    radius = 50,
#    count = 100,
#    output_file='generate_r.txt'
#)
# построить график y = cos(x) с определенным шагом и генерацией координат
def generate_gr(step, x_min, x_max, output_file):
    x_values = np.arange(x_min, x_max + step, step)
    y_values = np.cos(x_values)

    with open(output_file, "w", encoding="utf-8") as file:
            for x, y in zip(x_values, y_values):
                file.write(f"{x:.2f}\t{y:.2f}\n") 
    print(f"Координаты записаны в файл 'output_file'. ") 


    plt.figure(figsize = (10, 5))
    plt.plot(x_values, y_values, label = 'y=cos(x)', color = 'blue', marker = 'o', markersize = 4)

    plt.title("y=cos(x)")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True, linestyle = "--", alpha = 0.7)
    plt.axhline(0, color = 'black', linewidth = 1.5)
    plt.axvline(0, color = 'black', linewidth = 1.5)
    plt.legend()
    plt.show()

generate_gr(
    step = 0.5,
    x_min = -10,
    x_max = 10,
    output_file='generate_gr.txt'
)