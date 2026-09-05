from operator import itemgetter
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from simple_data_api.storage import ItemStorage
from simple_data_api.validators import ItemCreate, ItemUpdate
from simple_data_api.models import ItemDict

router = APIRouter()
storage = ItemStorage()


@router.get("/items", response_model=None)
def list_items(
    search: str | None = None,
    price_min: float | None = None,
    price_max: float | None = None,
    page: int = 1,
    limit: int = 10,
    sort: str | None = None,
    order: str = "asc",
) -> dict[str, list[ItemDict] | int]:
    """Return items with optional search, filter, pagination, and sorting."""
    items: list[ItemDict] = [i.to_dict() for i in storage.list_all()]

    # Search
    if search:
        items = [
            i
            for i in items
            if search.lower() in i["name"].lower()
            or search.lower() in i["description"].lower()
        ]

    # Price filter
    if price_min is not None:
        items = [i for i in items if i["price"] >= price_min]
    if price_max is not None:
        items = [i for i in items if i["price"] <= price_max]

    # Sorting
    if sort in {"name", "price"}:
        reverse = order == "desc"
        items.sort(key=itemgetter(sort), reverse=reverse)

    # Pagination
    start = (page - 1) * limit
    end = start + limit
    paginated = items[start:end]

    return {"items": paginated, "total": len(items)}


@router.get("/items/{item_id}", response_model=None)
def get_item(item_id: int):
    item = storage.read(item_id)
    if not item:
        return error_response(
            404, "ITEM_NOT_FOUND", f"Item with ID {item_id} not found"
        )
    return item.to_dict()


@router.post("/items", status_code=201)
def create_item(payload: ItemCreate) -> ItemDict:
    item = storage.create(payload.name, payload.description, payload.price)
    return item.to_dict()


@router.put("/items/{item_id}", response_model=None)
def update_item(item_id: int, payload: ItemUpdate):
    item = storage.update(item_id, **payload.model_dump(exclude_unset=True))
    if not item:
        return error_response(
            404, "ITEM_NOT_FOUND", f"Item with ID {item_id} not found"
        )
    return item.to_dict()


@router.delete("/items/{item_id}", status_code=204, response_model=None)
def delete_item(item_id: int):
    success = storage.delete(item_id)
    if not success:
        return error_response(
            404, "ITEM_NOT_FOUND", f"Item with ID {item_id} not found"
        )
    return None


def error_response(status_code: int, code: str, message: str):
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "error",
            "data": None,
            "error": {"code": code, "message": message},
        },
    )
