import pytest
from flunt.validations.collections_validation_contract import CollectionsValidationContract

@pytest.fixture
def contract():
    return CollectionsValidationContract()

class TestIsBetween:

    @pytest.mark.parametrize("collection, min_size, max_size", [
        ([1, 2, 3], 1, 3),
        ('abc', 1, 3),
        ({'a': 1, 'b': 2}, 1, 3),
        ({1, 2, 3}, 1, 3),
    ])
    def test_within_range(self, contract, collection, min_size, max_size):
        """Testa coleções dentro do intervalo especificado."""
        contract.is_between(collection, min_size, max_size, 'key', 'message')
        assert contract.is_valid

    @pytest.mark.parametrize("collection, min_size, max_size", [
        ([1], 2, 3),
        ('a', 2, 3),
        ({'a': 1}, 2, 3),
        ({1}, 2, 3),
    ])
    def test_below_range(self, contract, collection, min_size, max_size):
        """Testa coleções abaixo do intervalo especificado."""
        contract.is_between(collection, min_size, max_size, 'key', 'message')
        assert not contract.is_valid
        notifications = contract.get_notifications()
        assert len(notifications) == 1
        assert notifications[0].message == 'message'

    @pytest.mark.parametrize("collection, min_size, max_size", [
        ([1, 2, 3, 4], 1, 3),
        ('abcd', 1, 3),
        ({'a': 1, 'b': 2, 'c': 3, 'd': 4}, 1, 3),
        ({1, 2, 3, 4}, 1, 3),
    ])
    def test_above_range(self, contract, collection, min_size, max_size):
        """Testa coleções acima do intervalo especificado."""
        contract.is_between(collection, min_size, max_size, 'key', 'message')
        assert not contract.is_valid
        notifications = contract.get_notifications()
        assert len(notifications) == 1
        assert notifications[0].message == 'message'
