#Python
from typing import Optional;
from uuid import UUID;
from datetime import date, datetime;

#Pydantic
from pydantic import BaseModel, EmailStr, Field;

# FastAPI
from fastapi import FastAPI;

app = FastAPI();

# Models

class BaseUser(BaseModel):
  user_id: UUID = Field(...);
  email: EmailStr = Field(...);

class UserLogin(BaseUser):
  password: str = Field(
    ...,
    min_length=8,
    max_length=70
  );

class User(BaseUser):
  full_name: str = Field(
    ...,
    min_length=1,
    max_length=50
  );
  birth_date: Optional[date] = Field(default=None);


class Tweet(BaseModel):
  tweet_id: UUID = Field(...);
  message: str = Field(
    ...,
    min_length=1,
    max_length=256
  );
  created_at: datetime = Field(default=datetime.utcnow());
  update_at: Optional[datetime] = Field(default=None);
  by: User = Field(...);

@app.get("/")
def home():
  return {
    "hola": "Mundo"
  };
