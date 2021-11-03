#Python
from typing import Optional, List;
from uuid import UUID;
from datetime import date, datetime;
import json;

#Pydantic
from pydantic import BaseModel, EmailStr, Field;

# FastAPI
from fastapi import FastAPI, status, Body, Path;

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

class UserRegister(User):
  password: str = Field(
    ...,
    min_length=8,
    max_length=70
  );

class Tweet(BaseModel):
  tweet_id: UUID = Field(...);
  message: str = Field(
    ...,
    min_length=1,
    max_length=256
  );
  created_at: datetime = Field(default=datetime.utcnow());
  updated_at: Optional[datetime] = Field(default=None);
  by: User = Field(...);

# Path operations

## Users

### Register a user
@app.post(
  path="/signup",
  response_model=User,
  status_code=status.HTTP_201_CREATED,
  summary="SignUp User",
  tags=["Users"]
)
def signup(user: UserRegister = Body(...)):
  """
    # SignUp
    This path operation REGISTER a user in the app.

    ## Parameters:
      - Request body parameter
        - **user**: UserRegister

    Returns a json with the basic user information
      - user_id: UUID
      - email: EmailStr
      - full_name: str
      - birth_date: str
  """
  
  with open("users.json", "r+", encoding="utf-8") as file: # leer y escribir r+
    users = json.loads(file.read());

    user_dict = user.dict(); # lo pone fastapi para transformar json a dict PERO ATRIBUTOS MANUALMENTE
    user_dict["user_id"] = str(user_dict["user_id"]);
    user_dict["birth_date"] = str(user_dict["birth_date"]);

    users.append(user_dict);
    file.seek(0); # moverme al primer byte del archivo (ESCRIBIR DESDE CERO en el file)
    file.write(json.dumps(users)); # Convierto a json el dict
    return user;

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
  tags=["Users"]
)
def get_all_users():
  """
    # GetAll users
    Get All users

    ## Parameters:
      -

    Returns a json list with all users int he, with the following KEYS:
      - user_id: UUID
      - email: EmailStr
      - full_name: str
      - birth_date: str
  """
  
  with open("users.json", "r+", encoding="utf-8") as file: # leer y escribir r+
    users = json.loads(file.read());
    return users;

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
  tags=["Tweets"]
)
def home():
  """
    # GetAll tweets
    Get All tweets

    ## Parameters:
      -

    Returns a json list with all tweets int the, with the following KEYS:
      - tweet_id: UUID
      - message: str
      - created_at: datetime
      - updated_at: Optional[datetime]
      - by: User
  """
  
  with open("tweets.json", "r+", encoding="utf-8") as file: # leer y escribir r+
    tweets = json.loads(file.read());
    return tweets;

### Post a user
@app.post(
  path="/post",
  response_model=Tweet,
  status_code=status.HTTP_201_CREATED,
  summary="Post ONE Tweet",
  tags=["Tweets"]
)
def post(tweet: Tweet = Body(...)):
  """
    # Post a tweet
    This path operation REGISTER a user in the app.

    ## Parameters:
      - Request body parameter
        - **tweet**: Tweet

    Returns a json with the basic user information
      - tweet_id: UUID
      - message: str
      - created_at: datetime
      - updated_at: Optional[datetime]
      - by: User
  """
  
  with open("tweets.json", "r+", encoding="utf-8") as file: # leer y escribir r+
    tweets = json.loads(file.read());

    tweet_dict = tweet.dict(); # lo pone fastapi para transformar json a dict PERO ATRIBUTOS MANUALMENTE
    tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"]);
    tweet_dict["created_at"] = str(tweet_dict["created_at"]);
    tweet_dict["updated_at"] = str(tweet_dict["updated_at"]);
    tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"]);
    tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"]);

    tweets.append(tweet_dict);
    file.seek(0); # moverme al primer byte del archivo (ESCRIBIR DESDE CERO en el file)
    file.write(json.dumps(tweets)); # Convierto a json el dict
    return tweet;

### Get One tweet
@app.get(
  path="/tweets/{tweet_id}",
  response_model=Tweet,
  status_code=status.HTTP_200_OK,
  summary="Get ONE Tweet",
  description="Get one tweet",
  tags=["Tweets"]
)
def get_one_tweet(
  tweet_id: str = Path(
    ...,
    example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
  )
):
  """
    # GetAll tweets
    Get All tweets

    ## Parameters:
      - **tweet_id**: UUID

    Returns a json list with all tweets int the, with the following KEYS:
      - tweet_id: UUID
      - message: str
      - created_at: datetime
      - updated_at: Optional[datetime]
      - by: User
  """
  
  with open("tweets.json", "r", encoding="utf-8") as file: # leer y escribir r+
    tweets = json.loads(file.read());
    tweet = {"myTweet": tweetItem for tweetItem in tweets if tweetItem["tweet_id"] == tweet_id};
    return tweet["myTweet"];

### Delete One tweet
@app.delete(
  path="/tweets/{tweet_id}/delete",
  response_model=List[Tweet],
  status_code=status.HTTP_200_OK,
  summary="Delete ONE Tweet",
  tags=["Tweets"]
)
def delete_one_tweet(
  tweet_id: str = Path(
    ...,
    example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
  )
):
  """
    # Delete One tweet
    Delete One tweet by id

    ## Parameters:
      - **tweet_id**: UUID

    Returns a json with the list of Tweets existents.
  """
  
  with open("tweets.json", "r+", encoding="utf-8") as file: # leer y escribir r+
    tweets = json.loads(file.read());
    tweets_enum = enumerate(tweets);

    for tweetItemFor in tweets:
      tweet_dict = dict(tweetItemFor); # lo pone fastapi para transformar json a dict PERO ATRIBUTOS MANUALMENTE
      tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"]);
      tweet_dict["created_at"] = str(tweet_dict["created_at"]);
      tweet_dict["updated_at"] = str(tweet_dict["updated_at"]);
      tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"]);
      tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"]);

    tweet = {"myTweet": tweetIndex for (tweetIndex, tweetItem) in tweets_enum if tweetItem["tweet_id"] == tweet_id};

    tweets.pop(tweet["myTweet"]);
    print(tweets);
    file.seek(0); # moverme al primer byte del archivo (ESCRIBIR DESDE CERO en el file)
    file.write(json.dumps(tweets)); # Convierto a json el dict
    return tweets;

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
