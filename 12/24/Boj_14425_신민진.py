from sys import stdin

N, M = map(int, stdin.readline().strip().split())
S = {} # 딕셔너리 O(1), 시간복잡도 고려
cnt = 0 # 개수 초기값 설정

for _ in range(N):
    S[stdin.readline().strip()] = True # S에 N개의 key값 저장
    
for _ in range(M):
    if stdin.readline().strip() in S: # M개, S에 존재하는지 확인
        cnt += 1

print(cnt)