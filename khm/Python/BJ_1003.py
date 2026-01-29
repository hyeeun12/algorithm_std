import sys

# 피보나치 수열을 직접 계산하는 문제 아님..
dp = [(0, 0)] * 41
# dp[0]은 n == 0일때 0과 1의 개수, dp[1]은 n == 1일때 0과 1의 개수
# (a, b) => a는 0의 개수, b는 1의 개수
dp[0] = (1, 0)
dp[1] = (0, 1)

for i in range(2, 41):
    dp[i] = ((dp[i - 1][0] + dp[i - 2][0]), (dp[i - 1][1] + dp[i - 2][1]))

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(*dp[n], sep= ' ')
