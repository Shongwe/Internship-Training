import pytest
from simple_data_api.validators import ItemCreate, ItemUpdate
from pydantic import ValidationError


def test_item_create_blank_name():
    with pytest.raises(ValidationError):
        ItemCreate(name="   ", description="Bad", price=10)


def test_item_create_negative_price():
    with pytest.raises(ValidationError):
        ItemCreate(name="Book", description="Novel", price=-5)


def test_item_update_optional_fields():
    item = ItemUpdate(name="Updated", price=20, description=None)
    assert item.name == "Updated"
    assert item.price == 20
