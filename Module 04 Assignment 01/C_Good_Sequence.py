def isGood (n,a):
    cnt = {}
    for val in a:
        if(val in cnt):
            cnt[val]+=1
        else :
            cnt[val]=1
    opr=0
    for val ,frq in cnt.items():
        if(frq>= val):
            opr +=abs (val-frq)
        else :
            opr+= frq
    return opr
    
    
#input: 
n = int(input())
a = map(int,input().split())
print(isGood(n,a))
