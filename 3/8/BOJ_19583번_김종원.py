S = "22:00" # 개강 총회 시작 시간
E = "23:00" # 개강 총회 끝난 시간
Q = "23:30" # 개강 스트리밍이 끝난 시간

member_list = [
    "21:30 malkoring",
    "21:33 tolelom",
    "21:34 minjae705",
    "21:35 hhan14",
    "21:36 dicohy27",
    "21:40 906bc",
    "23:00 906bc",
    "23:01 tolelom",
    "23:10 minjae705",
    "23:11 hhan14",
    "23:20 dicohy27",
]

# S = "06:00" 
# E = "12:00" 
# Q = "18:00"
# member_list= [
#             "06:00 shinyo17"
#             ,"06:00 kimchist"
#             ,"06:00 swoon"
#             ,"06:00 kheee512"
#             ,"06:00 Green55"
#             ,"09:00 kimchist"
#             ,"11:59 shinyo17"
#             ,"12:00 kimchist"
#             ,"17:59 swoon"
#             ,"17:59 swoon"
#             ,"18:00 kheee512"
#             ,"18:01 swoon"
#             ,"18:01 Green55"
#             ,"18:01 kheee512"
#             ,"18:01 swoon"
#             ,"18:21 jinius36"
#             ,"18:40 jeongyun1206"
# ]

import sys

S,E,Q = sys.stdin.readline().strip().split()


member_list = []

while True:
    note = sys.stdin.readline().strip()
    if len(note) == 0:
        break
    member_list.append(note)


S_h, S_m = list(map(int, S.split(":")))
E_h, E_m = list(map(int, E.split(":")))
Q_h, Q_m = list(map(int, Q.split(":")))
S = S_h*60 + S_m
E = E_h*60 + E_m
Q = Q_h*60 + Q_m

in_member = set()
out_member = set()

for me in member_list:
    time_str, name = me.split(" ")
    hour, minute = list(map(int,time_str.split(":")))
    time = hour * 60 + minute
    if time > Q:
        continue
    if S >= time:
        in_member.add(name)
    elif E <= time <= Q:
        out_member.add(name)        

print(len(in_member & out_member))