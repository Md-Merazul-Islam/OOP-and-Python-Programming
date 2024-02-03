#global varibale 
balance =1000
def buy_things(items,price):
    global balance
    print(f'Privious balance :{balance}')
    balance-= price
    print(f'After buying {items} new balance {balance}')
    
buy_things("shoes",200)

numbers =[7,8,5,4,3,2,4]
print(numbers[::-1])