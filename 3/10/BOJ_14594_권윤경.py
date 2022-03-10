n = int(input())
m = int(input())
act = [list(map(int,input().split())) for _ in range(m)]

visit = [1] * (n+1)

for x,y in act:
    if x<y:
        for i in range(x+1,y+1):
            visit[i] = 0

print(sum(visit)-1)
