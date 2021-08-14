#!/usr/bin/python3
import random


number = random.randint(5,10)

print(number)
for i in range(1, 10):
    mul_table = number * i
    print("{} * {} = {}".format(number, i, mul_table))
