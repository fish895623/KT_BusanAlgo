import sys
input = sys.stdin.readline().rstrip
a,b,c,d,e,f = map(int, input().split())

'''
# 런타임 에러ㅠ
y = (d*c - a*f) / (b*d - a*e)
x = (c - b*y) / a
print(int(x),int(y))
'''

for i in range(-999,1000):
    for j in range(-999,1000):
        if (a*i)+(b*j)==c and (d*i)+(e*j)==f:
            print(i,j)
