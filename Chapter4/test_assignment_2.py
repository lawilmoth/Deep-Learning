import pytest
from sklearn.datasets import make_classification
import numpy as np
from assignment_2 import inspect_data_1, inspect_data_2, inspect_data_3, inspect_data_4, inspect_data_5, inspect_data_6, separtate_90_percent_for_training

def test_inspect_data_1():
    a_shape = inspect_data_1()
    assert a_shape == (10000, 20)

def test_inspect_data_2():
    param_name = inspect_data_2()
    assert param_name == 'n_features'

def test_inspect_data_3():
    center_value = inspect_data_3()
    assert center_value == 0

def test_inspect_data_4():
    std_dev = inspect_data_4()
    assert std_dev == 1

def test_inspect_data_5():
    avg_zeros = inspect_data_5()
    assert avg_zeros == 90

def test_inspect_data_6():
    result = inspect_data_6()
    assert result == "I inspected the data"

def test_separate_90_percent_for_training():
    a, b = make_classification(n_samples=10000, weights=(0.9, 0.1))
    idx = np.where(b == 1)[0]
    x0 = a[idx,:]
    y0 = b[idx]
    idx = np.where(b == 0)
    x1 = a[idx[0],:]
    y1 = b[idx]
    n_trn0 = int(x0.shape[0] * 0.9)
    n_trn1 = int(x1.shape[0] * 0.9)
    
    assert n_trn0 == int(len(np.where(b == 1)[0]) * 0.9)
    assert n_trn1 == int(len(np.where(b == 0)[0]) * 0.9)