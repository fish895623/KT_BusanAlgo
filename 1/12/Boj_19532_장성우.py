"""
https://www.acmicpc.net/problem/19532


ax + by = c
dx + ey = f

ae x + be y = ce
bd x + be y = bf
 x = (ce - bf)/ (ae-bd)


ad x + db y = cd
ad x + ae y = af

(db - ae) y = cd - af
y = (cd - af) / (db - ae)
x = ()
x = (c-by)/a

"""

a, b, c, d, e, f = map(int, input().split())

y = (c*d - a*f) / (d*b - a*e)
x = (c * e - b*f) / (a*e - b* d)

print(int(x), int(y))