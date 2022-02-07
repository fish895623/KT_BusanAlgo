# array = ['(', '0', '/', '(', '0', ')', ')']
# print(array)
from itertools import combinations
array = list(input())
stack, pos, answer = [], [], set()

for i, v in enumerate(array):
    if v == '(':
        stack.append(i)
    if v == ')':
        pos.append((stack.pop(), i))

for i in range(1, len(pos)+1): # 현재 pos에 존재하는 쌍들의 조합을 만들기 위해서 1개부터 pos 개수 만큼 for문 돌려서 만드는 것
    comb = list(combinations(pos, i))
    for j in comb:
        tmp = array[:]
        for idx1, idx2 in j:
            tmp[idx1]= ""
            tmp[idx2]= ""
        answer.add("".join(tmp))   

for i in sorted(list(answer)):
    print(i)     