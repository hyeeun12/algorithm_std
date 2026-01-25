#나무 자르기
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 나무 수, 가져갈 나무 길이
tree = list(map(int, input().split()))

# 1억번의 연산 가능
# 완전탐색 -> 최악의 경우 10억번 연산 -> 시간 초과
# 따라서 이분탐색 이용

left, right = 0, max(tree)  # 자를 높이의 범위 설정
ans = 0
while left <= right:  # 자를 높이의 최댓값 구하기
    mid = (left + right) // 2
    sum = 0  # 잘린 나무 길이의 합
    for x in tree:
        if mid <= x:
           sum += x - mid

    if sum < m:  # 너무 높은데서 잘랐음 -> 왼쪽 탐색
        right = mid - 1
    else:  # 낮은데서 잘랐음 -> 더 높이 잘라도 되는지 오른쪽 탐색
        ans = mid  # 정답 후보를 저장
        left = mid + 1

print(ans)