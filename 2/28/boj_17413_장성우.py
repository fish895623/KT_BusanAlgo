"""
https://www.acmicpc.net/problem/17413

1. 소문자, 숫자, 공백, 특수문자로 이루어져있다.
2. 문자열의 시작과 끝은 공백이 아니다.
3. < > 문자열에 있는 경우 번갈아가며 등장 < 먼저 등장

< 시작해서 > 끝나는 길이가 3이상인 부분 문자열 <> 사이에는 알파벳 소문자와 공백만 있다.
단어는 알파벳소문자와 숫자로 이루어진 부분 무나졍ㄹ, 연속하는 두 단어는 공백 하나로 구분


1. <이 들어오면 >이 들어오기전까지 패스


100,000 이기때문에 for문으로 충분히 가능
"""


data = ""  # 데이터 저장
tag = False  # 현재 태그 상태인지 확인

for d in input():
    if tag:  # 현재 태그안인가?
        if d == ">":  # 태그가 끝나는지 확인
            data += d
            print(data, end = "")  # 태그 뒤는 그대로 데이터를 보내준다.
            
            data = ""
            tag = False    # 태그 값 초기화
        else:
            data += d

    else:   # 태그 안이 아닌 경우?
        if d == "<": # 태그로 들어간다.
            if len(data) != 0:  # 이전가지 있는 데이터가 있다면 출력
                print(data[::-1], end = "")
                data = ""
            data += (d)
            tag = True

        elif d == " ": # 공백이 오면 데이터 역순으로 출력
            print(data[::-1], end = " ")
            data = ""

        else:
            data += d

if len(data): # 마지막으로 남은 데이터 출력
    print(data[::-1], end = " ")
