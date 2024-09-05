from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
import os

uri = f"mongodb+srv://artursousac:ZWw9iafqnMBeHOG4@cluster0.brp8cuh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

db = client.user

collection_user = db["users"]

"""try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)"""
