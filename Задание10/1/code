# -- coding: utf-8 --
def max_krat(x, matrix):
    count = 0 
    max_element = 0
    
    for row in matrix:
        for element in row:
            if element % x == 0:
                count += 1
                if element > max_element:
                    max_element = element
    
    return count, max_element

matrix = []
with open('Ivanov_Y232_vvod.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.strip().split())) 
        matrix.append(row)
    print("Матрица просчитана:")
    for row in matrix:
        print(row)

x = int(input('Введите число x:'))

count, max_element = max_krat(x, matrix)

with open('Ivanov_Y232_vivod.txt', 'w') as file:
    print(f"Кол-во кратных {x}: {count}", file=file)
    print(f"Наибольший кратный {x}: {max_element}", file=file)
