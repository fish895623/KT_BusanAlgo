import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemon = [input().strip() for _ in range(n)]
quiz = [input().strip() for _ in range(m)]

for i in quiz:
    try:
        print(pokemon[int(i)-1])
    except:
        print(pokemon.index(i)+1)