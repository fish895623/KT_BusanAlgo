S = "quqacukqauackck"
# S = "quackquackquackquackquackquackquackquackquackquack"
# S = "qqqqqqqqqquuuuuuuuuuaaaaaaaaaacccccccccckkkkkkkkkk"
S = "quackqauckquack"
S = "quqaquuacakcqckkuaquckqauckack"
# S = "kcauq"

## 오리문제는 quack 순으로 문자열을 탐색을 진행하는데,
## 찾아야하는 문자(findStr)과 현재 문자열이 같고 이전에 방문(visited)한적이 없다면
### 방문 인덱스에 0에서 1로 수정하고 찾아야했던 문자열을 다시 text 리스트에 append 함으로써 순회하면서 탐색이 가능하게 하였다.
### 처음 q 문자(findStr)을 탐색할때, text 리스트 원소에는 [u,a,c,k]가 존재하고 S 문자열에서 순차적으로 q문자열을 찾았을때 방문하지 않았다면
### 방문(visited) 변수 인덱스에 방문했다고 1로 수정하고 text 리스트 원소에 q를 append 함으로써 [u,a,c,k,q]가 된다. 그 후 findStr 값을 u로 업데이트 시키면서
### 순차적으로 탐색을 한다. 그러면서 searchingCount를 이용해 탐색 횟수를 카운트를 해주면서 quack의 문자열 길이 5로 나눔으로써 나머지가 0으로 떨어지지 않는다면
### quack라는 문자열이 전부 탐색이 되지 않은 경우이기에 -1을 리턴한다.

import sys

S = list(sys.stdin.readline().rstrip())

count = 0
flag = True
text = ['q','u','a','c','k']
if len(S) % 5 != 0 or len(S) == 0:
    print(-1)
else:
    while len(S) != 0:
        midx,j,searchingCount = 0,0,0
        findStr = text[j]
        if S[midx] != 'q':
            flag = False
            break
        else:
            while midx !=len(S):
                if (findStr == S[midx]):
                    S.pop(midx)
                    midx -=1
                    j  = (j+1) % 5
                    findStr = text[j]
                    searchingCount +=1
                midx +=1
            if searchingCount % 5 !=0 or len(S) %5 !=0 or findStr != 'q' or midx %5 !=0:
                flag = False
                break
            count +=1
    if flag:
        print(count)
    else:
        print(-1)