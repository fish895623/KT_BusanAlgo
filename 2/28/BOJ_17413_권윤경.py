from collections import deque

s = input()
queue = deque(s)

result = []
arr = []
arr2 = []
while queue:
    num = queue.popleft()
    if num =="<":
        arr.append(num)
    else:
        if len(arr) != 0:
            arr.append(num)
            if num == ">":
                result.append("".join(arr))
                arr = []
        else:
            try:
                if num != " " and queue[0] != "<":
                    arr2.append(num)
                else:
                    if queue[0] == "<":
                        arr2.append(num)
                        result.append("".join(arr2)[::-1])
                        arr2 = []
                    else:
                        result.append("".join(arr2)[::-1]+" ")
                        arr2 = []
            except:
                arr2.append(num)
                result.append("".join(arr2)[::-1])
                arr2 = []

print("".join(result))
    