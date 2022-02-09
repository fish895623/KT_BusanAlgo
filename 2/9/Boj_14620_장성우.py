"""
https://www.acmicpc.net/problem/14620

"""

n = int(input())

visited = [[False] * n for i in range(n)]


data = []
for _ in range(n):
    data.append(list(map(int, input().split())))



def flower(x, y, data, visited):
    result = data[x][y] + data[x-1][y] + data[x+1][y] + data[x][y+1] + data[x][y-1]
    visited[x][y] = True
    visited[x-1][y] = True
    visited[x+1][y] = True
    visited[x][y-1] = True
    visited[x][y+1] = True
    return result, visited

def visited_check(x, y, visited):

    if not visited[x][y]:
        if not visited[x-1][y]:
            if not visited[x+1][y]:
                if not visited[x][y-1]:
                    if not visited[x][y+1]:
                        return True
    
    return False


def visited_false(x, y, visited):
    visited[x][y] = False
    visited[x-1][y] = False
    visited[x+1][y] = False
    visited[x][y-1] = False
    visited[x][y+1] = False

    return visited
    



result = 1e9
# x, y는 각각 1, n-1까지만 돌면된다.
first, second, thrid = 0, 0, 0
# 첫번째 좌표
for y1 in range(1, n-1):
    for x1 in range(1, n-1):
        
        if visited_check(x1,y1,visited):
            first, visited = flower(x1, y1, data, visited)
        
        # 두번째 좌표
        for y2 in range(y1, n-1):
            for x2 in range(1, n-1):
                
                if visited_check(x2,y2, visited):
                    second, visited = flower(x2, y2, data, visited)
                else:
                    continue

                # 세번째 좌표
                for y3 in range(y2, n-1):
                    for x3 in range(1, n-1):
                        if visited_check(x3,y3,visited):
                            third, visited = flower(x3, y3, data, visited)
                            result = min(result, first+ second+ third)
                            visited = visited_false(x3, y3, visited)
                        else:
                            continue
                
                visited = visited_false(x2, y2, visited)
        
        visited = visited_false(x1, y1, visited)
print(result)






