"""
https://www.acmicpc.net/problem/17609

앞 뒤가 같은 문자열 -> 회문

하나를 없애서 회문이 되면 유사회문

회문 : 0
유사회문 : 1
그 외 : 2

유사회문을 구하는게 더 어렵다.

아 여기서 잘못했네 홀수여도 바로 회문이 될 수있다.
`
짝수인경우 팰린드롬을 그대로 구하면되고

홀수인경우
어디선가 틀리는 경우가 생긴다,

이 경우 앞선 s를 빼야한다.
두가지 경우를 다 진행하자.
1) 처음 틀린경우에서 s를 빼고 진행한경우
2) 처음 틀린 경우에서 u를 빼고 진행한경우
둘 중 하나라도 회문이 나오면 유사회문이 된다.

ssummus
s   s
s   u
u   s
s  


summuus
s   s
u   u
m   u
m   

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
    
    # 아니면서 홀수개의 데이터이면 하나를 빼고 구할 수 있다.
    else:

        data_start = list(data)
        data_end = list(data)

        for i in range( math.ceil(int(len(data)/2))  ):
        # 하나씩 비교하면서 진행하면서 틀린 경우 앞선 데이터를 뺄것인지 뒤의 데이터를 뺄 것인지 진행
            if data[i] != data[-(i +1)]:
                data_start.pop(i)
                data_end.pop(-(i+1))
                # 앞 선 데이터 빼고 진행
                if data_start == data_start[::-1]:
                    print("1")
                    break

                if data_end == data_end[::-1]:
                    print("1")
                    break
                # 여기까지 온 경우 둘다 아니므로 일반문자를 출력해주자.
                print("2")
                break





                


