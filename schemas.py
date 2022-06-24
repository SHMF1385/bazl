from pydantic import BaseModel

class Token(BaseModel):
    access_token: str

class TokenData(BaseModel):
    email: str | None = None

class User(BaseModel):
    email: str

class Login(User):
    password: str

class ShowUser(User):
    nickname: str

class Signup(User):
    nickname: str
    password: str

class ArticleBase(BaseModel):
    title: str
    bazl_number: int
    description: str
    content: str

class Article(ArticleBase):
    id: int
