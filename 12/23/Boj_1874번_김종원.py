# 1874번 스택 수열
'''
    n1 : 1부터 n까지 순서대로 수를 담는 리스트
    n2 : n1으로 부터 push 되는 수를 담는 리스트
    answers : 정답이라는 수열에 대한 리스트
    Flag : 수열이 안되는 경우 NO를 표현하기 위해 사용함 (True/False)
    texts : push와 pop을 표현하는 기호 + -를 담기 위한 리스트
'''
n = int(input())
n1, n2, answers = [],[],[]
Flag ,texts = True,[]

## 입력 받는 부분
for i in range(n):
    num = int(input())
    answers.append(num)
    n1.append(i+1)

# 정답이라는 수열 리스트 정보가 empty가 될때까지 반복한다.
while answers:
    answer = answers.pop(0) # 왼쪽 수열 값부터 뽑아낸다. ex) answer = 4 3 6 ... 이라면 숫자 4를 뽑아낸다.
    """
        1부터 n까지 순서대로 입력된 리스트에서 정답값(4)보다 작으면 n2로 push한다. 정답값과 n1에서 뽑은 x가 같다면 push와 pop을 동시에 한다.
        만약 x가 answer보다 크다면 즉, x > answer 보다 크다면 
        정답값이 현재 n1 리스트 안에 없다고 보고 뽑았던 x 값을 n1에 다시 입력하고 반복문을 빠져나간다.
    """
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
    """
        push가 되어 n2 리스트에 담긴 배열 안에서 정답값이 있는지 찾는다.
        정답값이 있다면 pop
        정답값이 n2에서 뽑은 x2값보다 작다면 No의 경우라서 Flag =False로 바꾸고 break를 한다.
        ex) n2 = 3 4 -> x2 = 4 answer = 3 >> x2 > answer인 경우 4 > 3 수열이 될수 없다.
        x2가 answer보다 작다면 n2에 x2를 다시 넣고 n1 배열에서 정답을 찾는다.
    """
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
        

