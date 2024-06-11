def stocks():
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
        change=random.randint(-0.2,0.2)
    
