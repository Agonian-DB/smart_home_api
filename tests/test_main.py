# tests/test_main.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/user/create", json={
        "user_id": 1,
        "name": "Alice",
        "email": "alice@example.com",
        "houses": []
    })
    assert response.status_code == 200
    assert response.json()["message"] == "User created successfully"

def test_create_existing_user():
    response = client.post("/user/create", json={
        "user_id": 1,
        "name": "Alice",
        "email": "alice@example.com",
        "houses": []
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "User already exists."

def test_control_device_invalid_device():
    response = client.put("/device/control/9999?status=on")
    assert response.status_code == 404
    assert response.json()["detail"] == "Device not found."

def test_control_device_invalid_status():
    client.post("/user/create", json={
        "user_id": 2,
        "name": "Bob",
        "email": "bob@example.com",
        "houses": []
    })
    client.post("/house/add", json={
        "house_id": 10,
        "name": "Bob's House",
        "owner_id": 2,
        "rooms": []
    })
    client.post("/room/add", json={
        "room_id": 100,
        "name": "Living Room",
        "house_id": 10,
        "devices": []
    })
    client.post("/device/add", json={
        "device_id": 1000,
        "name": "Light 1",
        "type": "light",
        "room_id": 100,
        "status": "off"
    })
    response = client.put("/device/control/1000?status=something_invalid")
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid status value."
