"""
https://www.acmicpc.net/problem/3029

datetime 쓰고싶은데 기억이 안난다.
"""

first = input()
second = input()

def trans_second(time):
    hour = int(time[0:2])
    minute = int(time[3:5])
    second = int(time[6:8])

    return hour * 3600 + minute * 60 + second

def second_trans(time):
    hour = str(time // 3600)
    time %= 3600
    minute = str(time // 60)
    time %= 60
    second = str(time)

    return print(hour.zfill(2) + ":" + minute.zfill(2) + ":" + second.zfill(2))

first_second = trans_second(first)
second_second = trans_second(second)

if first_second == second_second:
    print("24:00:00")
elif first_second > second_second:
    time = 86400 - first_second + second_second
    second_trans(time)
else:
    time = second_second - first_second
    second_trans(time)

