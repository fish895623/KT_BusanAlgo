# BOJ 1715번
# n = 3
# cards = [10, 20, 30, 40]
import heapq
import sys

# n의 갯수
n = int(sys.stdin.readline().rstrip())
# 입력된 카드 수를 담는 리스트

cards = []
# 카드 정보 입력
for i in range(n):
    w = int(sys.stdin.readline().rstrip())
    cards.append(w)

# 카드덱이 1개이면 바꿀 덱이 없기에 교환 0 >> 이거 체크 안하면 런타임 에러 뜸
if len(cards) ==1:
    print(0)
else:
    # 카드 덱이 2개 이상이면 교환하여 최소 몇번 비교하는지 힙을 통해 구함
    # 덱이 [20,40,30,10] 이라고 하면 heapq 구조를 만드면 최소 힙이 되기에
    # 마치 정렬이 자동으로 된다. [10, 20, 30, 40] 구조이다.
    # 최소가 되기 위해서는 힙자료형에 최소 숫자 두개를 더해서 더 한값을 다시 힙 자료형에 push를 한다음
    # 힙 자료형이 빈 리스트가 됐을때 더 이상 바꿀 덱이 없다고 판단하여 종류한다.
    heapq.heapify(cards)
    total = 0
    t = 0

    while cards:
        q1 = heapq.heappop(cards)  # 첫번째 뽑는 카드 수(덱)
        q2 = heapq.heappop(cards)  # 두번째 뽑는 카드 수(덱)
        total = q1 + q2            # 뽑은 덱을 합한다.
        t = total +t               # 뽑힌 합들을 총 합한다
        if not(cards):             # 뽑을 카드 덱이 없다면 break
            break
        else:
            heapq.heappush(cards,total)  # 뽑을 카드가 있다면 total을 push한다

    print(t)
