while True:
    try:
        import sys
        input = sys.stdin.readline
        s,t = list(input().split())

        from collections import deque
        s = deque(s)
        for t1 in t:
            if len(s) == 0:
                break
            if t1 == s[0]:
                s.popleft()
        if s:
            print('No')
        else:
            print('Yes')
            
    except:
        break
    
    
'''
위에꺼는 개선된 코드, 이건 원래 내 코드
while True:
    try:
    import sys
    input = sys.stdin.readline
    s,t = list(input().split())

    from collections import deque
    t = deque(t)
    array = []
    result = 0
    for s1 in s:
        while len(t) != 0:
            if s1 == t.popleft():
                array.append(s1)
                break
        if len(s) == len(array):
            print('Yes')
            result = 1
            break

    if result == 0:
        print('No')
except:
    break
'''