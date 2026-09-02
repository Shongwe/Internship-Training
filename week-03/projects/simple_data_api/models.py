from datetime import datetime, UTC
from typing import TypedDict


class ItemDict(TypedDict):
    id: int
    name: str
    description: str
    price: float
    created_at: str


class Item:
    def __init__(self, id: int, name: str, description: str, price: float):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.created_at = datetime.now(UTC).isoformat()

    def to_dict(self) -> ItemDict:
        """Convert the Item instance into a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: ItemDict) -> "Item":
        """Create an Item instance from a dictionary."""
        return cls(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            price=data["price"],
        )
