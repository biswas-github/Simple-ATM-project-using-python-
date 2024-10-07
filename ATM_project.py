current_balance=10000
assert current_balance>=0
print("welcome to the atm service  :")
while True:
    User_options="""
     choose 1 for check balance
     choose 2 for deposit
     check 3 for withrawl
     4 exit
     """
    choice=int(input("enter your choice"))
    if choice==1:
        print(f"the amount in bank is as :-{current_balance}")
    elif choice==2:
        money=int(input("enter the amount to deposit"))
        current_balance=current_balance+money
        print(f"the money after deposit is {current_balance}")
    elif choice==3:
        withdraw=int(input("enter the withdraw amt"))
        if withdraw<=current_balance:
            current_balance=current_balance-withdraw
            print(f"the amount: {withdraw} is withdraen")
        else:
            print("the withdrawa amt is greater than the current balance")
    elif choice==4:
        print("we are now  exiting   ....")
        break
    else:
        print("enter the valid option :\n")