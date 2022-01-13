"""
https://www.acmicpc.net/problem/2470



"""
import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

result_sum = 0
result_list = []
# 투 포인터

start = 0
last = n-1

while start < last:
    result_sum = data[start] + data[last]
    result_list.append([abs(result_sum), data[start], data[last]])

    if abs(data[start]) < abs(data[last]):
        last += -1
    elif abs(data[start]) > abs(data[last]):
        start += 1
    else:
        result_list = [[abs(result_sum), data[start], data[last]]]
        break

result = sorted(result_list, key = lambda x: x[0])
print(result[0][1], result[0][2])
    

