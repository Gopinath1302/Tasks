from Controller.book_control import route
from Model.dbconnection_model import db,cursor
class login:
    @staticmethod
    def authenticate_user(username, password):

        query = "SELECT * FROM logindetails WHERE username = %s AND paasword = %s"
        cursor.execute(query, (username, password))

        result = cursor.fetchone()
        return result is not None
    @staticmethod
    def check():
        entered_username = input("Enter your username: ")
        entered_password = input("Enter your password: ")
        if login.authenticate_user(entered_username, entered_password):
            print("Login successful. Proceed with further actions.")
            route.goto()
        else:
            print("Invalid username or password. Login failed. \n")
            print(" Enter 1 for Login again \n Enter 2 for Register \n Enter 3 for logout")
            opt = int(input())
            if opt == 1:
                login.check()
            elif opt == 2:
                pass
            else:
                print("Logout")
