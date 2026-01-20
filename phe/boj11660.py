#구간 합 구하기 5

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
cumulative_sum = [[] for _ in range(N+1)]

for i in range(N+1):
    current_sum = 0
    for j in range(N+1):
        current_sum += arr[i][j]
        cumulative_sum[i].append(current_sum)

for _ in range(M):
    r1, c1, r2, c2 = map(int, input().split())
    sum = 0
    for i in range(r1, r2+1):
        sum += cumulative_sum[i][c2] - cumulative_sum[i][c1-1]

    print(sum)