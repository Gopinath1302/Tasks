global op
class Choice:
    @staticmethod
    def first():
        print("Welcome to RG Book Store")
        print("Enjoy Shopping")
        print("--------------------------------------------------")
        flag = True
        while flag:
            global op
            print("Enter 1 for Register")
            print("Enter 2 for Login")
            print("Enter 3 for Logout")
            try:
                op = int(input())
            except ValueError:
                print("Enter Only Numbers")
            else:
                flag = False
                if op == 3:
                    print("Logged out")
                elif op > 3:
                    flag = True
                    print("Enter option Correctly")
                else:
                    return op
