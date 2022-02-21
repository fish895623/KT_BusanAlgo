l, r = input().split()
arr = input()

sl = {
    'q' : (0,0), 'w' : (0,1), 'e' : (0,2), 'r' : (0,3), 't' : (0,4), 'a' : (1,0), 's' : (1,1), 'd' : (1,2), 'f' : (1,3), 'g' : (1,4), 'z' : (2,0), 'x' : (2,1), 'c' : (2,2), 'v' : (2,3)
}
sr = {
    'y' : (0,5),'u' : (0,6),'i' : (0,7),'o' : (0,8),'p' : (0,9),'h' : (1,5),'j' : (1,6),'k' : (1,7),'l' : (1,8),'b' : (2,4),'n' : (2,5),'m' : (2,6)
}

lstart = (sl[l][0], sl[l][1])
rstart = (sr[r][0], sr[r][1])
result = 0

for i in arr:
    result += 1
    if i in sl:
        result += abs(lstart[0]- sl[i][0]) + abs(lstart[1]- sl[i][1])
        lstart = sl[i]
    else:
        result += + abs(rstart[0]- sr[i][0]) + abs(rstart[1]- sr[i][1]) 
        rstart = sr[i]
print(result)