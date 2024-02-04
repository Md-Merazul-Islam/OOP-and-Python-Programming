n,q= map(int,input().split())
mylist = list(map(int,input().split()))
prsum = [0]*(n+1)
for i in range (1,n+1):
    prsum[i]= prsum[i-1]+mylist[i-1]
# print(prsum)

while(q):
    l,r= map(int,input().split())
    sum= prsum[r]- prsum[l-1]
    print(sum)
    q-=1