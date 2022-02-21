import copy

row, col = map(int, input().split())
maps = []
for _ in range(row):
    maps.append(list(input()))
result_maps = copy.deepcopy(maps)
xx = [0,1,0,-1]
yy = [1,0,-1,0]

for i1,v1 in enumerate(maps):
    for i2, v2 in enumerate(v1):
        if maps[i1][i2] == '.':
            continue
        cnt = 0
        for x, y in zip(xx,yy): 
            if (0 <= i1+x < row and 0 <= i2+y < col) and maps[i1+x][i2+y] == '.':
                cnt += 1
            elif i1+x < 0 or i1+x >=row or i2+y < 0 or i2+y >=col:
                cnt +=1
        if cnt >= 3:
            result_maps[i1][i2] = '.'
            
min_row = row -1
max_row = 0
min_col = col-1
max_col = 0 
for i in range(row):
    if 'X' in result_maps[i] :
        min_row = min(min_row, i)
        max_row = max(max_row, i)
        for j in range(col):
            if result_maps[i][j] == 'X':
                min_col = min(min_col, j)
                max_col = max(max_col, j)              

for i in range(min_row,max_row+1):
    for j in range(min_col, max_col+1):
        print(result_maps[i][j], end="")
    print()