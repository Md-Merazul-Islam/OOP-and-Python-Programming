def first_call():
    print("this is first call")

class phone:
    price = 10000
    model = "VIVO"
    color="Green"
    features = ["camera","seaker","hammer"]
    
    #sepcial items
    def call (self):
        print("This is call one person")
    
    def send_sms(self,phone,sms):
        text = f'sending sms to {phone} and msg :{sms}'
        return text

my_phone = phone()
print(my_phone.price)
print(my_phone.color)
print(my_phone.features)
my_phone.call()
ans = my_phone.send_sms(10234098,"hello world")
print(ans)