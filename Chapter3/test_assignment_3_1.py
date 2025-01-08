import pytest
import numpy as np
import random
import time
from assignment_3_1 import time_for_loop, time_list_comprehension, time_numpy_array


def large_arrays():
    n = 1_000_000
    a = [random.random() for i in range(n)]
    b = [random.random() for i in range(n)]
    return a, b


def samples():
    a, b = large_arrays()
    a_a = np.array(a)
    b_a = np.array(b)
    t1 = time.time()
    a_a * b_a
    c = time.time() - t1
    t1 = time.time()
    [a[i] * b[i] for i in range(len(a))]
    d = time.time() - t1
    t1 = time.time()

    x = []
    for i in range(len(a)):
        x.append(a[i] * b[i])
    e = time.time() - t1 
    return d, e, c




def test_time_list_comprehension():
    a,b = large_arrays()
    answer = time_list_comprehension(a,b)
    duration = samples()[0]
    assert (duration - duration *.2 )< answer 
    assert answer < (duration + duration *.2 )

def test_time_for_loop():
    a,b = large_arrays()
    answer = time_for_loop(a,b)
    duration = samples()[1]
    assert (duration - duration *.2) < answer 
    assert answer < (duration + duration *.2) 

def test_time_numpy_array():
    a,b = large_arrays()
    answer = time_numpy_array(a,b)
    duration = samples()[2]
    assert (duration - duration *.1) < answer 
    assert answer < (duration + duration *.1 )

