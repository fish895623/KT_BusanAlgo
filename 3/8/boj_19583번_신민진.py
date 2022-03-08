import sys
input = sys.stdin.readline

S, E, Q = map(str, input().split())

S = int("".join(S.split(':')))
E = int("".join(E.split(':')))
Q = int("".join(Q.split(':')))

check = set()
cnt = 0

while True:
    try:
        # 입력이 들어올 경우 실행
        time, name = input().split()
        time = int("".join(time.split(':')))

        if time <= S:
            check.add(name)

        if E <= time <= Q:
            if name in check:
                cnt += 1
                # 채팅 여러번 칠 경우 대비
                check.remove(name)
    except:
        break

print(cnt)