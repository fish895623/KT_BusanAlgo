"""
https://www.acmicpc.net/problem/2503

1. 1 ~ 9까지 모든 조합을 리스트에 저장
2. 모든 조합을 돌면서 입력된 값이랑 strike와 ball이 같은것만 따로 리스트에 저장
3. 따로 저장된것을 가지고 입려 된 다른 데이터 비교
4. 마지막에 남은 데이터의 길이 출력

사용된 변수
predict_list : 조합 리스트 저장
data : 입력된 값

"""
import itertools


n = int(input())


# 1 ~ 9까지 모든 조합 list에 저장

predict_list = list(itertools.permutations(['1','2','3','4','5','6','7','8','9'], 3))



# 숫자 야구 모든 경우의 수 확인, 이전 경우의수에서 살아남은것만 다시 저장해서 돌리기
for _ in range(n):

    data, strike, ball = map(int, input().split())

    # result = 남은 데이터 저장하기 위한 리스트
    result = []

    # predict_list : 조합에서 살아남은 리스트
    for pre_data in predict_list:

        # pre_ball : 현재 ball count
        # pre_strike : 현재 strike count
        pre_ball = 0
        pre_strike = 0

        # 입력된 값이 int형이므로 str로 바꾸어서 하나씩 비교
        for data_i in str(data):

            # 입력된 값이 조합 안에 있다면 해당 조합에 ball count 1증가
            if data_i in pre_data:
                pre_ball += 1

        # 만약 위치까지 같다면 strike 증가, ball 감소
        for i in range(3):
            if str(data)[i] == pre_data[i]:
                pre_ball -= 1
                pre_strike += 1

        # strike 숫자와 ball의 숫자가 원하는 값가 같다면 result에 저장하고 남은 조합 반복
        if pre_strike == strike and pre_ball == ball:
            result.append(pre_data)

    # 이전 숫자야구에서 맞는 데이터만 다시 조합식에 저장
    predict_list = result
    
# 결과의 길이만 출력
print(len(result))