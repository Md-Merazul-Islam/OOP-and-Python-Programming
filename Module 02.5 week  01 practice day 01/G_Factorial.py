def factorial(n):
    ans =1
    for i in range(n):
        ans = ans+(ans*i)
    print(ans)


#input
t = int(input())
for _ in range(t):
    n = int(input())
    factorial(n)