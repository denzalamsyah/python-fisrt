from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title:str
    body:str
        
class Blog(BlogBase):
    class Config():
        orm_mode: True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name: str
    email : str
    blogs: List[Blog] = [] # menampilkan user beserta list blog
    class Config():
        orm_mode: True
 
# membuat response model
# ini akan menampilkan title dan body pada response json
# class ShowBlog(Blog):
#     class Config():
#         orm_mode: True
'''atau bisa dicustom seperti di bawah ini'''

# ini akan menampilkan title saja pada response json
class ShowBlog(BaseModel):
    title:str
    body: str
    creator:ShowUser #menampilkan blog dan user
    class Config():
        orm_mode: True
    
class Login(BaseModel):
    email : str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None