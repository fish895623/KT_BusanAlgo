# 1,2,3 더하기
# dfs

def dfs(num, now_sum, arr):
    global cnt
    if now_sum == num:
        cnt += 1
        if cnt == k:
            print("".join(arr)[:-1])
            exit(0)
            
    if now_sum > num:
        return   
        
    for i in range(1,4):
        arr.append(f"{i}+")
        dfs(num, now_sum+i, arr)
        arr.pop()

n, k = map(int,input().split())
cnt = 0
dfs(n,0,[])
print(-1)