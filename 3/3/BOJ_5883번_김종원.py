# 1 <= N <= 1000 사람들
# 용량을 마음대로 정한다. 16/ 32/ 64 
# 9S는 자신이 원하는 용량의 크기 B(i)를 점원에게 말하면 정확하게 그 용량을 가진 아이폰 9S를 그자리에서 만들어 구매
# 같은 용량을 원하는 사람이 연속되어 있으면 더 보기 좋을 것으로 판단.
# 특정 사람을 고르고 그 사람이 원하는 용량을 용량을 줄에서 모두 뺀다. ??
# 특정 용량을 골랐을때 같으면 뺀다. -> 최대 길이 구한다.
import sys

n = int(sys.stdin.readline().rstrip())
B = []
for _ in range(n):
    B.append(int(sys.stdin.readline().rstrip()))

uniqueB = list(set(B))

if len(uniqueB) == 1:
    print(1)
else:
    total = []
    for i in range(len(uniqueB)):
        select_number = uniqueB[i]
        dp = []
        count = 0
        max_length = 1
        for j in range(n):
            if select_number == B[j]:
                continue
            if count ==0:
                dp.append((B[j],1))
            else:
                if (B[j] != dp[count-1][0]):
                    dp.insert(count, (B[j],1))
                else:
                    val = dp[count-1][1] + 1
                    dp.insert(count,(B[j],val))
                    if max_length < val:
                        max_length = val
            count+=1
        total.append(max_length)
    print(max(total))