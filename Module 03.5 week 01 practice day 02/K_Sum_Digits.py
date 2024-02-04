n = int (input())
st = str(input())
sum =0
for i in range(len(st)):
    digit = int(st[i])
    sum+=digit
print(sum)