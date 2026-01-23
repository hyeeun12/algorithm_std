#랜선 자르기
import sys
input = sys.stdin.readline

#시간 제한 2초 = 2억번의 연산
#이분탐색인 이유: 최댓값/최소값 구하는 문제이면서, 수의 범위가 커서 완전 탐색이 불가능함

k, n = map(int, input().split())
cable = [int(input()) for _ in range(k)]

left = 1  # 가능한 최소 길이
right = max(cable)  # 가능한 최대 길이
ans = 0

while left <= right:
    mid = (left + right) // 2
    cnt = sum(x//mid for x in cable)

    if cnt < n:  # 너무 길게 잘라서 충분한 개수가 나오지 않음. 왼쪽 탐색
        right = mid - 1
    else:
        ans = mid  # 정답 후보 갱신
        left = mid + 1  # 더 길게도 가능한지 오른쪽 탐색

print(ans)