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
    