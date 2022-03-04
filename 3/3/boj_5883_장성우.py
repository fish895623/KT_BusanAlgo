"""
https://www.acmicpc.net/problem/5883

"""
# 일단 최악의 경우로 풀어보자. --> 되네? .. 엄청 빡빡하게는 안줬나보다.


data = []
for _ in range(int(input())):

    data.append(int(input()))

last_data = -1
cnt = 0
result_cnt = 0
# 제거할 데이터들을 하나씩 불러온다.
for i in set(data):
    for j in data:

        if j != i: # 제거될 데이터는 빼고 본다.
            if last_data != j: # 데이터가 이전 데이터랑 다를 경우
                result_cnt = max(result_cnt, cnt)
                last_data = j
                cnt = 1
            else:
                cnt += 1
result_cnt = max(result_cnt, cnt)

print(result_cnt)
