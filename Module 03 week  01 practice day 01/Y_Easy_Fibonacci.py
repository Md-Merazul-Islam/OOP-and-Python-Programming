def fibonnacci(n):
    a,b=0,1
    ans =[]
    for _ in range(n):
        print(a,end=' ')
        a,b= b,a+b
    return ''
n = int(input())
print(fibonnacci(n))
print(fibonnacci(n))