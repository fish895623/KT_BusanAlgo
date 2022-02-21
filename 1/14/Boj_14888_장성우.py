"""
https://www.acmicpc.net/problem/14888


최대값 : 최대값은 곱하기부터
최솟값 : 최대값을 만들어서 음수 * 양수  최대?
몰라 그냥 다돌아

"""
import itertools
n = int(input())

data = list(map(int, input().split()))

oper_list = []
for i, oper in enumerate(list(map(int, input().split()))):
    if i == 0:
        for _ in range(oper):
            oper_list.append("+")
    elif i == 1:
        for _ in range(oper):
            oper_list.append("-")
    elif i == 2:
        for _ in range(oper):
            oper_list.append("*")
    else:
        for _ in range(oper):
            oper_list.append("/")

all_oper = list(itertools.permutations("".join(oper_list), n-1))

sum_data = []

for oper in all_oper:

    first_num = data[0]

    for i in range(n-1):
        if oper[i] == "+":
            first_num += data[i+1]
        elif oper[i] == "-":
            first_num -= data[i+1]
        elif oper[i] == "*":
            first_num = int(first_num * data[i+1])
        else:
            first_num = int(first_num / data[i+1])
        
    sum_data.append(first_num)

print(max(sum_data))
print(min(sum_data))

