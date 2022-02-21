"""
https://www.acmicpc.net/problem/17609

앞 뒤가 같은 문자열 -> 회문

하나를 없애서 회문이 되면 유사회문

회문 : 0
유사회문 : 1
그 외 : 2

"""
# T의 크기가 30개 미만이므로 readline이랑 별 차이가 없을것이다.

import math

# # 입력되는 값
t = int(input())

for _ in range(t):
    data = input()

    # 팰린드롬인지 확인
    if data == data[::-1]:
        print("0")
    
    else:
        # data_start = 처음 데이터에서 하나를 뺄 데이터
        # data_end = 마지막 데이터에서 하나를 뺄 데이터
        data_start = list(data)
        data_end = list(data)

        # 홀수인 경우 올림으로 받아와서 진행해야 하나를 빼먹지 않는다.
        for i in range( math.ceil(int(len(data)/2))  ):
            
            # 하나씩 비교하면서 진행하면서 틀린 경우 앞선 데이터를 뺄것인지 뒤의 데이터를 뺄 것인지 진행
            if data[i] != data[-(i +1)]:
                data_start.pop(i)
                data_end.pop(-(i+1))

                # 앞 선 데이터 빼고 진행
                if data_start == data_start[::-1]:
                    print("1")
                    break

                # 뒤의 데이터를 빼고 진행
                if data_end == data_end[::-1]:
                    print("1")
                    break

                # 여기까지 온 경우 둘다 아니므로 일반문자를 출력해주자.
                print("2")
                break





                


