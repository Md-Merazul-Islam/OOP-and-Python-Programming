s = input()
n = len(s)
my_list = []

cnt=0
tmp=""
for c in s:
    tmp +=c
    if(c=='L'):
        cnt+=1
    else:
        cnt-=1
    if cnt==0:
        my_list.append(tmp)
        tmp=""
    
print(len(my_list))
for i in my_list:
    print(i)
        