import pytest

from assignment import (
    labeling_classes,
    types_of_features_2,
    types_of_features_3,
    types_of_features_4,
    inspect_data,
    interpolation_problem,
    extrapolation_problem,
    prior_class_probabilities,
    data_set_size,
    data_set_size_2
)

def test_labeling_classes():
    assert labeling_classes() == 6 

def test_types_of_features_2():
    assert types_of_features_2() == 'c'  

def test_types_of_features_3():
    assert types_of_features_3() == 'b'  

def test_types_of_features_4():
    assert types_of_features_4() == 'a'  

def test_inspect_data():
    assert inspect_data() == 'increases'  

def test_interpolation_problem():
    assert interpolation_problem() == pytest.approx(27.9, 0.1)  # Assuming the predicted age in 2025 is around 27.9

def test_extrapolation_problem():
    assert extrapolation_problem() == pytest.approx(150.6, 0.1)  # Assuming the predicted age in 2800 is around 245.5

def test_prior_class_probabilities():
    assert prior_class_probabilities() == '10:1'  # Assuming this is the correct answer

def test_data_set_size():
    assert data_set_size() == 'All of it'  # Assuming this is the cheeky answer

def test_data_set_size_2():
    assert data_set_size_2() == 'diminishing'  # Assuming this is the correct answer