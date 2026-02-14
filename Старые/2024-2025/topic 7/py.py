#with open("file.txt", "r", encoding='utf-8') as input_file: 
#    content = input_file.readlines() 
#
#with open("output.txt", "w", encoding='utf-8') as output_file: 
#    for line in content: 
#        output_file.write(f"Обработанная строка: {line}")

#with open("file.txt", "r", encoding='utf-8') as file:
#    #print(file.readlines())
#    #print(list(file))
#    #print(file.readline())
#    for line in file:
#            print(line)

#numbers = ['1 \n', '2 \n', '3 \n' ] 
#with open("numbers.txt", "w") as file: 
#    file.writelines(numbers)
#   # for number in numbers: 
#   #     file.write(f"{number}\n")


import os
#print(os.listdir())
#print(os.listdir('C:/Users/Asus-/OneDrive/Рабочий стол/AP/algorithmization-and-programming'))
#
#print(os.getcwd())

def print_dir(dir):
    all_files = os.walk(dir)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
        print(f'Директории: {",".join([file for file in catalog[1]])}')
        print(f'Файлы: {",".join([file for file in catalog[2]])}')
        print("-" * 40)

print_dir('C:/Users/Asus-/OneDrive/Рабочий стол/AP/algorithmization-and-programming')

try: 
    with open("file.txt", "r", encoding='utf-8') as file:
        print(file.readlines())
except FileNotFoundError:
    print("Файл не найден")
except IOError:
    print("Ошибка ввода-вывода")