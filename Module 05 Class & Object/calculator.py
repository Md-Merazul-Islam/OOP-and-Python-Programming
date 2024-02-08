class calculator:
    brand = "casion MS990"
    
    #sum
    def sum(self,a,b):
        return a+b
    def sub (self,a,b):
        return a-b
    def div(self,a,b):
        return a/b
    def mul (self,a,b):
        return a*b
print("Enter the first num :")
a= int(input())
print("What operation do you want (+, -, /, *):")
s = input()
print("Enter the value of snd :")
b= int(input())
calc = calculator()



if s == "+":
    ans = calc.sum(a,b)
    print(ans)
elif s == "-":
    ans = calc.sub(a,b)
    print(ans)
elif s == "/":
    ans = calc.div(a,b)
    print(ans)
else :
    ans = calc.mul(a,b)
    print(ans)
    
