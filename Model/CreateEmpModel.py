from pydantic import BaseModel,Field
from typing import Annotated

class EmpStruct(BaseModel):
    ID : Annotated[int,Field(title = "Enter your id:")]
    NAME : Annotated[str, Field(title= "Enter your name:")]
    DEPT : Annotated[str, Field(title="Enter your Dept:")]
    SALARY : Annotated[int , Field(title="Enter yout Salary:")]
    
    