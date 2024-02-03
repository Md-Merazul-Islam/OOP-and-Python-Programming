t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if (x > y):
        x, y = y, x
    sum = 0
    for i in range(x+1, y):
        if (i % 2 == 1):
            sum += i
    print(sum)
