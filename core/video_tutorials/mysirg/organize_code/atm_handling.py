class InsufficientBalance(ZeroDivisionError):
    def __init__(self, arg):
        self.msg = arg


balance = 5000
w = int(input("Enter amount to withdraw: "))
try:
    if w > balance:
        raise InsufficientBalance("Insufficient balance in the account.")
    balance = balance - w
except InsufficientBalance as i:
    print("Exception", i.msg)
else:
    print("Withdraw amount", w, "successfully")
finally:
    print("Current Balance is", balance)
