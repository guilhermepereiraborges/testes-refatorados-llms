import pytest
from lottie.objects.base import LottieProp, LottieObject, CustomObject

@pytest.fixture
def lottie_object():
    return LottieObject()

@pytest.fixture
def custom_object():
    return CustomObject()

@pytest.fixture
def lottie_prop():
    return LottieProp("test", int, 0)

def test_lottie_object_init(lottie_object):
    assert lottie_object is not None

def test_lottie_object_to_dict(lottie_object):
    assert lottie_object.to_dict() == {}

def test_lottie_object_clone(lottie_object):
    clone = lottie_object.clone()
    assert clone is not lottie_object

def test_custom_object_init(custom_object):
    assert custom_object is not None

def test_lottie_prop_init(lottie_prop):
    assert lottie_prop is not None

def test_basic_to_dict_with_invalid_v(lottie_prop):
    with pytest.raises(Exception):
        lottie_prop._basic_to_dict({})

def test_basic_to_dict_with_mixed_list_v(lottie_prop):
    result = lottie_prop._basic_to_dict([1, "foo", True])
    assert result == [1, "foo", True]

def test_basic_to_dict_with_list_of_lists_v(lottie_prop):
    result = lottie_prop._basic_to_dict([[1, 2], [3, 4]])
    assert result == [[1, 2], [3, 4]]

def test_clone_value_with_invalid_value(lottie_prop):
    with pytest.raises(Exception):
        lottie_prop.clone_value({})

def test_clone_value_with_mixed_list_value(lottie_prop):
    result = lottie_prop.clone_value([1, "foo", True])
    assert result == [1, "foo", True]

def test_clone_value_with_list_of_lists_value(lottie_prop):
    result = lottie_prop.clone_value([[1, 2], [3, 4]])
    assert result == [[1, 2], [3, 4]]
