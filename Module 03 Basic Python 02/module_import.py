from math import*
import calendar
from random import*
from time import sleep
from turtle import*
print(ceil(20.3))
print(floor(20.29))

ans = calendar.month(2024,2)
print(ans)


print(random())
print(randint(1,100))
# sleep(3)
print(choice(['meraz','rakib','beiman','hridoy','proyot']))



import turtle as t
from random import random

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)