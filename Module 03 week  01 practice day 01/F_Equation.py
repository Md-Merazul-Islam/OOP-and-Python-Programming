def chek(x,y):
    ans = 0

    for i in range(2,y+1,2):
        ans+=(x**i)
    return ans
x,y= map(int,input().split())
print(chek(x,y))