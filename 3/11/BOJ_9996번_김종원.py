# 알파벳 소문자 여러 개와 별표(*) 하나로 이루어진 문자열


import re,sys

N = int(sys.stdin.readline().strip())
pattern = sys.stdin.readline().strip()
n1, n2 = pattern.split("*")
pattern = '^'+n1+"[a-z]*"+n2+'$'
p = re.compile(pattern)

for _ in range(N):
    file = sys.stdin.readline().strip()
    # print(p.search(file).group())
    if p.search(file) == None:
        print("NE")
    else:
        print("DA")




