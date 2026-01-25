#구간 합 구하기 4
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

nums = list(map(int, input().split()))
cumulative_sum = [0]
current_sum = 0

for num in nums:
    current_sum += num
    cumulative_sum.append(current_sum)

for _ in range(M):
    i, j = map(int, input().split())

    print(cumulative_sum[j] - cumulative_sum[i-1])