from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


uri = f"mongodb+srv://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@cluster0.brp8cuh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

db = client.user

collection_user = db["users"]

"""try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)"""
