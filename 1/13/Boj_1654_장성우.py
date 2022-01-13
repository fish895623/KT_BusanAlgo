"""
https://www.acmicpc.net/problem/1654

"""

k, n = map(int, input().split())

data = []
for _ in range(k):
    data.append(int(input()))

max_data = max(data)
first_data = 1

while True:
    result = 0

    if first_data > max_data:
        break

    
    mid = (first_data + max_data) // 2


    for i in data:
        result += i//mid
    
    if result < n:
        max_data = mid-1
    else:
        len_data = mid
        first_data = mid+1
print(len_data)