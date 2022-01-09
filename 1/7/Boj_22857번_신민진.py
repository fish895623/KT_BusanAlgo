N, K = map(int, input().split())
lst = list(map(int, input().split()))

odd = 0
odd_lst = []
for i in range(N):
    if lst[i] % 2 == 0:
        odd_lst.append(odd)
        odd = 0
    else:
        odd += 1

length = len(odd_lst)

# 홀수만 있는 경우
if length == 0:
    print(0)

# 짝수가 1개만 있는 경우
elif length == 1:
    print(1)

# 짝수 2개 이상, 비교가능할 때
else :
    odd_lst[0] = 1000001
    cnt_lst = []

    for i in range(length - 1):
        n = i
        cnt = 1
        sum = 0
        if odd_lst[n] > odd_lst[n + 1]:
            while(sum <= K and n < length):
                n = n + 1
                if (n == length):
                    break
                sum += odd_lst[n]
                if(sum > K):
                    break
                cnt += 1
            cnt_lst.append(cnt)
        
        
        else:
            while(sum <= K and n < length):
                sum += odd_lst[n]
                if(sum > K):
                    break
                n = n + 1
                cnt += 1
            cnt_lst.append(cnt)

    print(max(cnt_lst))