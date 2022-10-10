from fastapi import APIRouter
from models.user import User
from database.user import create_user, get_user, get_users, delete_user, update_user


routes_user = APIRouter()

# CREATE USER

@routes_user.post("/create", response_model=User)
def create(user: User):
    return create_user(user.dict())


    
# GET USER BY ID

@routes_user.get("/get/{id}")
def get_by_id(id: int):
    return get_user(id)



# GET ALL USERS

@routes_user.get("/all")
def get_all():
    return get_users()



# DELETE USER

@routes_user.delete("/delete")
def delete(user: User):
    return delete_user(user.dict())



# UPDATE USER

@routes_user.put("/update")
def update(user: User):
    return update_user(user.dict())
