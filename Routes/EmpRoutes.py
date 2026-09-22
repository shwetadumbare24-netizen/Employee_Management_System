from fastapi import APIRouter
from Controller.EmpController import(
    get_Emp,
    createEmpModel,
    updateEmpModel,
    deleteEmpModel
    
    
)

from Database.Connection import employee_collection
from Model.CreateEmpModel import EmpStruct
from Model.UpdateEmpModel import UpdateStruct
router = APIRouter()


@router.get("/all_data")
def get_all_emp():
    return get_Emp()

@router.post("/add_employee")
def create_emp(employee:EmpStruct):
    return createEmpModel(employee)

@router.put("/edit/{ID}")
def update_emp(ID : int, emp_update : UpdateStruct):
    return updateEmpModel(ID,emp_update)

@router.delete("/delete_emp/{ID}")
def delete_emp(ID : int):
    return deleteEmpModel(ID)
    



    

