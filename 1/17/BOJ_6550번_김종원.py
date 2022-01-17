# S가 T의 부분문자열인지 T가 큰것.
s, t = "sequence" ,"subsequence"
s,t = "person" ,"compression"
s,t = "VERDI","vivaVittorioEmanueleReDiItalia"
s, t = "caseDoesMatter", "CaseDoesMatter"

KM = input()
while KM:
    try:
        s,t = KM.split()
        visited = [(0,0)] * (len(s) +1)
        visited[0] = (-1,1)
        flag = True
        num_idx,num_idx_bf = 0,0
        for i in range(len(s)):
            # print("문자 : ",t[num_idx:]," 찾을 문자열 : ",s[i])
            num_idx = t[num_idx:].find(s[i])
            if num_idx == -1:
                flag=False
                break
            num_idx += num_idx_bf
            if visited[i][0] > num_idx:
                flag=False
                break
            visited[i+1] = (num_idx,1)
            num_idx_bf = num_idx
        if flag:
            count =0 
            for j in visited:
                count +=j[1]
            if count ==len(visited):
                print("Yes")
            else:
                print("No")
        else:
            print("No")
        KM = input()
    except:
        break