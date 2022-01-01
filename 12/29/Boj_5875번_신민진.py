br_lst = list(input())
N = len(br_lst)
left_bracket = 0
right_bracket = 0
total_bracket = 0
result = 0
for i in range(N):
    if br_lst[i] == '(':
        left_bracket += 1
        total_bracket += 1
    else:
        right_bracket += 1
        total_bracket -= 1
 
    if total_bracket == 1: # 지금까지 나온 여는괄호 '(' 는 변경불가 / 초기화시켜주는거.
        left_bracket = 0
 
    if total_bracket == -1: # 닫는 괄호 ')' 가 오탈자가 되는 기준점
        result = right_bracket
        break # 오탈자가 1개만 존재하므로 for문 다 안돌아도 됨.
 
 
if total_bracket == 2: # for문 다 돌고, 최종 total값이 2면 오탈자가 여는괄호 '('다. / 초기화과정 다 거친 여는괄호 '(' 개수가 변경가능경우의수.
    result = left_bracket
 
print(result)

''' 소스코드는 아래사이트를 참조했습니다!, 기준이 되는 값들, 조건은 이해하기 쉽게 변경하였습니다.
https://welog.tistory.com/273?category=928922 '''