# check
def min_opr(n, a):
    all_even = all(x % 2 == 0 for x in a)
    cnt = 0
    if (all_even):
        while (True):
            for i in range(n):
                if (a[i] % 2 != 0):
                    all_even = False
                    break
                a[i] //= 2
            if (all_even):
                cnt += 1
            else:
                break
    return cnt

#main fun
n = int(input())
a = list(map(int, input().split()))
print(min_opr(n, a))
