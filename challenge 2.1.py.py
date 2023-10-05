￼class BankAccount:
def_init_(self, account_number, account_holder_name, initial_balance=0.0):
   self._account_number=account_number
     self. _account_holder_=name=account_holder_name
    self. _account_holder_name=account_holder_name
    self. _account_balance=initial_balance
def depasite(self, amount):
  if amount>0:
    self. _account_balance+=amount
         print("Deposited ₹{}.New, balance:₹{}".format(amount, self.__account_balance))
  else:
    print ("invalid deposit amount. ")
   def, withdraw (self, amount):
     if amount>0and amount<=._account_balance:
    self. _account_balance=amount
     print (" withdraw₹{}.Newbalance:₹{}."format(amount)) 
else:
     print ("invalid withdraw amount or insufficient balance. ") 
def display_balance(self):
    print (" Account balance for {}(account#{}) :₹{}".format(self._account_holder_name, self. _account_number, self. _account_balance)) 
account=BankAccount(account_number="123456789", account_holder_name="Maha",initial_balance=5000.0) 
account. display_balance ()
account. deposite(500.0)
account . withdraw (200.0)
acount. display_balance () 