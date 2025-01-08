import pytest
import numpy as np
from assignment_3_2 import *

def test_create_array():
    arr = create_array()
    assert arr.size == 6
    assert arr.shape == (6,)
    assert arr.dtype == np.int64

def test_create_array_2():
    arr = create_array_2()
    assert arr.size == 6
    assert arr.shape == (6,)
    assert arr.dtype == np.float32

def test_create_array_3():
    arr = create_array_3()
    assert arr.shape == (3, 3)
    assert np.all(arr == 0)

def test_create_array_4():
    arr = create_array_4()
    assert arr.shape == (3, 3, 3)
    assert np.all(arr == 1)

def test_create_array_5():
    arr = create_array_5()
    assert arr.shape == (2, 3, 4)
    assert np.all(arr == 9)

def test_access_array():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    elem = access_array(arr)
    assert elem == 9

def test_create_array_6():
    arr = create_array_6()
    assert arr.shape == (2, 5, 3)
    assert arr[1, 1, 0] == 1

def test_load_csv(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    file = d / "example.csv"
    file.write_text("1,2,3\n4,5,6\n7,8,19")
    arr = load_csv(file)
    assert arr[2, 2] == 20

def test_create_and_save_array(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    file = d / "example_2.npz"
    create_and_save_array()
    data = np.load(file)
    assert np.all(data['a'] == 9)
    assert np.all(data['b'] == 8)

def test_load_array_from_image():
    arr = load_array_from_image()
    from PIL import Image
    im = Image.load("Chapter3/at.jpg")
    im_array = np.array(im)
    assert isinstance(arr, np.ndarray)
    assert im_array.shape == arr.shape
    assert np.all(im_array == arr)


def test_inspect_data():
    result = inspect_data()
    assert isinstance(result, str)