import pytest

from assignment import add_matrices, scalar_mult, multiply_matrices, multiply_matrices_1, multiply_matrices_2 , probability_distributions 
from assignment import probability_distributions_2, statistical_tests
def test_add_matrices():
    assert add_matrices([[1, 2], [3, 4]], [[2, 2], [2, 2]]) == [[3, 4], [5, 6]]
    assert add_matrices([[1, 0], [0, 1]], [[0, 1], [1, 0]]) == [[1, 1], [1, 1]]
    assert add_matrices([[1, 2, 3]], [[4, 5, 6]]) == [[5, 7, 9]]

def test_scalar_mult():
    assert scalar_mult(3, [[1, 2], [3, 4]]) == [[3, 6], [9, 12]]
    assert scalar_mult(0, [[1, 2], [3, 4]]) == [[0, 0], [0, 0]]
    assert scalar_mult(-1, [[1, -2], [-3, 4]]) == [[-1, 2], [3, -4]]

def test_multiply_matrices_1():
    assert multiply_matrices_1() == [[32]]

def test_multiply_matrices_2():
    assert multiply_matrices_2() == [[22, 28], [49, 64]]

def test_multiply_matrices():
    assert multiply_matrices([[1, 2, 3]], [[4], [5], [6]]) == [[32]]
    assert multiply_matrices([[1, 2, 3], [4, 5, 6]], [[1, 2], [3, 4], [5, 6]]) == [[22, 28], [49, 64]]
    assert multiply_matrices([[1, 2]], [[1, 2], [3, 4]]) == None

def test_probability_distributions():
    import codecs
    ans = codecs.decode("Havsbez Qvfgevohgvba", "rot_13")
    assert probability_distributions().title() == ans

def test_probability_distributions_2():
    import codecs
    ans1 = codecs.decode("Abezny Qvfgevohgvba", "rot_13")
    ans2 = codecs.decode("Tnhffvna Qvfgevohgvba", "rot_13")
    assert (probability_distributions_2().title() == ans1) or (probability_distributions_2().title() == ans2)

def test_statistical_tests():
    assert statistical_tests() == (ord("A") - 60) /100