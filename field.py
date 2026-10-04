from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    id : int = Field(gt = 0, description = "Put a positive int") # gt -> grater than 0
    name : str = Field(max_length = 22, description = "Name of the user")
    age : int = Field(gt = 18, lt = 100, description = "Age must be between 18 to 100 years")
    course : str = Field(description = "enter your courses name")
    mail : EmailStr = Field(description = "enter you email here")

user_1 = User(
    id = 1,
    name = "Akul",
    age = 22,
    course = "B.Tech",
    mail = "akul@gmail.com"
)

print(user_1)


user_2 = User(
    id = 2,
    name = "Akul",
    age = 16,
    course = "B.Tech",
    mail = "akul@akul"
)

print(user_2)

# Through the erro
# age
#   Input should be greater than 18 [type=greater_than, input_value=16, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.13/v/greater_than
# mail
#   value is not a valid email address: The part after the @-sign is not valid. 
# It should have a period. [type=value_error, input_value='akul@akul', input_type=str]