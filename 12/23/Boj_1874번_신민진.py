from sys import stdin

N = int(stdin.readline()) # 얼마까지의 수열인가를 나타냄
stack = [] # 스택
inc_num = 1 # 점점 증가하는 수(스택에 넣는)
result = [] # 결과값

for i in range(N): # N만큼 시행을 반복
    num = int(stdin.readline()) # 들어오는 입력값 + 시간절약

    # num까지 stack에 넣음
    while inc_num <= num:
        stack.append(inc_num)
        result.append('+')
        inc_num += 1

    # 스택 맨 끝 값이 입력값(num)과 같으면 pop
    if stack[-1] == num:
        stack.pop()
        result.append('-')
        
    # 스택 맨 끝 값이 입력값(num)과 다르면 'NO'출력
    else:
        print('NO')
        exit(0) # 이 줄 빼면 오류남!!! , sys 모듈함수임

# append 시킨 result값 출력
for i in result:
    print(i)