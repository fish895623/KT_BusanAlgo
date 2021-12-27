from collections import deque

n = int(input())
m = []
for i in range(n):
    m.append(int(input()))
    
array1 = sorted(m)
array2 = deque(m)

# array1 : 오름차순, array2 : 조건
a = [] # 스택
num = 0
result = []

while len(array2) !=0:
    # a가 비어있지 않으며 a의 마지막이 조건 리스트의 0번째와 같으면 pop하고, 조건 리스트의 0번째도 완료 됐으므로 숫자를 뺌
    if len(a) !=0 and a[-1] == array2[0]:
        array2.popleft()
        a.pop()
        result.append('-')
    
    # 위의 조건과 틀리면 스택에 추가하고 다음 비교할 오름차순 리스트 번호(num)에 +1
    else:
        # 조건이 실행 가능한 문제
        try:
            a.append(array1[num])
            num +=1
            result.append('+')
        # 조건이 실행 가능하지 않는 문제
        except:
            result = []
            result.append("NO")
            break;

for result in result:
    print(result)
