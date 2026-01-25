#진심 좌우 반복뛰기
import sys
input = sys.stdin.readline

t = int(input())
#ver1. 완전탐색 (하지만 결과는 시간 초과)
# for _ in range(t):
#     n, k= map(int, input().split())
#
#     # 0.15초 -> 1500만번 연산 가능
#     # 완전탐색 -> 최악의 경우 1000만번 연산 -> 가넝할듯..?
#     # 이동 횟수 ans
#     ans = 0
#     while True:
#         if ans*(ans+1)//2 * k >= n:
#             break
#
#         ans += 1
#
#     # a번 이동 시 도착 좌표, 바라보는 방향, n-1만큼 이동한 좌표
#     # 방향: 왼쪽 0, 오른쪽 1
#     if ans % 2 == 0:
#         goal = - ans // 2 * k
#         dir = 0
#         cur = goal + (ans*(ans+1)//2 * k - (n - 1))
#     else:
#         goal = (ans + 1) // 2 * k
#         dir = 1
#         cur = goal - (ans * (ans + 1) // 2 * k - (n - 1))
#
#     if goal == n-1:
#         dir = not dir  # 전환점에 도달했다면 방향 바꿔주기
#
#     if dir:
#         print(cur, 'R')
#     else:
#         print(cur, 'L')

#ver2. 이분탐색

for _ in range(t):
    n, k = map(int, input().split())
    ans = 0  # 정답 이동 횟수
    left, right = 0, n  # 이동 횟수의 범위
    while left <= right:
        mid = (left + right) // 2

        if mid * (mid + 1) // 2 * k >= n:
            right = mid - 1
        else:
            ans = mid
            left = mid + 1

    ans += 1

    if ans % 2 == 0:
        goal = - ans // 2 * k
        dir = 0
        cur = goal + (ans * (ans + 1) // 2 * k - (n - 1))
    else:
        goal = (ans + 1) // 2 * k
        dir = 1
        cur = goal - (ans * (ans + 1) // 2 * k - (n - 1))

    if goal == n-1:
        dir = not dir  # 전환점에 도달했다면 방향 바꿔주기

    if dir:
        print(cur, 'R')
    else:
        print(cur, 'L')