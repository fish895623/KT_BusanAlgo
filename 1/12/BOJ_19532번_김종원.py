# BOJ_19532번
#-------------------------
# ax + by = c
# dx + ey = f
# ---- x 식 구하기 --------
# adX + bdy = c*d
# adX + eay = f*a
# ---- y 식 구하기 ---------
# aeX + bey = c*e
# bdX + bey = f*b
#-------------------------

import sys

a,b,c,d,e,f = map(int,sys.stdin.readline().rstrip().split())

X = int((c*e - f*b) /(a*e - b*d))
y = int((c*d - f*a) / (b*d - e*a))

print(X,y)