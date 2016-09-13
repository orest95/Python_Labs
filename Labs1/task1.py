#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

a = int(input("Введіть a:"))
x = int(input("Введіть b:"))
c = int(input("Введіть c:"))

f1 = (math.sqrt((math.exp(x))-(math.cos(x**2*a**5)**4))+(math.atan(a-x**5)**4))
f2 = (math.sqrt(math.fabs(a+x*c**4)))

r = f1/f2

print("Результат: ", r)