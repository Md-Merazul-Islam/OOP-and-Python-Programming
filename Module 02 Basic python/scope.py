#global varibale 
balance =1000
def buy_things(items,price):
    global balance
    print(f'Privious balance :{balance}')
    balance-= price
    print(f'After buying {items} new balance {balance}')
    
buy_things("shoes",200)