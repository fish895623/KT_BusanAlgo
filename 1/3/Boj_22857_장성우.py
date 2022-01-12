"""
https://www.acmicpc.net/problem/22857


1) +와 -가 연속적으로 있는것은 더하기 (+는 +1 , -는 -1)
2) 만약 첫번째 연속적으로 있는 데이터가 -인경우 없앤다.


쉽게 다음과 같이 숫자가 있다고 해보자.

1 1 1 2 2 2 1 1 2 2 2 2 1 1 2 2 2 2 2 1 1 2
홀수 최대 3개까지 제거 가능

홀수와 짝수의 갯수를 배열에 따로 저장해놓는다.

홀수 짝수 홀수 짝수 홀수 짝수 홀수 짝수 
 -3   +3   -2   +4  -2   +5  -2  +1


1) 첫번째 홀수는 의미없음 ( 짝수의 최대 갯수가 필요한데 초반 홀수는 없는게 더 많은 짝수를 넣을 수 있으니까.. )

2) 짝수 3 저장

even_stack [3]
odd_stack []
result = []

3) 홀수 2 저장 (아직 3보다 적으므로 다음 짝수 확인)

even_stack [3]
odd_stack [2]
result []

4) 짝수 4 저장

even_stack [3,4]
odd_stack [2]
result []

5) 홀수 2저장 이때 홀수값이 3보다 크므로 result에 even 합 저장 그리고 이전 짝수 하나와 홀수 제거

even_stack [3, 4]
odd_stack [2, 2]
result [7]
->
even_stack [4]
odd_stack [2]

6) 짝수 5 저장
even_stack [4, 5]
odd_stack [2]
result [7]

7) 홀수 2 저장 -> 홀수값이 3보다 크므로 result에 even 합 저장 그리고 이전 짝수 하나와 홀수 제거

even_stack [4, 5]
odd_stack [2, 2]
result [7, 9]
->
even_stack [5]
odd_stack [2]
result [7, 9]

이렇게 끝까지 진행 후 마지막에 max(result) 출력

시간복잡도 거의 O(n) + 조건문 계산...

data 짝수 홀수 검사 -> n
홀수 짝수의 합이 저장된 data 길이 = k

O(n+k) 최대 O(2n)


"""

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))




data_result = []

even = 0
odd = 0

for i in data:
    # 들어온 데이터가 짝수인 경우
    if i%2==0:
        if odd != 0:
            data_result.append(odd)
            odd = 0

        even +=1

    # 들어온 데이터가 홀수인 경우
    if i%2!=0:
        if even != 0:
            data_result.append(even)
            even = 0

        odd -=1

# 이거 처리안해줘서 92퍼에서 멈췄었다.
if odd != 0:
    data_result.append(odd)
elif even != 0:
    data_result.append(even)

minus_s = []
plus_s = []

result = []
try:
    # 첫번째 데이터가 0보다 작은경우 첫 데이터 없애기
    if data_result[0] < 0:
        data_result.pop(0)
except:
    pass

for data_result_num in data_result:
    if data_result_num < 0:
        minus_s.append(data_result_num)
    else:
        plus_s.append(data_result_num)

    while True:

        if abs(sum(minus_s)) > k:
            minus_s.pop(0)

            if len(plus_s) !=0:
                plus_s.pop(0)

        if abs(sum(minus_s)) <= k:
            break

    result.append(sum(plus_s))

if len(result) == 0:
    print("0")
else:
    print(max(result))


# queue 사용해서도 진행 -> 더 속도가 안나왔음
# import sys
# from collections import deque
# input = sys.stdin.readline

# n, k = map(int, input().split())
# data = list(map(int, input().split()))

# for i in data:
#     # 들어온 데이터가 짝수인 경우
#     if i%2==0:
#         if odd != 0:
#             data_result.append(odd)
#             odd = 0

#         even +=1

#     # 들어온 데이터가 홀수인 경우
#     if i%2!=0:
#         if even != 0:
#             data_result.append(even)
#             even = 0

#         odd -=1

# # 이거 처리안해줘서 92퍼에서 멈췄었다.
# if odd != 0:
#     data_result.append(odd)
# elif even != 0:
#     data_result.append(even)

# minus_s = deque()
# plus_s = deque()

# result = []
# try:
#     # 첫번째 데이터가 0보다 작은경우 첫 데이터 없애기
#     if data_result[0] < 0:
#         data_result.popleft()
# except:
#     pass

# for data_result_num in data_result:
#     if data_result_num < 0:
#         minus_s.append(data_result_num)
#     else:
#         plus_s.append(data_result_num)

#     while True:

#         if abs(sum(minus_s)) > k:
#             minus_s.popleft()

#             if len(plus_s) !=0:
#                 plus_s.popleft()

#         if abs(sum(minus_s)) <= k:
#             break

#     result.append(sum(plus_s))

# if len(result) == 0:
#     print("0")
# else:
#     print(max(result))







