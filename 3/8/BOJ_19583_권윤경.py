def minute(s):
    return int(s[0:2]) * 60 + int(s[3:])

start, end, last = input().split()

array = []
while True:
    try:
        array.append(input().split())
    except:
        break

start=minute(start)
end=minute(end)
last=minute(last)

a1 = set()
a2 = set()
for t, n in array:
    t = minute(t)
    if t <= start:
        a1.add(n)
    elif end <= t <= last:
        a2.add(n)

print(len(a1 & a2))

