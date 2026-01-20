#이건 꼭 풀어야 해!

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)
cumulative_sum = [0]
current_sum = 0
for num in nums:
    current_sum += num
    cumulative_sum.append(current_sum)

for _ in range(Q):
    L, R = map(int, input().split())
    print(cumulative_sum[R] - cumulative_sum[L - 1])