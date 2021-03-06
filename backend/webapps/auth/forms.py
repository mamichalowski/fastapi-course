from fastapi import Request, requests
from typing import Optional
from typing import List


class LoginForm:
    def __init__(self,request:Request):
        self.request : Request = request
        self.errors : List = []
        self.username : str = None
        self.password : str = None

    async def load_data(self):
        form = await self.request.form()
        self.username = form.get("email")
        self.password = form.get("password")

    async def is_valid(self):
        if not self.username or (not self.username.__contains__("@")):
            self.errors.append("Valid email is mandatory")
        if not self.password or len(self.password) >= 6 :
            self.errors.append("Password need to by >= 6")
        
        if not self.errors:
            return True
        else:
            return False

                
