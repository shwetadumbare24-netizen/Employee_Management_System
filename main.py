from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routes.EmpRoutes import router

app = FastAPI(title = "Employee Mnagament system")

app.include_router(router)

@app.get("/")
def welcome():
    return {"message":"Employee management system"}
    