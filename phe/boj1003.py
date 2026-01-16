#피보나치함수
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    if N == 0:
        print('1 0')
        continue

    elif N == 1:
        print('0 1')
        continue

    cnt0 = [0] * (N+1)
    cnt1 = [0] * (N+1)

    cnt0[0] = 1
    cnt1[1] = 1

    for n in range(2, N + 1):
        cnt0[n] = cnt0[n-1] + cnt0[n-2]
        cnt1[n] = cnt1[n-1] + cnt1[n-2]

    print(cnt0[N], cnt1[N])