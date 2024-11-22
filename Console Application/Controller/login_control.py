from View.home_view import Choice
from Model.login_model import login
from Model.register_model import Register
class User_choise:
 a =Choice.first()
 if a==1:
   Register.getin()
 elif a == 2:
    login.check()