from pydantic import BaseModel, Field
from uuid import uuid4

def generate_id():
    return str(uuid4())
 
class User(BaseModel):
    id: int = Field(default_factory=generate_id)
    userid: int
    username: str
    age: int