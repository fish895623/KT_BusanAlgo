import sys

try:
    sys.stdin = open("5883.txt", "r")
except FileNotFoundError:
    pass
################################################################################
N = int(sys.stdin.readline())
S = [int(sys.stdin.readline().strip()) for _ in range(N)]
COUNT = 0
################################################################################
mark = -1

# for i in range(N - 1):
#     COUNT = 0
#     temp = S
#     print(temp)
#     while i in temp:
#         temp.remove(i)
#         print(temp)
#     for number in temp:
#         if number == mark:
#             COUNT += 1
#             print(number, mark, COUNT)
#         else:
#             mark = number
#             print(number, mark, COUNT)
#
#     print()

for i in range(N):
    