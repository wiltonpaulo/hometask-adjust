#!/usr/bin/python3

import random
numbers = list(range(1,11))
random.shuffle(numbers)

for item in numbers:
    print(item)
