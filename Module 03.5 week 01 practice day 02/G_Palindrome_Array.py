def ispalindrome(ls):
    return ls==ls[::-1]

#main fun
n = int(input())
mylist= list(map(int,input().split()))
if (ispalindrome(mylist)):
    print("YES")
else : 
    print("NO")