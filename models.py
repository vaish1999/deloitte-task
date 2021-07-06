from database import Base
from sqlalchemy import Column,Integer,String
class Employee(Base):
    __tablename__="employee"
    id=Column(Integer,primary_key=True,index=True)
    employeeName=Column(String)
    employeeAge=Column(Integer)
    employeeAddress=Column(String)

    
