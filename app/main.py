# main.py

from fastapi import FastAPI, HTTPException
from .schemas import User, House, Room, Device
from . import models

app = FastAPI(title="Smart Home API", version="1.0.0")

## ========== Procedure-based APIs ========== ##
@app.post("/user/create")
def create_user(user: User):
    # 假设 user_id 不可重复
    if user.user_id in models.fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists.")
    models.fake_users_db[user.user_id] = user
    return {"message": "User created successfully", "user": user}

@app.post("/house/add")
def add_house(house: House):
    if house.house_id in models.fake_houses_db:
        raise HTTPException(status_code=400, detail="House already exists.")
    if house.owner_id not in models.fake_users_db:
        raise HTTPException(status_code=404, detail="Owner user not found.")
    models.fake_houses_db[house.house_id] = house
    user_obj = models.fake_users_db[house.owner_id]
    user_obj.houses.append(house.house_id)
    return {"message": "House added successfully", "house": house}

@app.post("/room/add")
def add_room(room: Room):
    if room.room_id in models.fake_rooms_db:
        raise HTTPException(status_code=400, detail="Room already exists.")
    if room.house_id not in models.fake_houses_db:
        raise HTTPException(status_code=404, detail="House not found.")
    models.fake_rooms_db[room.room_id] = room
    house_obj = models.fake_houses_db[room.house_id]
    house_obj.rooms.append(room.room_id)
    return {"message": "Room added successfully", "room": room}

@app.post("/device/add")
def add_device(device: Device):
    if device.device_id in models.fake_devices_db:
        raise HTTPException(status_code=400, detail="Device already exists.")
    if device.room_id not in models.fake_rooms_db:
        raise HTTPException(status_code=404, detail="Room not found.")
    if device.status not in ["on", "off"]:
        raise HTTPException(status_code=400, detail="Invalid device status.")
    models.fake_devices_db[device.device_id] = device
    room_obj = models.fake_rooms_db[device.room_id]
    room_obj.devices.append(device.device_id)
    return {"message": "Device added successfully", "device": device}

@app.put("/device/control/{device_id}")
def control_device(device_id: int, status: str):
    if device_id not in models.fake_devices_db:
        raise HTTPException(status_code=404, detail="Device not found.")
    if status not in ["on", "off"]:
        raise HTTPException(status_code=400, detail="Invalid status value.")
    device_obj = models.fake_devices_db[device_id]
    device_obj.status = status
    return {"message": f"Device {device_id} turned {status}", "device": device_obj}


## ========== Entity-based APIs ========== ##
@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id not in models.fake_users_db:
        raise HTTPException(status_code=404, detail="User not found.")
    return models.fake_users_db[user_id]

@app.get("/house/{house_id}")
def get_house(house_id: int):
    if house_id not in models.fake_houses_db:
        raise HTTPException(status_code=404, detail="House not found.")
    return models.fake_houses_db[house_id]

@app.get("/house/{house_id}/rooms")
def get_rooms_in_house(house_id: int):
    if house_id not in models.fake_houses_db:
        raise HTTPException(status_code=404, detail="House not found.")
    house_obj = models.fake_houses_db[house_id]
    room_ids = house_obj.rooms
    rooms = [models.fake_rooms_db[r_id] for r_id in room_ids]
    return {"house_id": house_id, "rooms": rooms}

@app.get("/room/{room_id}")
def get_room(room_id: int):
    if room_id not in models.fake_rooms_db:
        raise HTTPException(status_code=404, detail="Room not found.")
    return models.fake_rooms_db[room_id]

@app.get("/room/{room_id}/devices")
def get_devices_in_room(room_id: int):
    if room_id not in models.fake_rooms_db:
        raise HTTPException(status_code=404, detail="Room not found.")
    room_obj = models.fake_rooms_db[room_id]
    device_ids = room_obj.devices
    devices = [models.fake_devices_db[d_id] for d_id in device_ids]
    return {"room_id": room_id, "devices": devices}

@app.get("/device/{device_id}")
def get_device_status(device_id: int):
    if device_id not in models.fake_devices_db:
        raise HTTPException(status_code=404, detail="Device not found.")
    return models.fake_devices_db[device_id]
