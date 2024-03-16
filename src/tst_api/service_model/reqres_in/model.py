from typing import List

from pydantic import BaseModel, EmailStr, HttpUrl


class User(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl


class AllUsers(BaseModel):
    data: List[User]


class CreateUser(BaseModel):
    name: str
    job: str
    id: int
    createdAt: str
