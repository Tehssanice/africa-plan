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


@router.get("/places/", tags=["places"])
async def read_places():
    return [{"username": "Japan"}, {"username": "Dubai"}]


@router.get("/new_people/", tags=["new_people"])
async def read_new_people():
    return [{"username": "Nick"}, {"username": "James"}]


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


@router.post("/cart/")
async def create_cart(product: Cart, q: Annotated[str | None, Query(min_length=10, max_length=50)] = None):
    print(f"The product name is {product.name}")
    return product


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
