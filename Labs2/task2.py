#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open('TF1_1.txt', 'w')
n = int(input("Введіть кількість рядків: "))

i = 1
while i <= n:
    s = input("Введіть рядок: ")
    f.write(s + ' ')
    i += 1

f.close()
f = open('TF1_1.txt', 'r')
f2 = open('TF1_2.txt', 'w')

a = f.read().split(' ')

i = 0
while i < len(a):
    j = 1
    s = a[i]
    while j < len(s):
        if s[j] == s[j-1]:
            if s[j] == "," or s[j] == "." or s[j] == "!" or s[j] == "?":
                s.pop()
            f2.write(s + "\n")
        j += 1
    i += 1

f2.close()
f2 = open('TF1_2.txt', 'r')
for line in f2:
    print(line)