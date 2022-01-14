# 총합 = n(n+1)/2
# 2 * 총합 = n**2 + n

S = int(input()) *2

total = 0
n = 1
while True:
    total = n *(n+1) 
    if total <= S:
        n+=1
    else:
        break
print(n-1)


