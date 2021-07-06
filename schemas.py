
from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    employeeName: str
    employeeAge: int
    employeeAddress: str