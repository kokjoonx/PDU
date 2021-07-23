import timeit
import math

# 202 secs
print(timeit.timeit("math.factorial(2000)", setup="import math"));