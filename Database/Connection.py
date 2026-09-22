from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("mongodb")


ConnectionStr = MongoClient("mongodb+srv://shwetadumbare24_db_user:zvpr1vNlqyyTKE2Q@cluster0.pynqygh.mongodb.net/?appName=Cluster0")

database = ConnectionStr["Emp_DB"]

employee_collection = database["Emp_Collection"]