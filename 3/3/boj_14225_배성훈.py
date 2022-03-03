import sys

try:
    sys.stdin = open("14225.txt", "r")
except FileNotFoundError:
    pass
################################################################################
n = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
MAX = 20 * 100000
ANSWER = []
################################################################################


def dfs(val, idx):
    if idx == n:
        return 0
    val += S[idx]
    ANSWER.append(val)
    dfs(val, idx + 1)
    val -= S[idx]
    dfs(val, idx + 1)


dfs(0, 0)
ANSWER = set(ANSWER)
for number in range(1, MAX):
    if number not in ANSWER:
        print(number)
        break
