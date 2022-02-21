keyboard = ['qwertyuiop','asdfghjkl','zxcvbnm']

# keyboard 자판 행, 열 구하는 함수
def find_loc(word):
    for i in range(3):
        if word in keyboard[i]:
            return i, keyboard[i].index(word)

sl, sr = input().split()
arr = input()
time, distance = len(arr), 0

sl_row, sl_column = find_loc(sl)
sr_row, sr_column = find_loc(sr)

for i in arr:
    row, column = find_loc(i)
    # 자음자판
    if (row == 2 and column <= 3) or (row <= 1 and column <= 4):
        distance += abs(sl_row - row) + abs(sl_column - column)
        sl_row = row
        sl_column = column
    # 모음자판
    else:
        distance += abs(sr_row - row) + abs(sr_column - column)
        sr_row = row
        sr_column = column

time += distance
print(time)