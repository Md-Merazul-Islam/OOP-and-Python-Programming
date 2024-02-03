myset = [10,2,3,1,4,20,4,55,6,7,8,3,5,6,9]
print(myset)
my_set = set(myset)
print(my_set)
my_set.add(128)
print(my_set)
my_set.remove(5)
print(my_set)

for it in my_set:
    print(it,end=' ')
print ('')
if 23 in my_set:
    print("hello")
elif 20 in my_set:
    print("yes it's has")
else :
    print("no")
    
    