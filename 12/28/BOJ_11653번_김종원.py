# 11653번 문제

num = int(input())
num = 72 
while True:
    if num == 1:
        break
    for n in range(2, num+1):
        if num % n == 0:
            num = num//n
            print(n)
            break


