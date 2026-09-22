from pydantic import BaseModel,Field
from typing import  Annotated, Optional


class UpdateStruct(BaseModel):
    NAME : Annotated[Optional [str], Field(title = "Enter Your Name ", default=None)]
    DEPT : Annotated[Optional[str] , Field(title="Enter your Dept ", default=None)] 
    SALARY : Annotated[Optional[str] , Field(title="Enter your salary", default=None)]   
    
