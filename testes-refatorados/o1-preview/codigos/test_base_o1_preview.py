import pytest
from lottie.objects.base import LottieProp, LottieObject, CustomObject

class TestLottieObject:
    def test_init(self):
        obj = LottieObject()
        assert obj is not None

    def test_to_dict(self):
        obj = LottieObject()
        assert obj.to_dict() == {}

    def test_clone(self):
        obj = LottieObject()
        clone = obj.clone()
        assert clone is not obj

class TestCustomObject:
    def test_init(self):
        obj = CustomObject()
        assert obj is not None

class TestLottieProp:
    @pytest.fixture
    def prop(self):
        return LottieProp("test", int, 0)

    def test_init(self, prop):
        assert prop is not None

    def test_basic_to_dict_with_invalid_v(self, prop):
        with pytest.raises(Exception):
            prop._basic_to_dict({})

    @pytest.mark.parametrize("input_value, expected", [
        ([1, "foo", True], [1, "foo", True]),
        ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
    ])
    def test_basic_to_dict_valid_v(self, prop, input_value, expected):
        result = prop._basic_to_dict(input_value)
        assert result == expected

    def test_clone_value_with_invalid_value(self, prop):
        with pytest.raises(Exception):
            prop.clone_value({})

    @pytest.mark.parametrize("input_value, expected", [
        ([1, "foo", True], [1, "foo", True]),
        ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
    ])
    def test_clone_value_with_valid_value(self, prop, input_value, expected):
        result = prop.clone_value(input_value)
        assert result == expected
