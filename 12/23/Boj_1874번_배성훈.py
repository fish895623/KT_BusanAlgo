import sys

input = sys.stdin.readline

n = int(input())
targets = [int(input()) for _ in range(n)]
current = 1
stack, answer = [], []

for target in targets:
    while current <= target:
        stack.append(current)
        answer.append("+")
        current += 1

    if stack[-1] == target:
        answer.append("-")
        stack.pop()

if not stack:
    print("\n".join(answer))
else:
    print("No")
