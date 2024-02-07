# *args
"""
    -> *args allows to pass a varibale number of positional arg to a function.
    -> the * before args indicate any numbers of positioanl arg can be passed 
       to the function and they will collected into a tuple..
    
"""
def sum (*args):
    ans =0
    for i in args:
        ans+=i
    return ans

ans = sum(2,3,4,6)
print("the sum is : ",ans)



# **kwargs
"""
    -> **kwargs allow to pass a variable number of keyword arg to a function.
    -> the ** before kwargs indicares that any numbers of keyword
       arg can be passed to the fun and they will be collected into a 
       dictionary.
"""

def call(**kwargs):
    for key, val in kwargs.items():
        print(f'{key} : {val}')

call(Name="Merazul Islam", Roll=672581,Group = 'A',Blood_Group='O+')
