stock={ 
    "AAPL":291,
    "MSFT":390,
    "AMZN":238,
    "GOOGL":359,
    "TSLA":406,
    "META":566,
    "NFLX":80,
    "NVDA":205

    } 
price=0
while True:
    name=input("Enter the name of stock (or \"Done\" to quit):- ").upper()
    if name=="DONE":
        break
    if name in stock:
        qty=int(input("Enter the quantity:- "))
        invest=stock[name]*qty
        price+=invest
        print(f"Investment on {name} is ${invest}")
    else:
        print("Stock not found")
print(f"Total price of stock portfolio is ${price}")
