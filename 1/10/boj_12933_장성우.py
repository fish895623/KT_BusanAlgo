"""
https://www.acmicpc.net/problem/12933

"""

import sys


#"quack"

duck_sound = [0,0,0,0,0]

data = input()
cnt = 0
flag = True
test = True

for d in data:
    if d == "q":
        duck_sound[0] += 1
        if flag:
            cnt += 1
        else:
            flag = True
    elif d == "u":
        
        duck_sound[1] += 1
        if duck_sound[0] < duck_sound[1]:
            test = False
            break
    elif d == "a":
        duck_sound[2] += 1
        if duck_sound[1] < duck_sound[2]:
            test = False
            break
    elif d == "c":
        duck_sound[3] += 1
        if duck_sound[2] < duck_sound[3]:
            test = False
            break
    elif d == "k":
        duck_sound[4] += 1
        if duck_sound[3] < duck_sound[4]:
            test = False
            break
        for i in range(5):
            duck_sound[i] -= 1
            flag = False
    else:
        test = False
        break

if sum(duck_sound) != 0:
    test = False

if test:
    print(cnt)
else:
    print('-1')
    