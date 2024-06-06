def initializeWallet():
    wallet={"balance":0,"Trans_History":[]}
    return wallet
# print(initializeWallet())

def display_balance(wallet):
    bal=wallet["balance"]
    print(f"Current Balance in the wallet is: {bal}")
    return 
# wallet=initializeWallet()
# display_balance(wallet)
    
def addFunds(wallet,amount):
    if amount<=0:
        print("amount can't be negative")
    else:
        wallet["balance"]+=amount
        wallet["Trans_History"].append(amount)
        print(f"{amount} added to the wallet")
    return 
# wallet=initializeWallet()
# addFunds(wallet,100)
# display_balance(wallet)

def makePayment(wallet,amount):
    if amount>wallet["balance"]:
        print("insufficient funds in your wallet")
    else:
        wallet["balance"]-=amount
        wallet["Trans_History"].append(-amount)
        print("payment done succesfully")
        return 
# wallet=initializeWallet()
# addFunds(wallet,100)
# display_balance(wallet)
# makePayment(wallet,30)
# print(wallet)
# display_balance(wallet)

def transaction_History(wallet):
    transc=wallet["Trans_History"]
    return f"Your wallet transaction history: {transc}"

# wallet=initializeWallet()
# addFunds(wallet,100)
# makePayment(wallet,30)
# print(transaction_History(wallet))
    
def useWallet():
    print("Welcome to the digital wallet")
    wallet=initializeWallet()
    while True:
        print("1 >> View balance")
        print("2 >> Add Funds")
        print("3 >> Make a Payment")
        print("4 >> View trans history")
        print("5 >> Exit")
        user_choice=int(input("please enter your chouce: "))
        if user_choice==1:
            display_balance(wallet)
        if user_choice==2:
            amount=int(input("enter your amount to add: "))
            addFunds(wallet,amount)
        if user_choice==3:
            amount=(int(input("enter your amount to make payment: ")))
            makePayment(wallet,amount)
        if user_choice==4:
            print(transaction_History(wallet))
        if user_choice==5:
            break
    print("Thanks for using digita wallet")

useWallet()