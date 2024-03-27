```python
from fastapi import APIRouter, HTTPException, Query, Path
from pydantic import BaseModel, EmailStr
from typing import Optional, Annotated
from datetime import datetime

router = APIRouter()

class Cart(BaseModel):
name: str
category: str
price: Optional[int] = None
email: EmailStr

users = {
    1: {
        "name": "Jerry",
        "age": 34,
        "id": 1
    },
    2: {
        "name": "Lampard",
        "age": 45,
        "id": 2
    },
    3: {
        "name": "Mary",
        "age": 14,
        "id": 3
    }
}
```

# Code Writing: Path Parameters

● Write a FastAPI route that accepts a path parameter for user identification (user_id) and returns the user's profile information.
● Implement error handling for the case when the user_id path parameter is missing.

## AND

# Data Validation:

● Modify an existing FastAPI route that accepts a path parameter for user_id to ensure that user_id is an integer and greater than zero.
● Add validation to a query parameter start_date to ensure it is a valid date format.

```python
@router.get("/users/{user_id}")
async def check_users(user_id: int, start_date: datetime = Query(None, title="Start date")):
    try:
        if user_id > 0:
            if user_id in users:
                return users[user_id]
            else:
                raise HTTPException(status_code=404, detail="User not found")
    except HTTPException as e:
        return f"404 Error: {e.detail}"
```

# Code Writing: Query Parameters

● Create a FastAPI route that accepts query parameters for filtering a list of products by category and price range.
● Implement default values for the query parameters (category defaulting to 'all' and price_range defaulting to a specific range).

```python
@router.get("/products/")
async def filter_list(category: str = "all", price_range: str = "0-100", q: str | None = None):
    products = {
        "product1": {"category": "jewelry", "price_range": 100},
        "product2": {"category": "book", "price_range": 50},
        "product3": {"category": "electronics", "price_range": 150}
    }

    filtered_products = []

    if price_range:
        range_ = price_range.split("-")
        proposed_range = range(int(range_[0]), int(range_[-1]) + 1)

    for key, value in products.items():
        if category == "all" or products[key]["category"] == category:
            if products[key]["price_range"] in proposed_range:
                filtered_products.append(products[key])

    return filtered_products
```

## Combining Path and Query Parameters:

● Write a FastAPI route that accepts a path parameter for city (city_id) and query parameters for filtering restaurants by cuisine type (cuisine) and rating (min_rating).
● Ensure that the city ID is a path parameter while cuisine type and minimum rating are query parameters.

```python
@router.get("/city/{city_id}")
async def get_restaurant(cuisine_type: str = "all", min_rating: float = 3.0):

    restaurant = {
        1: {
            "cuisine_type": "chinese",
            "rating": 4.3,

        },
        2: {
            "cuisine_type": "italian",
            "rating": 3.8
        },
        3: {
            "cuisine_type": "spanish",
            "rating": 4.7
        },
        4: {
            "cuisine_type": "nigerian",
            "rating": 5
        },
        5: {
            "cuisine_type": "mixican",
            "rating": 2.8
        },
        6: {
            "cuisine_type": "american",
            "rating": 2
        }

    }

    filtered_res = []

    for key, value in restaurant.items():
        if cuisine_type == "all" or restaurant[key]["cuisine_type"] == cuisine_type:
            if not restaurant[key]["rating"] < min_rating:
                filtered_res.append(restaurant[key])

    return filtered_res



```

# Usage and Benefits:

● Analyze a given FastAPI application and identify instances where using path parameters would be more appropriate than query parameters, and vice versa.
● Discuss the benefits of using path and query parameters in the provided FastAPI application and how it enhances API design.

```python
rooms = {
    1: {"name": "Room A", "category": "electronics", "price": 130},
    2: {"name": "Room B", "category": "clothing", "price": 70},
    3: {"name": "Room C", "category": "electronics", "price": 300},
}

@router.get("/rooms/{room_id}")
async def get_room(room_id: int = Path(..., title="Product ID")):
    return rooms.get(room_id)


@router.get("/rooms/")
async def filter_rooms(category: str = Query(None, title="Category")):
    filtered_rooms = [room for room in rooms.values(
    )
        if room["category"] == category]if category else list(rooms.values())
    return filtered_rooms
```
