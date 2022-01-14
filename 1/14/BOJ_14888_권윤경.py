import sys
# input = sys.stdin.readline
# n = int(input())
# array = list(map(int,input().split()))
# calc = list(map(int,input().split()))
maximum = -sys.maxsize
minimum = sys.maxsize

n=6
array = [1, 2, 3, 4, 5, 6]
calc = [2, 1, 1, 1]

def calc_array(num, idx, plus, minus, multi, divi):
    global maximum, minimum, n
    if idx == n :
        maximum = max(maximum, num)
        minimum = min(minimum, num)
        return
        
    else:
        if plus > 0:
            calc_array(num + array[idx], idx + 1, plus -1, minus, multi, divi)
        if minus > 0:
            calc_array(num - array[idx], idx + 1, plus, minus-1, multi, divi)
        if multi > 0:
            calc_array(num * array[idx], idx + 1, plus, minus, multi-1, divi)
        if divi > 0:
            calc_array(int(num / array[idx]), idx + 1, plus, minus, multi, divi-1)


calc_array(array[0],1,calc[0],calc[1],calc[2],calc[3])
print(maximum,minimum)
