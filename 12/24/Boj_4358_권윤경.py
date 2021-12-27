s=[]
while True:
    try:
        s.append(input())
    except:
        break

s.sort()
from collections import Counter
dic = dict(Counter(s))
for i,v in dic.items():
    print("{} {:.4f}".format(i,round(v/len(s)*100,4)))