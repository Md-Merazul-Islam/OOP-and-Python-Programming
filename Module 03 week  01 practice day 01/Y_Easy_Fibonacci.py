def fibonnacci(n):
    a,b=0,1
    ans =[]
    for _ in range(n):
        print(a,end=' ')
        a,b= b,a+b
    return ''
#input
n = int(input())
print(fibonnacci(n))