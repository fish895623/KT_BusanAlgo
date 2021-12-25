from sys import stdin

if __name__ == '__main__':
    tree = dict()
    cnt = 0
    while True:
        s = stdin.readline().rstrip()

        if not s:
            break

        if s not in tree:
            tree[s] = 1
        else:
            tree[s] += 1

        cnt += 1
    tree = sorted(tree.items())

    [print("{} {:.4f}".format(k, round(v/cnt * 100, 4))) for k, v in tree]
