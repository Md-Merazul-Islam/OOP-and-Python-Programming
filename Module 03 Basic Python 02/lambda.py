# # ans = lambda x ,y : x**y
# # print(ans(20,2))

# # double = lambda x: x*2
# # numbers= [2,5,6,7,8,9]
# # double_nums= map(double, numbers)
# # print(numbers)
# # print(list(double_nums))

# # ans = map(lambda x: x*2,numbers)
# # print(list(ans))


# actors=[
#     {'name':'meraz','age':65},
#     {'name':'akash','age':45},
#     {'name':'robin','age':35},
#     {'name':'rajib','age':35},
# ]
# ans = filter(lambda actors: actors['age']<40, actors)
# print(list(ans))


numbers = [9, 15, 2, 36]
numbers = [9, 15, 2, 36]
numbers[1:4] = [20, 14, 36]
print(numbers)
try:
    result =20//5
except:
    print("error happened")
finally:
    print("finally here")