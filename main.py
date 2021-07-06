from typing import Optional

from fastapi import FastAPI
from .import schemas

app = FastAPI()




@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/employee")
def create_employee(new_emp:schems.Employee):
    


@app.get("/employee/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
