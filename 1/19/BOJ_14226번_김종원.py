# 영선이는 기뻐서 효빈이에게 스마일 이모티콘을 S개를 보낸다.
# 영선이는 이미 화면에 1개를 입력했다.
# 연산 3가지를 사용해 S개를 만들어보려고 한다.
# 1. 복사해서 클립보드 저장 -> 스택에 저장
# 2. 스택에 저장된(클립보드) 이모티콘 양만큼 붙여넣는다.
# 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
# 연산 모두 1초 

# S가 6개
# 자료형 num(num1) -> num : 화면, num1 : 클립보드
# 0(0) -> 1(0) -> 2(0) -> 3(0) -> 3(3) -> 6(0)
#   1초     1초     1초     4초      5초
# 1(0) -> 1(1) -> 1(2) -> 3(2) -> 3(3)-> 6(3) -> 6(4)-> 10(4) ->10(5) -> 15(5) -> 20(5) -> 19(5)
# 1(0) -> 1(1) -> 1(2) -> 1(3) -> 4(3) ->4(4) -> 4(5) ->9(5)



import sys
from collections import deque

target =int(sys.stdin.readline().rstrip())
startNum = 0

q = deque()
# (윈도우수, 클립보드수, 시간)
q.append((1,0,0))
minTime =0
while q:
    windowCnt,clipCnt,currentTime = q.popleft()
    # print("windowCnt : ", windowCnt, " ClipCnt : ",clipCnt, " currentTime : ", currentTime)
    if windowCnt == target:
        minTime = currentTime
        break
    elif windowCnt -1 == target or windowCnt + clipCnt == target:
        minTime = currentTime+1
        break
    for choice in [1,2,3]:
        if choice == 1 and ((windowCnt) <= target and (clipCnt+windowCnt<=target)):
            q.append((windowCnt, clipCnt+windowCnt, currentTime+1))
        elif choice ==2:
            if clipCnt !=0 and ((windowCnt + clipCnt) <= target and (clipCnt <=target)):
                q.append((windowCnt + clipCnt, 0, currentTime+1))
        else:
            if windowCnt >1  and ((windowCnt -1) <= target and (clipCnt <=target)):
                q.append((windowCnt -1 ,clipCnt, currentTime+1))
print(minTime)
