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