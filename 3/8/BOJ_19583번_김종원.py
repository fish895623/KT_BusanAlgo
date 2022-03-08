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