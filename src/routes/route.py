from fastapi import APIRouter
from src.models.users import User
from src.config.database import collection_user
from src.schemas.userSchema import list
from src.schemas.userSchema import individual
from bson import ObjectId

router = APIRouter()


# GET Request Method
@router.get("/")
async def get_users():
    users = list(collection_user.find())
    return users

@router.get("/{id}")
async def get_user(id):
    user = individual(collection_user.find_one({"_id": ObjectId(id)}))
    return user

# POST Request Method
@router.post("/")
async def post_user(user: User):
    collection_user.insert_one(dict(user))

# PUT Request Method
@router.put("/{id}")
async def put_user(id: str, user: User):
    collection_user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})

# DELETE Request Method
@router.delete("/{id}")
async def delete_user(id: str):
    collection_user.find_one_and_delete({"_id": ObjectId(id)})
