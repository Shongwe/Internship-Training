from simple_data_api.models import Item, ItemDict


def test_item_to_dict() -> None:
    item = Item(1, "Book", "Novel", 10.0)
    data = item.to_dict()
    assert data["id"] == 1
    assert data["name"] == "Book"
    assert "created_at" in data


def test_item_from_dict() -> None:
    data: ItemDict = {
        "id": 2,
        "name": "Pen",
        "description": "Blue ink",
        "price": 1.5,
        "created_at": "2026-09-01T12:00:00Z",
    }
    item = Item.from_dict(data)
    assert item.id == 2
    assert item.name == "Pen"
