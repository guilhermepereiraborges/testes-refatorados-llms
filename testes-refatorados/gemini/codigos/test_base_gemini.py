import pytest
from lottie.objects.base import LottieProp, LottieObject, CustomObject

def test_lottie_object_creation():
    obj = LottieObject()
    assert obj is not None

def test_lottie_object_to_dict():
    obj = LottieObject()
    assert obj.to_dict() == {}

def test_lottie_object_cloning():
    obj = LottieObject()
    clone = obj.clone()
    assert clone is not obj
    assert clone.to_dict() == obj.to_dict()  # Ensure deep copy

def test_custom_object_creation():
    obj = CustomObject()
    assert obj is not None

def test_lottie_prop_creation():
    prop = LottieProp("test", int, 0)
    assert prop is not None

def test_basic_to_dict_invalid_value():
    prop = LottieProp("test", int, 0)
    with pytest.raises(TypeError):
        prop._basic_to_dict({})

def test_basic_to_dict_mixed_list_value():
    prop = LottieProp("test", int, 0)
    result = prop._basic_to_dict([1, "foo", True])
    assert result == [1, "foo", True]

def test_basic_to_dict_list_of_lists_value():
    prop = LottieProp("test", int, 0)
    result = prop._basic_to_dict([[1, 2], [3, 4]])
    assert result == [[1, 2], [3, 4]]

def test_clone_value_invalid_value():
    prop = LottieProp("test", int, 0)
    with pytest.raises(TypeError):
        prop.clone_value({})

def test_clone_value_mixed_list_value():
    prop = LottieProp("test", int, 0)
    result = prop.clone_value([1, "foo", True])
    assert result == [1, "foo", True]

def test_clone_value_list_of_lists_value():
    prop = LottieProp("test", int, 0)
    result = prop.clone_value([[1, 2], [3, 4]])
    assert result == [[1, 2], [3, 4]]