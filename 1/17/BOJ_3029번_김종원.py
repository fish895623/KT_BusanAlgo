now = input()
end = input()
if now == end:
    print("24:00:00")
else:
    now_s = int(now[-2:])
    end_s = int(end[-2:])

    now_m = int(now[3:5])
    end_m = int(end[3:5])

    now_h = int(now[:2])
    end_h = int(end[:2])

    m_s, m_m = 0,0
    if end_h - now_h < 0:
        fire_h = (24 - now_h) + end_h
    else:
        fire_h = end_h - now_h

    if end_m - now_m < 0:
        fire_m = (60 - now_m) + end_m
        fire_h -=1
    else:
        fire_m = end_m - now_m

    if end_s - now_s < 0:
        fire_s = (60 - now_s) + (end_s)
        fire_m -=1
    else:
        fire_s = end_s - now_s
    if fire_h <0:
        fire_h = 0
    if fire_m <0:
        fire_m = 0
    if fire_s <0:
        fire_s = 1

    if fire_h <10:
        fire_h = "0"+str(fire_h)
    if fire_m <10:
        fire_m = "0"+str(fire_m) 
    if fire_s <10:
        fire_s = "0"+str(fire_s) 
        
    print(f"{fire_h}:{fire_m}:{fire_s}")