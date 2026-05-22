from fastapi import FastAPI
from typing import TypedDict

app = FastAPI()

class bubbletea(TypedDict):
    name: str
    temperature: int
    price: float
    active: bool

bubble_teas = list[bubbletea]([
    {"name": "Classic Milk Tea", "temperature": 75, "price": 3.5, "active": True},
    {"name": "Taro Milk Tea", "temperature": 80, "price": 4.0, "active": True},
    {"name": "Matcha Milk Tea", "temperature": 70, "price": 4.5, "active": False},
    {"name": "Strawberry Milk Tea", "temperature": 65, "price": 3.0, "active": True},
    {"name": "Brown Sugar Milk Tea", "temperature": 85, "price": 4.0, "active": True}
])

@app.get("/")
def get_root():
    return {"message": "Hello, World!"}



def filter_out_bubbleteas(bubble_teas: list[bubbletea]) -> list[bubbletea]:
    return [bubbletea for bubbletea in bubble_teas if bubbletea["active"]]
    

@app.get("/bubbleteas")
def get_active_bubbleteas():
    return filter_out_bubbleteas(bubble_teas)