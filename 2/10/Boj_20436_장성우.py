"""

https://www.acmicpc.net/problem/20436



누르는 시간 1
움지이는 것

문제좀 제대로 읽자아아아아아아아


"""


# 문자의 x, y 위치를 반환해준다.
def find_loc(word):
    keyboard = [
        ['q','w','e','r','t','y','u','i','o','p'],
        ['a','s','d','f','g','h','j','k','l'],
        ['z','x','c','v','b','n','m']
    ]

    for i, key in enumerate(keyboard):
        if word in key:
            y = i
            x = key.index(word)
            return x, y


sl, sr = map(str, input().split())
data = input()
result = 0

# 모음 저장
consonant = "qwertasdfgzxcv"

for d in data:
    
    # 이미 왼손이나 오른손이 그 위치에 있는경우
    if sl == d or sr == d:
        result += 1
        
    
    # 아닌 경우 각각의 위치 별 x, y위치를 입력받자.
    else:

        slx, sly = find_loc(sl)
        srx, sry = find_loc(sr)
        dx, dy = find_loc(d)

        # 모음이라면 왼쪽이 이동한다.
        if d in consonant:
            result += abs(slx-dx) + abs(sly-dy) + 1
            sl, slx, sly = d, dx, dy
        # 자음이라면 오른쪽이 이동한다.
        else:
            result += abs(srx-dx) + abs(sry-dy) + 1
            sr, srx, sry = d, dx, dy

print(result)


