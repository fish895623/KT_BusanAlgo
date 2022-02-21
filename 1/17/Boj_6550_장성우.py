"""
https://www.acmicpc.net/problem/6550

len = O(1)
list.pop(0) -> O(n)
heapq.leftpop() -> O(1)
list.pop() -> O(1)
"""

import sys
input= sys.stdin.readline

while True:
    data = list(map(str, input().split()))

    if not data:
        break

    a = list(data[0])
    b = list(data[1])

    if len(a) > len(b): 
        print("No")
    elif len(a) == len(b):
        if a == b:
            print("Yes")
        else:
            print("No")
    elif len(a) == 0:
        print("No")
    else:
        first = a.pop()
            
        second = b.pop()
        # 뒤에서부터 확인하자.
        while True:
            if first != second:
                if len(b) == 0:
                    print("No")
                    break
                second = b.pop()
            else:
                if len(a) == 0:
                    print("Yes")
                    break
                first = a.pop()
                second = b.pop()

            



        


