# sample={
#     "class":{
#         "student":{
#             "name":"Meraz",
#             "mark":{
#                 "physics": 70 ,
#                 "history":80
#             }
#         }
#     }
# }

# print("name:",)
t =int(input())
for i in range (t):
    a = list(input())
    a.reverse()
    ans = " ".join(a)
    print(*a)
    print(ans)
