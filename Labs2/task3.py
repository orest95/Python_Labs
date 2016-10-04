#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = 'This is a simple test message for test'
s = a.split(' ')

n = 0
i = 0
while i < len(s):
    if s[i] == "test":
        n += 1
    i += 1

print(n)