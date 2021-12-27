from sys import stdin

tree = {}
cnt = 0

while True:
    name = stdin.readline().strip() # .strip() 안하면 무한루프
    if not name: # 입력이 없을 때까지 반복
        break
    tree.setdefault(name, 0) # 종이름 사전에 저장, 딕셔너리 초기값 0으로 설정.
    tree[name] += 1 # name(key값)에 대해 +1함.
    cnt += 1 # 나무 개체수

for name in sorted(tree.keys()): # key값 정렬
    print('{0} {1:0.4f}'.format(name, tree[name]*100/cnt)) 
    # key 값 정렬 / 비율출력