from functools import cache
from numba import jit
from decorators import timeit
from random import randint


@timeit
def samples_without_numba(samples):
    x = [randint(0, samples) for x in range(samples)]
    set_len = len(set(x))
    list_len = len(x)
    # print("Collision %:",(list_len-set_len)/list_len*100)


@timeit
@jit(nopython=True)
def samples_with_numba(samples):
    x = [randint(0, samples) for x in range(samples)]
    set_len = len(set(x))
    list_len = len(x)
    # print("Collision %:",(list_len-set_len)/list_len*100)


sample_size = 10000
print("Sample size: ", sample_size)
samples_with_numba(sample_size / 10000)
samples_without_numba(sample_size * 100)
samples_with_numba(sample_size * 100)
samples_with_numba(sample_size * 1000)
