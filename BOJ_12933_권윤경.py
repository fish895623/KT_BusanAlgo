import sys
input = sys.stdin.readline().rstrip
array = input()
arr = list("quack")

visited = [False] * (len(array))
result = 0
for a in range(len(array)):
    i = a
    j = 0
    first = False
    while i != (len(array)):
        if array[i] == arr[j] and visited[i] == False:
            visited[i] = True
            if array[i] == 'k' and first == False:
                first = True
                result += 1    
            if j == len(arr)-1:
                j = 0
            else:
                j += 1
        else:
            i += 1

if all(visited) == True and (len(array)%5 == 0) and result != 0:
    print(result)

else:
    print(-1)