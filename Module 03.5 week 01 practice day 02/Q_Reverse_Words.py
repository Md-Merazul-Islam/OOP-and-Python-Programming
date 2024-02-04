s = str(input())
st = s.split()
nw = [''.join(reversed(word)) for word in st]
print(' '.join(nw))
