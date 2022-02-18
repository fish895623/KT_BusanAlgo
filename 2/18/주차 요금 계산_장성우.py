"""
https://programmers.co.kr/learn/courses/30/lessons/92341

요금표, 
입차,
출차


만약 출차된 기록이 없으면 23:59에 도착
시 분 -> 분으로 변환

fee에 따라 다르다.
기본 시간 : 180분
기본 요금 : 5000원
단위 시간 : 10분
단위 요금 : 600원

누적이다. 바로바로 계산이 아니다.
잘못 있는 차가 출차되는 경우는 없다.


1. 모든 records의 시간을 분으로, 저장하자.
2. 만약 홀수개면 max값(23:59)과 빼기를 진행하자.
3. 누적 값을 이용해서 값을 구한다.
4. 차량 번호가 작은 순서이므로 차량 번호도 저장이 되어있어야한다.



"""
import math

def time_to_minute(time):

    hour = int(time[0:2])
    minute = int(time[3:5]) + hour * 60

    return minute


def solution(fees, records):
    
    # data : dic으로 데이터를 저장하는 곳
    # car_num : car num이 들어있는지 확인 하는 곳
    data, car_num, answer_result = [], [], []
     
    for recort in records:
        record_time, record_car_num, recort_in_out = recort.split()
        
        # 처음 들어온 차의 번호라면
        if record_car_num not in car_num:
            # 자동차 번호 저장
            car_num.append(record_car_num)

            data.append({
                "car_num" : record_car_num,
                "minute" : [time_to_minute(record_time)],
                "fee" : 0
            })
        # 이미 들어온 경우
        else:
            
            # data에서 car_num의 index를 검색해서 minute안에 데이터를 저장한다.
            data[car_num.index(record_car_num)]["minute"].append(time_to_minute(record_time))


    # 요금 계산
    # basic_time : 기본 시간
    # basic_fee : 기본요금
    # unit_time : 단위 시간
    # unit_fee : 단위 요금

    basic_time, basic_fee, unit_time, unit_fee = fees[0], fees[1], fees[2], fees[3]

    # # 자동차 번호 순서대로 저장
    # car_num.sort()

    # 자동차 갯수만큼 돌면서
    for i in range(len(car_num)):

        # 만약 mintue가 홀수이면 마지막은 max(23:59)값을 뺴주어야한다.
        if len(data[i]["minute"]) % 2 != 0:
            data[i]["minute"].append(time_to_minute("23:59"))
        
        result_minute = 0
        # 누적 시간을 진행한다. 짝수는 빼고 홀수는 더한다.
        for num, t in enumerate(data[i]["minute"]):
            if num % 2 == 0:
                result_minute -= t
            else:
                result_minute += t

        # 계산을 진행한다.
        result_fee = 0

        result_fee += basic_fee
        
        # 계산이 끝난 시간은 없애준다.
        result_minute -= basic_time
        
        # 단위 시간 계산
        if result_minute > 0:
            result_fee += math.ceil(result_minute / unit_time) * unit_fee
        
        data[i]["fee"] = result_fee

        answer_result.append([data[i]["car_num"], result_fee])
    

    answer_result.sort()

    answer = []
    for r in answer_result:
        answer.append(r[1])



    
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))
