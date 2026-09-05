import json
import os
from typing import Optional
from simple_data_api.models import Item


class ItemStorage:
    def __init__(self, filename: Optional[str] = None):
        base_dir = os.path.dirname(__file__)
        self.filename = filename or os.path.join(base_dir, "data.json")
        self.items = self.load()
        self.next_id = max([i.id for i in self.items], default=0) + 1


    def load(self) -> list[Item]:
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [Item.from_dict(item) for item in data.get("items", [])]
        except FileNotFoundError:
            return []

    def save(self):
        with open(self.filename, "w") as f:
            json.dump({"items": [i.to_dict() for i in self.items]}, f, indent=2)

    def create(self, name: str, description: str, price: float) -> Item:
        item = Item(self.next_id, name, description, price)
        self.items.append(item)
        self.next_id += 1
        self.save()
        return item

    def read(self, item_id: int) -> Item | None:
        return next((i for i in self.items if i.id == item_id), None)

    def list_all(self) -> list[Item]:
        return self.items

    def update(
        self,
        item_id: int,
        name: Optional[str] = None,
        description: Optional[str] = None,
        price: Optional[float] = None,
    ) -> Item | None:
        item = self.read(item_id)
        if not item:
            return None
        updates: dict[str, str | float] = {}
        if name is not None:
            updates["name"] = name
        if description is not None:
            updates["description"] = description
        if price is not None:
            updates["price"] = price
        for key, value in updates.items():
            setattr(item, key, value)
        self.save()
        return item

    def delete(self, item_id: int) -> bool:
        item = self.read(item_id)
        if not item:
            return False
        self.items = [i for i in self.items if i.id != item_id]
        self.save()
        return True
