# 가장 많이 팔린 책의 제목을 칠한에 써놓는다.
import sys

n = int(sys.stdin.readline().strip())
book_info = {}

max_val = 0 
max_book_name = ""

for _ in range(n):
    book_name = sys.stdin.readline().strip()
    if book_name not in book_info:
        book_info[book_name] = 1
    else:
        book_info[book_name] += 1

    if book_info[book_name] > max_val:
        max_book_name = book_name
        max_val = book_info[book_name]
    elif book_info[book_name] == max_val:
        if book_name < max_book_name:
            max_book_name = book_name

print(max_book_name)