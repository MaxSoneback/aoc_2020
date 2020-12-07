# This one was just for fun

import random
import time
from utils import import_data
data = import_data(1, __file__, True)

pair_not_found = True
num1 = num2 = num3 = 0

time_start = time.time()
while pair_not_found:
    r1 = random.randint(0, len(data) - 1)
    r2 = random.randint(0, len(data) - 1)
    r3 = random.randint(0, len(data) - 1)
    num1 = data[r1]
    num2 = data[r2]
    num3 = data[r3]

    if num1 + num2 + num3 == 2020:
        pair_not_found = False

time_end = time.time()
print(num1 * num2 * num3)
print( f' Execution time: {time_end - time_start}')