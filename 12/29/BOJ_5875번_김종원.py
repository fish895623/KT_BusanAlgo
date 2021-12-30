s = "()(())))"
s = list(s)

left_cnt, right_cnt = 0, 0
cnt = 0

s= []
l_c, r_c = 0,0
for i in range(len(s)):
    if s[i] =="(" and r_c ==0:
        l_c = -1
    elif s[i] == ")" and l_c ==1:
        r_c = +1
    elif s[i] =="(" and r_c >0:
        l_c = l_c -1
    elif s[i] ==")" and 
        pass

    cnt+=1
    