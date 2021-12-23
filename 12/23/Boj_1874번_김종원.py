# 1874번 스택 수열

n = int(input())
n1, n2, answers = [],[],[]
Flag ,texts = True,[]

for i in range(n):
    num = int(input())
    answers.append(num)
    n1.append(i+1)

while answers:
    answer = answers.pop(0)
    while n1:
        x = n1.pop(0)
        if x <= answer:
            # print("push")
            texts.append("+")
            if x == answer:
                # print("pop")
                texts.append("-")
                break
            else:
                n2.append(x)
        else:
            n1.insert(0,x)
            break
    if n2:
        x2 = n2.pop()
        if x2 == answer:
            texts.append("-")
        elif x2 > answer:
            Flag = False
            break
        else:
            n2.append(x2)
if not(Flag):
    print("NO")
else:
    for t in texts:
        print(t)
        

