from typing import Optional

from fastapi import FastAPI,Depends
import schemas,models
from database import engine,SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()


models.Base.metadata.create_all(bind=engine)

def get_db(): 
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/employee")
def create_employee(request:schemas.Employee,db: Session =Depends(get_db)):
    new_emp=models.Employee(employeeName=request.employeeName,employeeAge=request.employeeAge,employeeAddress=request.employeeAddress)
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

@app.get("/employee/all")
def all_employee(db: Session =Depends(get_db)):
    emps=db.query(models.Employee).all()
    return emps

@app.get("/employee/{id}")
def show_employee(id,db: Session =Depends(get_db)):
    emp=db.query(models.Employee).filter(models.Employee.id==id).first()
    return emp
    

