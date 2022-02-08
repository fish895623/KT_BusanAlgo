"""
https://www.acmicpc.net/problem/20210

숫자 > 문자열

알파벳 A a > B b ...

숫자 - 숫자
-> 십진법으로 작은 숫자가 먼저

같은 값을 가지는 숫자열의 경우 따라붙는 0의 개수가 적은것이 앞에 옴 => 아 00012 0012 -> 0012 > 00012이다.

N이 100,000단위다보니 계속 반복적으로 도는것은 안될것같다. 삽입정렬?로 바로바로 진행하도록하면

정렬은 삽입정렬으로 할려했는데 복잡도가 이미 최악 n^2니까 ... 1초안 불가능
시간초과 겁나 걸릴꺼같은데
일단 나누는것 부터 진행해보자.

도저히 풀 수 없는 문제였다. 블로그 참고해서 문제를 풀자.

"""



import re
from functools import cmp_to_key

t = int(input())
# 나뉘어진 데이터가 저장되는 위치
data = []

for _ in range(t):
    
    d = input()

    # 데이터에서 문자열과 숫자를 분리해서 저장
    temp = re.findall("[a-zA-Z]|\d+", d)

    # 데이터에 원래 데이터와 나뉘어진 값 각각 저장
    data.append([d, temp])

# 알파벳 유니코드로 하면 순서가 제대로 안나오므로 인덱스 가져오기 위한 데이터 생성
alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

# 정렬 사용자 함수
def comp(first,second):

    for i in range(min(len(first[1]), len(second[1]))):
        
        # 숫자 > 문자열이므로 first가 왼쪽에 가야한다.
        if first[1][i].isdigit() and second[1][i].isalpha():
            return -1
        
        # 문자열 < 숫자이므로 second가 왼쪽으로 가야한다.
        elif first[1][i].isalpha() and second[1][i].isdigit():
            return 1

        # 숫자 - 숫자 비교는 작은 숫자가 왼쪽이나 같은 경우 0의 갯수가 작은것이 왼쪽으로 간다.
        elif first[1][i].isdigit() and second[1][i].isdigit():
            
            # 숫자 비교
            if int(first[1][i]) == int(second[1][i]):

                # 같으면 패스
                if len(first[1][i]) == len(second[1][i]):
                    continue
                    
                # first의 0의 개수가 많으면 양수 second의 0의 개수가 많으면 음수가 리턴된다.
                return len(first[1][i]) - len(second[1][i])
            
            else:
                # first가 크면 양수 second가 크면 음수가 온다.
                return int(first[1][i]) - int(second[1][i])
        
        # 문자열 - 문자열 비교이이다.
        else:
            # 같으면 패스
            if first[1][i] == second[1][i]:
                continue
            else:
                # 다르면 alphabet의 인덱스를 비교하여 양수와 음수를 반환 해준다.
                return alphabet.index(first[1][i]) - alphabet.index(second[1][i])        

    # 들어오는 데이터에서 min값까지 다 같은 상태이고 다른 데이터가 큰 경우 first가 크면 양수 second가 크면 음수를 주어진다.
    return len(first[1]) - len(second[1])

answer = sorted(data, key = cmp_to_key(comp))
for i in answer:
    print(i[0])