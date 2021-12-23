# 스택 수열
# n = 8
# 4 3 6 8 7 5 2 1

# 1 2  5 6 7 8
# ++++--++-++--
# [1 2 5 ]

# 1 2 3 4 5 6 7 8
# 4

# 4 3 6
n = int(input())
findnums = []
numbox = []
numboxs = []
for i in range(n):
    num = int(input())
    findnums.append(num)
    numbox.append(i+1)
    
findnum = findnums.pop(0)
while findnums:
    while numbox:
        n = numbox.pop(0)
        if n < findnum:
            numboxs.append(n)
            print("push")
        elif n == findnum:
            numboxs.append(n)
            print("push")
            break
        else:
            print("No")
    while True:
        if numboxs[-1] == findnum:
            numboxs.pop()
            print("pop")
            if len(findnums) ==0:
                break
            else:
                findnum = findnums.pop(0)
        elif numboxs[-1] != findnum:
            break
        elif len(numboxs) ==0:
            break
