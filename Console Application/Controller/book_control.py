from View.book_view import bookS
from Model.payment_model import pay
class route:
 @staticmethod
 def goto():
     bookS.book_details()
     pay.payment()