import sys
from collections import deque

IN = "<open>tag<close>"
OUT = "<open>gat<close>"


result = deque()
temp = []
answer = ""
count = 0
words = list(sys.stdin.readline().strip())
state = False
for char in words:
    if char == "<":
        while temp:
            answer += temp.pop()
        result.append(char)
        state = False
    elif char == ">":
        result.append(char)
        state = True
        while result:
            answer += result.popleft()
    elif char == " ":
        if state:
            while temp:
                result += temp.pop()
        else:
            result.append(char)
            while result:
                answer += result.popleft()
    else:
        if state:
            temp.append(char)
        else:
            result.append(char)

while temp:
    answer += temp.pop()
