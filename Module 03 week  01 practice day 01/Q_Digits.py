def print_numbers(s):
    for i in range(len(s)-1,-1,-1):
        print(s[i], end=" ")
    print('')
    return ''


# input
t = int(input())
for _ in range(t):
    s = str(input())
    print_numbers(s)
