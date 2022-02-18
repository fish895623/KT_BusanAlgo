import math

def solution(fees, records):
    answer = []
    dic = {}
    final_time = 23 * 60 + 59

    for r in records:
        time, car, check = r.split(' ')
        hour, minute = time.split(':')
        time = int(hour) * 60 + int(minute)

        if check == 'IN':
            if car not in dic:
                dic[car] = [time, 0]
            else:
                dic[car] = [time, dic[car][1]]
        else:
            dic[car] = [-1, dic[car][1] + time - dic[car][0]]

    cars = sorted(dic.keys())

    for i in cars:
        minutes = dic[i][1]

        # 출차기록 없을 때
        if dic[i][0] != -1:
            minutes = minutes + final_time - dic[i][0]

        answer.append(fees[1] + math.ceil(max(0, minutes - fees[0]) / fees[2]) * fees[3])

    return answer