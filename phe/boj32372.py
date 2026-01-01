#마법의 나침반

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
treasure = [[0] * (N + 1) for _ in range(N+1)]
is_first = True

for _ in range(M):

    x, y, direction = map(int, input().split())

    for i in range(1, N + 1):
        for j in range(1, N + 1):

            if not is_first and not treasure[i][j]:
                continue

            if direction == 1:
                if i < x and j == y:
                    treasure[i][j] += 1

            if direction == 2:
                if i < x and j > y:
                    treasure[i][j] += 1

            if direction == 3:
                if i == x and j > y:
                    treasure[i][j] += 1

            if direction == 4:
                if i > x and j > y:
                    treasure[i][j] += 1

            if direction == 5:
                if i > x and j == y:
                    treasure[i][j] += 1

            if direction == 6:
                if i > x and j < y:
                    treasure[i][j] += 1

            if direction == 7:
                if i == x and j < y:
                    treasure[i][j] += 1

            if direction == 8:
                if i < x and j < y:
                    treasure[i][j] += 1

    is_first = False


def func():
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if treasure[i][j] == M:
                print(i, j)
                return

func()