# def full_name(first, last):
#     name = f'{first} {last}'
#     return name

# name = full_name("Merazul","Islam")
# print(name)


# def full_name(first, last):
#     name = f'{first} {last}'
#     return name
# a= "yes"
# b= "No"
# name = full_name(a,b)
# print(name)
# name = full_name(last="yes",first="no")
# print(name)

# def famous_name(first, last, **aditional):
#     name= f'{first} {last}'
#     print(aditional['title'])
#     return name
# name = famous_name(first="Merazul",last="Islam",title='Jonuir', aditional="Programmer")
# print(name)


# def famous_name(first, last, **aditional):
#     name= f'{first} {last}'
#     # print(aditional['title'])
#     for key,val in aditional.items():
#         print(key,val)
#     return name
# name = famous_name(first="Merazul",last="Islam",title='Jonuir', aditional="Programmer")
# # print(name)



# return multiple value

def a_lot (n1,n2):
    s1= n1-n2
    s2= n1+n2
    s3=n1*n2
    return s1,s2,s3
ans = a_lot(2,5)
# print(ans)