# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 25, 35, 45]
# odds = []
# for num in numbers:
#     if num % 2 == 1 and num % 5 == 0:
#         odds.append(num)
# print(odds)
# odd_num = [num for num in numbers if num %2]
# print(odd_num)

# players =['sakib','musfik','liton']
# ages =[23,34,56]

# age_com =[]
# for player in players:
#     print('Player : ',player)
#     for age in ages:
#         print(player,age)
#         age_com.append([player,age])
# print(age_com)
# age_com2 = [[player,age] for player in players for age in ages]
# print(age_com2)


def display_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


display_person(Name="Amir Khan", Age="45")
