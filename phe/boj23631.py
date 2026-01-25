#진심 좌우 반복뛰기
import sys
input = sys.stdin.readline

def binary_search(n, k):
    left, right = 0, n  # 점프 횟수 범위
    ans = 0  # x좌표

    while left <= right:
        mid = (left + right) // 2       # 현재까지 점프 횟수
        cur = k * mid * (mid + 1) // 2  # 현재까지 총 이동거리

        if cur < n - 1:
            ans = mid  # 정답 후보 갱신
            left = mid + 1
        elif cur == n - 1:
            if mid % 2 == 0:
                ans = mid + 1
                return ans, 'R'
            else:
                return - mid, 'L'
        else:
            right = mid - 1

    if ans % 2 == 0:
        return ans, 'R'
    else:
        return ans, 'L'

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())

    if n <= k:
        print(n-1, 'R')
        continue

    # l번 점프했을 때 총 이동거리 k(1 + 2 + 3 + ... l) 가  n보다 작아야 한다.
    # 즉, l의 최댓값을 구해야 하므로 이분탐색
    print(*binary_search(n, k))


