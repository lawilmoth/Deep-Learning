import numpy as np
import time
import random

# Creates two lists of 1 million random numbers
n = 1_000_000
a = [random.random() for i in range(n)]
b = [random.random() for i in range(n)]

def time_list_comprehension(a, b):
    start = time.time()
    # Use a list comprehension to multiply each element of a by the corresponding element of b
    # Put your code here

    

    end = time.time()
    return end - start

t = time_list_comprehension(a, b)
print(f"List comprehension time {t}")


def time_for_loop(a, b):
    start = time.time()
    # Use a for loop to multiply each element of a by the corresponding element of b
    # Put your code here


    end = time.time()
    return end - start

t = time_list_comprehension(a, b)
print(f"List comprehension time {t}")


def time_numpy_array(a, b):
    start = time.time()
    # Use a numpy array to multiply each element of a by the corresponding element of b
    # Put your code here
    


    end = time.time()
    return end - start

t = time_list_comprehension(a, b)
print(f"List comprehension time {t}")