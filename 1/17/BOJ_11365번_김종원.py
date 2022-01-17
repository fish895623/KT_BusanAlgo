S =[]
while True:
    s = input()
    if s == "END":
        break
    S.append(s)

for i in range(len(S)):
    for j in range(len(S[i])-1,-1,-1):
        print(S[i][j],end="")
    print()