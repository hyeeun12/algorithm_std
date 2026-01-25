import sys
input = sys.stdin.readline

def can_installed(mid):
    # 공유기 설치 확인
    # 첫번째 집에 먼저 설치해서 확인
    count = 1
    start = houses[0]

    for i in range(1, N):
        # 집 사이 거리가 mid 보다 크면 공유기 범위에서 벗어나니 설치해야함
        if houses[i] - start >= mid:
            count += 1
            start = houses[i]
    if count >= C:
        return True
    else:
        return False

N, C = map(int,input().split())
houses = []
for _ in range(N):
    x = int(input())
    houses.append(x)

# 1) houses 정렬
# 2) 각 집들 간의 최소 거리, 최대 거리 구하기
# 3) 최소거리 ~ 최대거리에서 이분탐색을 활용해 해당 거리만큼 C개의 공유기를 설치할 수 있는지 확인하기
# 4) 설치할 수 있는 거리 중 최대값을 찾아야함

houses.sort()
low = 1 # 최소거리는 적어도 1은 되겠지..
high = houses[-1] - houses[0]
answer = 0

while low <= high:
    mid = (low + high) // 2

    if can_installed(mid):
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)