#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

a = int(input("Введiть a:"))
x = int(input("Введiть x:"))

esp = float(input("Введiть esp:"))



#while math.fabs(d) > eps:
#    k += 1;
#    fk *= k;
#    fk2 *= fk;
#    d = math.sin(a**k + x**k)/fk2;
#    s += d;

k = 1
fn = stax=st3=1
d = math.sin(1)/2
s = d

while math.fabs(d)>esp:
    k += 1;
    fn *= k;
    st3 *= 3;
    stax *= (a+x);
    d = (((-1)**k)*math.log(x**(2*k)))/((2**k)+k*k);
    s += d;


print("Результат: ", s)
print("Кiлькiсть доданкiв: ", k)
