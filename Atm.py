# setting the basic amount in the account as 1000
bal = 1000

# creating the class atm
class atm:
    # creating the constructor "__init__" function
    def __init__(self,atm_card_number,pin_number):
        self.atm_CN = atm_card_number
        self.pin_N = pin_number

    # creating the cash_withdrawl method
    def cash_withdrawl():
        withdrawl_amount = float(input("Enter the amount that needs to be withdrawed:"))
        if withdrawl_amount > bal:
            print("Your present balance in the account is less than the amount you want to withdraw")
            print("Your present balance is:"+bal)
        else:
            bal = bal - withdrawl_amount
            print("Transaction complete")
            print("Please collect your receipt")

    # creating the balance enquire function
    def balace_enquiry():
        print("Your present balance in the account is :"+bal)
    
    # creating the cash deposit function
    def cash_deposit():
        deposit_amount = float(input("Enter the amount to be depostited"))
        bal = bal + deposit_amount
        print("Transaction complete")
        print("Present balance is :"+bal)