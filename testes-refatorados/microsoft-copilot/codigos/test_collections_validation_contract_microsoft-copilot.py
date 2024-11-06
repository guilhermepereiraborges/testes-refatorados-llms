import pytest
from flunt.validations.collections_validation_contract import CollectionsValidationContract

@pytest.fixture
def contract():
    return CollectionsValidationContract()

@pytest.mark.parametrize("data, min_val, max_val, expected", [
    ([1, 2, 3], 1, 3, True),
    ([1], 2, 3, False),
    ([1, 2, 3, 4], 1, 3, False),
    ('abc', 1, 3, True),
    ('a', 2, 3, False),
    ('abcd', 1, 3, False),
    ({'a': 1, 'b': 2}, 1, 3, True),
    ({'a': 1}, 2, 3, False),
    ({'a': 1, 'b': 2, 'c': 3, 'd': 4}, 1, 3, False),
    ({1, 2, 3}, 1, 3, True),
    ({1}, 2, 3, False),
    ({1, 2, 3, 4}, 1, 3, False)
])
def test_is_between(contract, data, min_val, max_val, expected):
    contract.is_between(data, min_val, max_val, 'key', 'message')
    assert contract.is_valid == expected

    if not expected:
        assert len(contract.get_notifications()) == 1
        assert contract.get_notifications()[0].message == 'message'
