import sys
n = int(input())
mylist = list(map(int, input().split()))

mx = max(mylist)
mn = min(mylist)
i = 0
j = 0
for ind, key in enumerate(mylist):
    if (key == mx):
        i = ind
    if (key == mn):
        j = ind
mylist[i], mylist[j] = mylist[j], mylist[i]
print(*mylist, sep=' ') # this in a method print without bracket and comma