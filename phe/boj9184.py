#1로 만들기

import sys
input = sys.stdin.readline

N = int(input())
calculation = [0] * (N + 1)

for n in range(2, N + 1):

    if n % 6 == 0:
        calculation[n] = min(calculation[n // 3], calculation[n // 2], calculation[n - 1]) + 1
    elif n % 3 == 0:
        calculation[n] = min(calculation[n // 3], calculation[n - 1]) + 1
    elif n % 2 == 0:
        calculation[n] = min(calculation[n // 2], calculation[n - 1]) + 1
    else:
        calculation[n] = calculation[n - 1] + 1

print(calculation[N])