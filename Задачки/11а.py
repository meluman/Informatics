import math

x = float(input('Введите число x: '))
y = float(input('Введите число y: '))
z = float(input('Введите число z: '))

a = ( (abs(x - 1) ** 0.5) - (abs(y) ** 1/3) ) / (1 + (x**2) / 2 + (y**2) / 4)
b = x * (math.atan(z) + math.e ** -(x + 3))

print('a = ', a)
print('b = ', b)