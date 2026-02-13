#신나는 함수 실행

import sys
input = sys.stdin.readline

w = [[[0] * 21 for _ in range(21)] for _ in range(21)]

for i in range(21):
    for j in range(21):
        for k in range(21):
            if i <= 0 or j <= 0 or k <= 0:
                w[i][j][k] = 1
            elif i < j < k:
                w[i][j][k] = w[i][j][k - 1] + w[i][j - 1][k - 1] - w[i][j - 1][k]
            else:
                w[i][j][k] = w[i-1][j][k] + w[i-1][j-1][k] + w[i-1][j][k-1] - w[i-1][j-1][k-1]


a = b = c = 0
while True:

    a, b, c = map(int, input().split())

    if a == b == c == -1:
        break

    if a <= 0 or b <= 0 or c <= 0:
        print(f'w({a}, {b}, {c}) = 1')
    elif a > 20 or b > 20 or c > 20:
        print(f'w({a}, {b}, {c}) = {w[20][20][20]}')
    else:
        print(f'w({a}, {b}, {c}) = {w[a][b][c]}')