from sys import stdin
input = stdin.readline

queue_S = []
queue = []
data = input()
data = data.split(" ")
N = int(data[0])
M = int(data[1])


for i in range(N):
    queue_S.append(input())

for i in range(M):
    queue.append(input())

count = 0

for val in queue_S:
    for val2 in queue:
        if val == val2:
            count += 1
        else:
            pass

print(count)
