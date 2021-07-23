import timeit
import math

def fact_recursion(num):
    if num < 0:
        return 0
    if num == 0:
        return 1

    return num * fact_recursion(num - 1)

# 151 secs
print(timeit.timeit("fact_recursion(500)", globals=globals()));