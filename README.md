# Smart Home API (Stub Version)

This project is a stub implementation of a Smart Home API using FastAPI.  
It provides basic APIs for managing users, houses, rooms, and devices.  
The focus is on API design, error handling, input validation, and automated testing.  

## API Endpoints

### User APIs
| Method | Endpoint              | Description             |
|--------|----------------------|-------------------------|
| `POST` | `/user/create`       | Create a new user      |
| `GET`  | `/user/{user_id}`    | Get user details       |

### House APIs
| Method | Endpoint                | Description                |
|--------|------------------------|----------------------------|
| `POST` | `/house/add`           | Add a new house           |
| `GET`  | `/house/{house_id}`    | Get house details         |
| `GET`  | `/house/{house_id}/rooms` | Get all rooms in a house |

### Room APIs
| Method | Endpoint               | Description                  |
|--------|-----------------------|------------------------------|
| `POST` | `/room/add`          | Add a new room             |
| `GET`  | `/room/{room_id}`    | Get room details           |
| `GET`  | `/room/{room_id}/devices` | Get all devices in a room |

### Device APIs
| Method | Endpoint                | Description                  |
|--------|------------------------|------------------------------|
| `POST` | `/device/add`          | Add a new device            |
| `GET`  | `/device/{device_id}`  | Get device status           |
| `PUT`  | `/device/control/{device_id}` | Control a device (on/off) |

This implementation does not include database connections or real device interactions.  
It is designed to simulate API behaviors and validate inputs using in-memory data structures.  
