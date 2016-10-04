#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = int(input("Введіть натуральне число: "))
n = ""
def IntToByte(x):
    n = ""
    while x > 0:
        y = str(x % 2)
        n = y + n
        x = int(x / 2)

    print(n)

IntToByte(321)