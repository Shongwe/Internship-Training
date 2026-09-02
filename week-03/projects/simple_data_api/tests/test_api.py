from fastapi.testclient import TestClient
from simple_data_api.app import app

client = TestClient(app)


def test_create_item():
    response = client.post(
        "/api/items", json={"name": "Test Item", "description": "A test", "price": 9.99}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Test Item"


def test_get_item_not_found():
    response = client.get("/api/items/999")
    assert response.status_code == 404


def test_delete_item():
    create_response = client.post(
        "/api/items",
        json={"name": "Delete Me", "description": "Temporary", "price": 5.0},
    )
    item_id = create_response.json()["id"]

    delete_response = client.delete(f"/api/items/{item_id}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/api/items/{item_id}")
    assert get_response.status_code == 404


def test_list_items():
    client.post(
        "/api/items", json={"name": "Item1", "description": "Desc1", "price": 10}
    )
    client.post(
        "/api/items", json={"name": "Item2", "description": "Desc2", "price": 20}
    )
    response = client.get("/api/items")
    assert response.status_code == 200
    data = response.json()
    assert any(item["name"] == "Item1" for item in data)
    assert any(item["name"] == "Item2" for item in data)


def test_update_item(client):
    create = client.post(
        "/api/items", json={"name": "Old", "description": "Temp", "price": 5}
    )
    item_id = create.json()["id"]
    update = client.put(f"/api/items/{item_id}", json={"name": "New", "price": 15})
    assert update.status_code == 200
    assert update.json()["name"] == "New"
    assert update.json()["price"] == 15


def test_blank_name_validation(client):
    response = client.post(
        "/api/items", json={"name": "   ", "description": "Bad", "price": 10}
    )
    assert response.status_code == 422


def test_negative_price_validation(client):
    response = client.post(
        "/api/items", json={"name": "BadPrice", "description": "Oops", "price": -1}
    )
    assert response.status_code == 422


def test_missing_price_validation(client):
    response = client.post(
        "/api/items", json={"name": "NoPrice", "description": "Oops"}
    )
    assert response.status_code == 422


def test_delete_not_found(client):
    response = client.delete("/api/items/999")
    assert response.status_code == 404


def test_multiple_items_id_increment(client):
    r1 = client.post(
        "/api/items", json={"name": "First", "description": "One", "price": 1}
    )
    r2 = client.post(
        "/api/items", json={"name": "Second", "description": "Two", "price": 2}
    )
    assert r2.json()["id"] == r1.json()["id"] + 1
