#Python
from typing import Optional, List;
from uuid import UUID;
from datetime import date, datetime;

#Pydantic
from pydantic import BaseModel, EmailStr, Field;

# FastAPI
from fastapi import FastAPI, status;

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

# Path operations

## Users

### Register a user
@app.post(
  path="/signup",
  response_model=User,
  status_code=status.HTTP_201_CREATED,
  summary="SignUp User",
  description="For register a users",
  tags=["Users"]
)
def signup():
  pass;

### Login a user
@app.post(
  path="/login",
  response_model=User,
  status_code=status.HTTP_200_OK,
  summary="Login User",
  description="For login a users",
  tags=["Users"]
)
def login():
  pass;

### Get All users
@app.get(
  path="/users",
  response_model=List[User],
  status_code=status.HTTP_200_OK,
  summary="Get ALL User",
  description="Get all users",
  tags=["Users"]
)
def get_all_users():
  pass;

### Get One user
@app.get(
  path="/users/{user_id}",
  response_model=User,
  status_code=status.HTTP_200_OK,
  summary="Get ONE User",
  description="Get one user",
  tags=["Users"]
)
def get_one_user():
  pass;

### Update One user
@app.put(
  path="/users/{user_id}",
  response_model=User,
  status_code=status.HTTP_200_OK,
  summary="Update User",
  description="Update one User",
  tags=["Users"]
)
def update_one_user():
  pass;

### Delete One user
@app.delete(
  path="/users/{user_id}",
  response_model=User,
  status_code=status.HTTP_200_OK,
  summary="Delete ONE User",
  description="Delete one user",
  tags=["Users"]
)
def delete_one_user():
  pass;

## Tweets

### Get All tweets
@app.get(
  path="/",
  response_model=List[Tweet],
  status_code=status.HTTP_200_OK,
  summary="Get ALL Tweets",
  description="Get all tweets",
  tags=["Tweets"]
)
def home():
  pass;

### Post a user
@app.post(
  path="/post",
  response_model=Tweet,
  status_code=status.HTTP_201_CREATED,
  summary="Post ONE Tweet",
  description="Post ONE tweet",
  tags=["Tweets"]
)
def post():
  pass;

### Get One tweet
@app.get(
  path="/tweets/{tweet_id}",
  response_model=Tweet,
  status_code=status.HTTP_200_OK,
  summary="Get ONE Tweet",
  description="Get one tweet",
  tags=["Tweets"]
)
def get_one_tweet():
  pass;

### Delete One tweet
@app.delete(
  path="/tweets/{tweet_id}/delete",
  response_model=Tweet,
  status_code=status.HTTP_200_OK,
  summary="Delete ONE Tweet",
  description="Delete one tweet",
  tags=["Tweets"]
)
def delete_one_tweet():
  pass;

### Update One tweet
@app.put(
  path="/tweets/{tweet_id}/update",
  response_model=Tweet,
  status_code=status.HTTP_200_OK,
  summary="Update ONE Tweet",
  description="Update one tweet",
  tags=["Tweets"]
)
def update_one_tweet():
  pass;
