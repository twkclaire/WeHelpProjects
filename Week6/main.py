from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
import starlette.status as status
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root123",
  database="memberdata"
)

app = FastAPI()
SECRET_KEY = "my_secret_key"
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.post("/signup", response_class=HTMLResponse)
async def signup(request: Request,name: str = Form(),username: str = Form(), password: str = Form()):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM member WHERE username = %s", (username,))
    existing_user = mycursor.fetchone()
    if existing_user:    
        return RedirectResponse(url=f"/error?message=帳號已經被註冊", status_code=status.HTTP_302_FOUND)
    else:            
        sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        val = (name, username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)


    
#create homepage    
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    context={'request':request}
    return templates.TemplateResponse("index.html",context)  

#create error page
@app.get("/error", response_class=HTMLResponse)
def error(request: Request, message: str=None):
    return templates.TemplateResponse("error.html",{"request": request, "message": message})

#when sign in, check if username is unique. If unique add to our data base [], if not, show the error message    
#signin endpoint: get username/ password from the form
@app.post("/signin", response_class=HTMLResponse)
async def login(request: Request,username: str = Form(), password: str = Form()):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM member WHERE username=%s and password=%s",(username,password))
    existing_user = mycursor.fetchone()
    if existing_user:
            # request.session["signed_in"] = True #before redirecting, assin session cookie "signed_in" to true
            mycursor.execute("SELECT * FROM member WHERE username=%s and password=%s",(username,password))
            currentuser=mycursor.fetchone()
            currentid=currentuser[0]
            currentusername=currentuser[1]
            request.session.update({"id": currentid, "name": currentusername, "username": username}) 
            return RedirectResponse(url=f"/member", status_code=status.HTTP_302_FOUND) #redirect to memeber page  
    else:
           return RedirectResponse(url=f"/error?message=帳號或密碼輸入錯誤", status_code=status.HTTP_302_FOUND) #if username/password not right, error page
   
# need to change the way message is being shown to the frontend. 
# likelyneed to join memeber and message table but once i have only that i don't need to  care about the loop since it's only name and content
#create member page
@app.get("/member", response_class=HTMLResponse)
def member(request: Request):
    mycursor = mydb.cursor()
    currentusername = request.session.get("name")
    # currentid=request.session.get("id")    
    if currentusername:
        mycursor.execute("SELECT member.name, message.content, message.id FROM member INNER JOIN message on message.member_id=member.id")
        all_messages = mycursor.fetchall()
        return templates.TemplateResponse("member.html",{"request": request, "name": currentusername, "messages":all_messages})
    else:
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)

#create message and get session name post it as name:message return only current user's message. 
#usesql and fet everybody's messages
@app.post("/createMessage",response_class=HTMLResponse)
def createMessage(request:Request,content:str =Form()):
    member_id=request.session.get("id")
    if member_id != None:
        mycursor = mydb.cursor()
        sql = "INSERT INTO message (member_id, content) VALUES (%s, %s)"
        val = (member_id, content)
        mycursor.execute(sql, val)
        mydb.commit()
        return RedirectResponse(url=f"/member", status_code=status.HTTP_302_FOUND) #redirect to memeber page  
    else:
        return RedirectResponse(url=f"/error?message=要登入歐", status_code=status.HTTP_302_FOUND)


class Item(BaseModel):
    message_id:int

@app.post("/deleteMessage")
async def deleteMessage(request: Request, item:Item):
    message_id = item.message_id
    member_id=request.session.get("id")
    if member_id != None:
        mycursor = mydb.cursor()
        sql="DELETE FROM message WHERE id=%s"
        sql_data=(message_id,)
        mycursor.execute(sql,sql_data)
        mydb.commit()
        return RedirectResponse(url=f"/member", status_code=status.HTTP_302_FOUND)
    else:
        return RedirectResponse(url=f"/error?message=要登入歐", status_code=status.HTTP_302_FOUND)
    



#create singout 
@app.get("/signout",response_class=HTMLResponse)
def signout(request:Request):        
    request.session.clear()
    return RedirectResponse(url="/")



#database structure 
# mycursor.execute("CREATE DATABASE memberdata")
# mycursor.execute("CREATE TABLE member (id BIGINT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255) NOT NULL, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL)")
# mycursor.execute("CREATE TABLE message(id BIGINT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255) NOT NULL, username VARCHAR(255) NOT NULL, message VARCHAR(255) NOT NULL)")
#mycursor.execute("CREATE TABLE message(id BIGINT PRIMARY KEY AUTO_INCREMENT, member_id BIGINT NOT NULL, content varchar(255) NOT NULL, FOREIGN KEY(member_id) REFERENCES member(id))")


