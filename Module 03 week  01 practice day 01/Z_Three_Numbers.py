def numbers(k,s):
    cnt =0
    for i in range (k+1):
        for j in range(k+1):
            z = s-i-j
            
            if(0<=z <=k):
                cnt+=1
    return cnt
#input

k,s = map(int,input().split())
print(numbers(k,s))