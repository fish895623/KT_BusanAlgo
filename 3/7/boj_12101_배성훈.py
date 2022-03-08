import sys

try:
    sys.stdin = open("3/7/12101.txt", "r")
except FileNotFoundError:
    pass

n, k = map(int, sys.stdin.readline().split())
visited = [False] * (4)
result = []
total = []


def DFS(s):
    global result
    visited[s] = True
    if sum(result) == n:
        total.append(result[:])
        return
    for next in range(1, 4):
        if sum(result) < n:
            result.append(next)
            DFS(next)
            result.pop(-1)


DFS(0)
if len(total) > k - 1:
    # for i in map(str, total_result[k - 1]):
    #     print(i)
    print("+".join(map(str, total[k - 1])))
else:
    print(-1)
