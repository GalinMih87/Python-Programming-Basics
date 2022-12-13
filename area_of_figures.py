from math import pi

type_of_the_figure = input()
result = 0
if type_of_the_figure == "square":       # пресмята лице на квадрат
    side = float(input())
    result = side * side
elif type_of_the_figure == "rectangle":  # пресмята лице на правоъгълник
    said_a = float(input())
    said_b = float(input())
    result = said_a * said_b
elif type_of_the_figure == "circle":     # пресмята лице на кръг
    radius = float(input())
    result = pi * (radius ** 2)
else:                                    # пресмята лице на триъгълник                
    side = float(input())
    height = float(input())
    result = side * height / 2
print(f'{result:.3f}')
