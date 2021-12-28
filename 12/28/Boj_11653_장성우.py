"""
https://www.acmicpc.net/problem/11653

소인수분해

소수 판별하고 그 값으로 나누기

소수를 1000만까지 확인할려면 dp에 저장하는거 말고 방법이 있나?



"""
import math
n = int(input())

while True:
    cnt = 0
    for i in range(2, int(math.sqrt(n))+1):

        if n % i == 0:
            n = n / i
            print(i)
            cnt = 1
            break
    
    if cnt == 0:
        print(int(n))
        break


