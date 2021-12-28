# math 메서드로 실행된 결과
from math import gcd, lcm

n1, n2 = map(int,input().split())

print(gcd(n1,n2))
print(lcm(n1,n2))

# GCD 공식을 통한 풀이
def GCD(n1,n2):
    if n2 ==0:
        return n1
    else:
        return GCD(n2, n1%n2)


n1,n2 =  24 ,18
max_num = GCD(n1,n2)
print(max_num)
print(int(n1*n2 / max_num))


