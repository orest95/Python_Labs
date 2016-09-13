#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

x = int(input("Введiть x:"))
y = int(input("Введiть y:"))
z = int(input("Введiть z:"))

a = int(input("Введiть a:"))
b = int(input("Введiть b:"))

c = int(input("Введiть c:"))
d = int(input("Введiть d:"))


if (c <= x and x <= d and c <= y and y <= d and c <= z and z <= d):
    print("Виконується умова 1.")
    result = max(x, max(y, z))
    
elif (c > x and x > d and c > y and y > d and c > z and z > d):
    print("Виконується умова 2.")
    result = min(x, min(y, z))
else:
    print("Виконується умова 3.")
    result = (a + b) / 2

print("Результат: ", result)


