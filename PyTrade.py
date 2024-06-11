import random
def generate_stocks():
    stocks=[
        {"name":"RVNL","price":100,"prev_price":100},
        {"name":"NHPC","price":135,"prev_price":135},
        {"name":"HPCL","price":123,"prev_price":123},
        {"name":"TATA","price":111,"prev_price":111},
        {"name":"IRFC","price":223,"prev_price":223},
        ]
    return stocks
# print(stocks())

def update_stocks(stocks):
    for stock in stocks:
        stock["prev_price"]=stock["price"]
        change=random.uniform(-0.2,0.2)
        newPrice=stock["price"]*(1+change)
        # print(newPrice)
        stock["price"]=newPrice
    return stocks
# stock=stocks() 
# print(stock)
# print("------------")
# print(update_stocks(stock))

def display_portfolio(portfolio):
    money=portfolio["money"]
    stocks=portfolio["stocks"]
    print(f"your current money: {money} and holding shares are: {stocks}")

def buy_stocks(stocks,portfolio):
    stock_name=input("enter your stock name to buy: ").strip().upper()
    quantity=int(input("enter your quantity: "))
    for stock in stocks:
        if stock["name"]==stock_name:
            cost=stock["price"]*quantity
            if portfolio["money"]>=cost:
                portfolio["money"]-=cost
                if stock_name not in portfolio["stocks"]:
                    portfolio["stocks"][stock_name]={"stock":stock_name,"quantity":quantity}
                else:
                    portfolio["stocks"][stock_name]["quantity"]+=quantity
            else:
                print("Insufficient funds to buy stocks")
    return portfolio

def sell_stocks(stocks,portfolio):
    stock_name=input("enter your stock name to sell: ").strip().upper()
    quantity=int(input("enter your quantity: "))
    if stock_name in portfolio["stocks"]:
        if quantity<=portfolio["stocks"][stock_name]["quantity"]:
            # print("yes ")
            portfolio["stocks"][stock_name]["quantity"]-=quantity
            if portfolio["stocks"][stock_name]["quantity"]==0:
                del portfolio["stocks"][stock_name]
            for stock in stocks:
                if stock==stock_name:
                    cost=stock["price"]*quantity
                    portfolio["money"]+=cost
    return portfolio

def total_portfolio(portfolio):
    amount=portfolio["money"]
    for stock,values in portfolio.items():
        


def main():
    print("welcome to the py Trading")
    initial_amount=2000
    simu_days=5
    stocks=generate_stocks()
    portfolio={"money":initial_amount,"stocks":{}}
    for day in range(1,simu_days+1):
        print(f"---day{day}---")
        display_portfolio(portfolio)
        while True:
            for stock in stocks:
                print(stock)
            action=input("enter your option|buy|sell|stay: ").strip().lower()
            print(action)
            if action=="buy":
                buy_stocks(stocks,portfolio)
                print(portfolio)
            elif action=="sell":
                sell_stocks(stocks,portfolio)
                print(portfolio)
            else:
                break
    total_portfolio(portfolio)

main()