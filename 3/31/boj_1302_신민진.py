n = int(input())
books = {}

for _ in range(n):
    book = input()
    if books.get(book):
        books[book] += 1
    else:
        books[book] = 1

max_ = max(books.values())

best_seller = []

for book, number in books.items():
    if number == max_:
        best_seller.append(book)

print(sorted(best_seller)[0])