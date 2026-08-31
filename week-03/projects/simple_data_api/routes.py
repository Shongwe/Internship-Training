from fastapi import APIRouter, HTTPException
from storage import ItemStorage
from validators import ItemCreate, ItemUpdate

router = APIRouter()
storage = ItemStorage()

@router.get("/items")
def list_items():
    items = [i.to_dict() for i in storage.list_all()]
    return {"items": items, "total": len(items)}

@router.get("/items/{item_id}")
def get_item(item_id: int):
    item = storage.read(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item.to_dict()

@router.post("/items", status_code=201)
def create_item(payload: ItemCreate):
    item = storage.create(payload.name, payload.description, payload.price)
    return item.to_dict()

@router.put("/items/{item_id}")
def update_item(item_id: int, payload: ItemUpdate):
    item = storage.update(item_id, **payload.dict(exclude_unset=True))
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item.to_dict()

@router.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    success = storage.delete(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return None