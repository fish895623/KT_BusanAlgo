'''
백트래킹 : 해를 찾아가는 도중, 지금의 경로가 해가 될 것 같지 않으면 
그 경로를 더이상 가지 않고 되돌아감(가지치기), 즉 모든 가능한 경우의 수 중에서 
특정한 조건을 만족하는 경우만 살펴보는 것

DFS 처럼 모든 경우의 수를 탐색하는 과정에서, 조건문 등을 걸어 답이 절대
될 수 없는 상황을 정의하고, 그런 상황일 경우 탐색을 중지시킨 뒤 그 이전으로
돌아가서 다시 다른 경우를 탐색하게끔 구현
'''

import sys
input = sys.stdin.readline

def dfs(sum_num, answer):
    global cnt
    # n보다 큰 경우 확인할 필요x -> 가지치기
    if sum_num > n:
        return    
    if n == sum_num:
        # k번째 수를 찾기 위함
        cnt += 1
        if cnt == k:
            # 숫자+숫자+숫자+로 기록하므로, 마지막을 제거하고 출력
            print(answer[:-1])
            exit()
    for i in range(1, 4):
        dfs(sum_num + i, answer+str(i)+'+')

cnt = 0
n, k = map(int, input().split())
dfs(0, '')
print(-1)