def solution(n, words):
    words_dict = {}

    before_word = words.pop(0)
    people = 0
    count = 1

    result = []
    words_dict = { before_word : [people,count]}

    flag = False
    while words:
        people +=1
        current_word = words.pop(0)
        if people % n == 0:
            count +=1

        if before_word[-1] != current_word[0]:
            people_ord = (people % n) + 1
            current_count = count
            result.append([people_ord,current_count])
            flag = False
            break
        else:
            if current_word not in words_dict:
                people_ord = (people % n) + 1
                current_count = count
                words_dict[current_word] = [people_ord,current_count]
                flag = True
                before_word = current_word
            else:
                flag= False
                people_ord = (people % n) + 1
                current_count = count
                result.append([people_ord,current_count])
                break
    if flag:
        return [0,0]
    else:
        return result[0]