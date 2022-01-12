# number_list = [(123,1,1), (356,1,0),(327, 2,0),(489, 0,1)]

# 완전 탐색 문제

N = int(input())
number_list = []

for _ in range(N):
    n1,n2,n3 = map(int,input().split())
    number_list.append((n1,n2,n3))
answer = 0

for num in range(123,987+1,1):
    num = str(num)
    if (num[0] == num[1]) or( num[0] == num[2]) or (num[1] == num[2]) or (num[0] =="0" or num[1] =="0" or num[2] =="0"): 
        continue
    flag = True
    for selectNum, s,b in number_list:
        selectNum = str(selectNum)
        strike,ball = 0,0
        for a1 in range(3):
            for b1 in range(3):
                if (a1 == b1 and num[a1] == selectNum[b1]):
                    strike +=1
                elif (a1 != b1 and num[a1] == selectNum[b1]):
                    ball+=1

        if strike != s or ball != b:
            flag = False
            break
    if flag:
        answer +=1
print(answer)