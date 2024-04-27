from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
import starlette.status as status
from starlette.middleware.sessions import SessionMiddleware

app=FastAPI()

SECRET_KEY = "my_secret_key"
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

#create database structure to store dummy data
class Users(BaseModel):
   email :str
   password: str

#input our test data
data = {
   "email": "test",
   "password": "test",
}

# s1=Users(**data)
# print(s1.email)

#signin endpoint: get email/ password from the form
@app.post("/signin", response_class=HTMLResponse)
async def login(request: Request,email: str = Form(None), password: str = Form(None)):
    if email is None or password is None: #if either email or password is empty, redirect to error page please enter user name and password 
        return RedirectResponse(url=f"/error?message=請填寫帳號及密碼", status_code=status.HTTP_302_FOUND)
    else: #if email and password are both provided    
      if email == data["email"] and password == data["password"]: # and it matches our email/password in the data base
          request.session["signed_in"] = True #before redirecting, assin session cookie "signed_in" to true
          return RedirectResponse(url="/member", status_code=status.HTTP_302_FOUND) #redirect to memeber page
      else:
          return RedirectResponse(url=f"/error?message=帳號或密碼輸入錯誤", status_code=status.HTTP_302_FOUND) #if email/password not right, error page
#----------
#create homepage
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    context={'request':request}
    return templates.TemplateResponse("index.html",context)

#create member page
@app.get("/member", response_class=HTMLResponse)
def member(request: Request):
    context={'request':request}
    signed_in = request.session.get("signed_in", False) #retrieve ethe signe_in value, if doesn't exist, return False
    if signed_in:
      return templates.TemplateResponse("member.html",context)
    else:
        return RedirectResponse(url="/")

#create error page
@app.get("/error", response_class=HTMLResponse)
def error(request: Request, message: str=None):
    return templates.TemplateResponse("error.html",{"request": request, "message": message})

#create singout 
@app.get("/signout",response_class=HTMLResponse)
def signout(request:Request):
    request.session["signed_in"] = False
    return RedirectResponse(url="/")



