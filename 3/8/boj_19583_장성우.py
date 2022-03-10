"""
https://www.acmicpc.net/problem/19583

1. 채팅기록
2. 끝내고나서 스트리밍 끝날때까지 대화를 해야한다.

00:00 ~ 개강총회 시작하기전 = 대기시간
경계값에 있는 사람들은 뺸다.

출석 : 개강총회 시작전에 대화를 나눈사람

퇴장 : 끝나고 스트리밍 끝나기전까지 대화

"""
import sys
# solution : 몇 명이 끝냇는지 리턴
def solution(start, end, streaming_end, data):

    start_minute, end_minute, streaming_end_minute = change_minute(start), change_minute(end), change_minute(streaming_end)

    
    start_chat, end_chat = [], []
    result = []
    for d in data:
        time, name = d.split()
        if 0 <= change_minute(time) <= start_minute:
            start_chat.append(name)
        
        if end_minute <= change_minute(time) <= streaming_end_minute:
            if name in start_chat:
                result.append(name)

    
    # # start_chat = list(set(start_chat))
    # # end_chat = list(set(end_chat))

    # for i in start_chat:
    #     if i in end_chat:
    #         result.append(i)

    return len(set(result))


import sys
# 시간 => minute    
def change_minute(time):
    hour, minute = time.split(":")
    result_minute =  int(hour) * 60 + int(minute)
    return result_minute

if __name__ == "__main__":
    start, end, streaming_end = map(str, input().split())
    start_minute, end_minute, streaming_end_minute = change_minute(start), change_minute(end), change_minute(streaming_end)

    start_chat, end_chat, result, data = [],[], [], []
    while True:
        
        try:
            time, name = sys.stdin.readline().rstrip().split()
            t = change_minute(time)

            if 0 <= t <= start_minute:
                start_chat.append(name)
            
            elif end_minute <= t <= streaming_end_minute:
                end_chat.append(name)

        except:
            break

    result = set(start_chat) & set(end_chat)
    print(len(result))