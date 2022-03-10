from sys import stdin


def dfs(idx, sum_num, check):
    global cnt
    # n보다 큰 경우 확인할 필요 없음.
    if sum_num > n:
        return

    if n == sum_num:
        # k번째 수를 찾기 위함
        cnt += 1
        if cnt == k:
            # 숫자+숫자+숫자+로 기록하므로, 마지막을 제거하고 출력.
            print(''.join(check)[:-1])
            exit(0)

    for i in range(1, 4):
        check.append(str(i) + '+')
        dfs(idx + 1, sum_num + i, check)
        check.pop()


if __name__ == '__main__':
    cnt = 0
    n, k = map(int, stdin.readline().split())
    dfs(0, 0, [])
    print(-1)