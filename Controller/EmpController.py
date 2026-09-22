from Model.CreateEmpModel import EmpStruct
from Model.UpdateEmpModel import UpdateStruct
from Database.Connection import employee_collection
# from Model.UpdateEmpModel import up

def get_Emp():
    all_data = list(employee_collection.find({}, {"_id": 0 }))
    return all_data

def createEmpModel(employee:EmpStruct):
    s_id = employee.ID
    s_name = employee.NAME
    s_dept = employee.DEPT
    s_salary = employee.SALARY    
    
    sdict = {
        "ID":s_id,
        "NAME":s_name,
        "DEPT":s_dept,
        "SALARY":s_salary

    }
    employee_collection.insert_one(sdict)
    return {"message":"Employee Created!!"}

def updateEmpModel(ID : int, emp_update : UpdateStruct):
    all_data = list(employee_collection.find({}, {"_id": 0}))
    
    UpdateEmp = {}
    
    for i in all_data:
        
        if i["ID"] == ID:
            
            if emp_update.NAME != None:
                UpdateEmp["NAME" ] = emp_update.NAME
            if emp_update.DEPT != None:
                UpdateEmp["DEPT"] = emp_update.DEPT
            if emp_update.SALARY != None:
                UpdateEmp["SALARY"] = emp_update.SALARY
                
            employee_collection.update_one(
                {"ID": ID},
                {"$set":UpdateEmp}
                
            )
            return {"message":"Student Updated"}
        
def deleteEmpModel(ID : int):
    all_data = list(employee_collection.find({}, {"id" :0}))
    
    for i in all_data:
        if i["ID"] == ID:
            
            employee_collection.delete_one({"ID":ID})  
            return {"message": "Student Deleted"}              


    