from fastapi import FastAPI
from passlib.context import CryptContext
import random

myctx = CryptContext(schemes=["sha256_crypt", "md5_crypt", "des_crypt"])

app = FastAPI()

list1 = [ ]
token_list1 = [ ]

@app.post("/register")
def root(username: str ,password: str, token: str):
    if token in token_list1:
        token_list1.remove(token)
        password = myctx.hash(password)
        list1.append( {username:password})
        return(username,password) 
    else:
        return("You need to have a token to be able to register!")


@app.post("/login")
def root(username: str, password: str):
    for user_info in list1:
        if username in user_info:
            stored_password = user_info[username]
            if myctx.verify(password, stored_password):
                return {"message": "Login successful"}
            else:
                return {"Wrong password"}        
        else:
            return {"Wrong username"}

@app.put("/changepassword")
def change_password(username: str, old_password: str, new_password: str):
    for user_info in list1:
        if username in user_info:
            stored_password = user_info[username]
            if myctx.verify(old_password, stored_password):
                user_info[username] = myctx.hash(new_password)
                return {"message": "Password changed successfully"}
            else:
                return {"cant change the password"}

@app.delete("/delete")
def delete_account(username: str, password: str,):
    for user_info in list1:
        if username in user_info:
            stored_password = user_info[username]
            if myctx.verify(password, stored_password):
                list1.remove(user_info)
                return("Account deleted")
            else:
                return("Wrong password")
        else:
            return("Wrong username")            

@app.get("/randomtoken")
def generate_random_code():
    code = ''.join(random.choices('acbd0123456789', k=10))
    token_list1.append(code)
    return(token_list1)


@app.get("/dictionary")
def root():
    return(list1)

#