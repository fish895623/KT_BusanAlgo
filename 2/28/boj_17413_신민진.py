words = list(input())

i = 0
start = 0

while i < len(words):
    # 태그안
    if words[i] == '<':
        i += 1
        while words[i] != '>':
            i += 1
        i += 1

    # 태그밖 영문자, 숫자
    elif words[i].isalnum():
        start = i
        while i < len(words) and words[i].isalnum():
            i += 1
        tmp = words[start:i]
        tmp.reverse()
        words[start:i] = tmp
        
    # 태그밖 공백
    else:
        i += 1

print("".join(words))
