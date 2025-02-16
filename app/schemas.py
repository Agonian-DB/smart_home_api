# schemas.py

from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    houses: List[int] = Field(default_factory=list)  # 用户所拥有的 house_id 列表

class House(BaseModel):
    house_id: int
    name: str
    owner_id: int  # 房主的 user_id
    rooms: List[int] = Field(default_factory=list)   # 该房屋内的 room_id 列表

class Room(BaseModel):
    room_id: int
    name: str
    house_id: int
    devices: List[int] = Field(default_factory=list) # 该房间内的 device_id 列表

class Device(BaseModel):
    device_id: int
    name: str
    type: str  # 设备类型（如 light, thermostat 等）
    room_id: int
    status: str  # 设备状态（如 on, off）
