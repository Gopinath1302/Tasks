from Model.login_model import login
from Model.dbconnection_model import db,cursor
import re
class Register():
    @staticmethod
    def register_user(username, password, name, phonenumber):

        query = "INSERT INTO logindetails (username, paasword, name,number) VALUES (%s, %s, %s, %s)"
        values = (username, password, name, phonenumber)
        cursor.execute(query, values)

        db.commit()

    @staticmethod
    def getin():
        flag = True
        regex = ("(?=.*[a-z])(?=.*[A-Z]).+$")
        check = re.compile(regex)
        while flag:
            username = input("Enter the Username:\n")
            query = "Select username from logindetails where username=%s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            if re.search(check, username) and result is None:
                flag = False
            else:
                print("Invalid Username! or \n User name already exist\nPlease try to enter a valid username!")
        regex = ("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
        check = re.compile(regex)
        flag = True
        while flag:
            password = input("Enter the password:\n")
            if re.search(check, password):
                flag = False
            else:
                print("Invalid password!\nPlease try  to enter a valid password")
        name = input("Enter your Name: ")
        flag = True
        while flag:
            try:
                mobile = int(input("Enter your Mobile number:\n"))
            except:
                print("Invalid entry !\nPlease try  to enter a valid Mobile number")
            else:
                if 6000000000 < mobile < 10000000000:
                    flag = False
                else:
                    print("Invalid Mobile number!\nPlease try  to enter a valid Mobile number")
        Register.register_user(username, password, name, mobile)
        login.check()
