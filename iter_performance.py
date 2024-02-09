###THIS script compares performance of different iteration approaches###  

from timeit import timeit
import numpy
from numba import njit


L = [0] * 100_000_000
numpy_L = numpy.zeros((100_000_000), dtype='int')


def while_cicle(l):
    i=0
    length = len(l)
    while i < length:
        l[i] += 1
        i += 1
    return l

def map_method(l):
    return list(map(lambda x: x+1, l))

def for_cicle(l):
    for i in range(len(l)):
        l[i] += 1
    return l

def comprehensive(l):
    return [i+1 for i in l]

@njit
def njit_for_cicle(l:numpy):
    for i in range(len(l)):
        l[i] += 1
    return l

def numpy_method(l):
    return l + 1


print ('Testing iteration methods preformance...')
print()
print(f"While cicle: {timeit('while_cicle(L)', number=1, globals=globals()):.3f} seconds")
print(f"Map method: {timeit('map_method(L)', number=1, globals=globals()):.3f} seconds")
print(f"For cicle: {timeit('for_cicle(L)', number=1, globals=globals()):.3f} seconds")
print(f"Comprehensive: {timeit('comprehensive(L)', number=1, globals=globals()):.3f} seconds")
print(f"Numpy method 2nd time: {timeit('numpy_method(numpy_L)', number=1, globals=globals()):.3f} seconds")
print(f"Njit decorator 1st time: {timeit('njit_for_cicle(numpy_L)', number=1, globals=globals()):.3f} seconds")
print(f"Njit decorator 2nd time: {timeit('njit_for_cicle(numpy_L)', number=1, globals=globals()):.3f} seconds")
