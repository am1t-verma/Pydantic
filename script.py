from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str
    email : str
    address : str
    house_no : int
    is_active : bool

user_1 = User(id = 1, name = "ishu", email = "ishu3@mail.com", address = "Near Gurughar, Kharar", house_no = 1174, is_active = True)
user_2 = User(id = "2", name = "ishika", email = "ishika64@mail.com", address = "Ajeet Nagar Gurughar, Kharar", house_no = 374, is_active = False)

print(f"User 1.\n   {user_1}\n")
print(f"User 2.\n   {user_2}\n") # auto convert string to int
user_3 = {
    "id" : 3,
    "name" : "akansha",
    "email" : "akan23@gmail.com",
    "house_no" : 32,
    "is_active" : False,
    "address" : "Near CU Om Patle"
}

user_3 = User(**user_3)
print(f"User 3.\n   {user_3}\n")

user_4 = {
    "id" : 4,
    "name" : "nail",
    "email" : "adamnail@cuchd.in",
    "house_no" : 33,
    "is_active" : True,
    "address" : "Near CU Om Patle"
}

user_4 = User.model_validate(user_4)
print(f"User 4.\n   {user_4}\n")