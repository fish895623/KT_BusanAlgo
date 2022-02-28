
import sys

s = sys.stdin.readline().rstrip()

blank = []  # < > 태그 정보를 담는 리스트
words = []  # 태그 정보가 아닌 단어를 담는 리스트

flag = True  # < > 태그안에 포함되는 단어인지 아닌지 판별하는 flag 변수
flag1 = True # < > 태그가 아니면서 " " 빈 문자열로 단어가 구분되어 나타낸것인지 구분하기 위한 flag 변수

word = "" # 태그나 단어 정보를 기입하는 변수

# 단어와 태그 정보를 쪼개어 blank 와 words 변수에 저장한다.
for i in range(len(s)):
    if s[i] =="<":
        if len(word) !=0:
            words.append((i,word))
            word=""
        flag = False
    elif s[i] == ">":
        word +=s[i]
        flag = True
        blank.append((i,word))
        word=""
        continue

    if not(flag):        
        word +=s[i]
    else:
        if s[i] != " ":
            flag1 = True
        else:
            flag1 = False
            word +=s[i]
            words.append((i,word))
            word = ""

        if flag1:
            word +=s[i]

# 맨 마지막 단어에 " " 스페이스 없이 끝난 경우 word에 빈문자열 아니면 해당 단어를 단어 리스트에 추가.
if len(word) !=0:
    words.append((i,word))

# 합하고 정렬하여 입력된 순서 정보를 맞춘다.
total = blank + words
total.sort(key=lambda x: x[0])

# 출력
for j in range(len(total)):
    # 태그이면 그대로 출력
    if total[j] in blank:
        print(total[j][1] ,end ="")
    # 태그가 아니면 단어이므로 단어는 역으로 출력
    else:
        if total[j][1][-1] == " ":  # 구분된 문자이면 출력시 " " 문자열이 필요하기에 해당 부분만 따로 작성하였다.
            for k in range(len(total[j][1])-2,-1,-1):
                print(total[j][1][k],end ="")
            print(end =" ")
        else:
            for k in range(len(total[j][1])-1,-1,-1):
                print(total[j][1][k],end ="")