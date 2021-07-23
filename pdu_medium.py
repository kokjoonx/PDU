import timeit
import math

def fact_loop(num):
    if num < 0:
        return 0
    if num == 0:
        return 1

    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial

# 245 secs
print(timeit.timeit("fact_loop(900)", globals=globals()));