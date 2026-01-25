import heapq

N = int(input())

numbers = [int(input()) for _ in range(N)]

# 중간값 : 정렬된 숫자 배열에서 가운데에 위차한 값
# 숫자 개수가 홀수개면 중간에 위치한 하나의 숫자가 중간값
# 짝수개면 중간에 위치한 두 숫자 중 제일 작은 값을 중간값으로
# 숫자 배열을 왼/오 두 구역으로 나눠서 왼쪽 가장 끝에 위치한 값이 중간값이 되도록(왼쪽 구역의 최대값)
# [1, 2, 4] [6, 12] 인 경우 왼쪽의 최대값이 중간값
# [1, 2, 4] [6, 10, 12] 인 경우 왼쪽 최대값과 오른쪽 최소값 비교 -> 왼쪽 최대값이 중간값

# 파이썬에는 최대힙 없음. 음수로 값을 저장하면 최대힙처럼 사용 가능

left = []   # 최대힙
right = []  # 최소힙

for n in numbers:
    if not left or n <= -left[0]:  # 첫번째 입력 수 이거나 숫자가 왼쪽의 최대값(중간값)보다 작은 경우
        heapq.heappush(left, -n)
    else:
        heapq.heappush(right, n)

    # left와 right의 개수는 left = right 이거나 left = right + 1 이어야 함
    if len(left) > len(right) + 1:  # left가 right + 1보다 크면 2개 이상 차이난다는 뜻이니 개수를 맞추가 위해 left 하나를 오른쪽으로 넘김
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):    # right가 left보다 많으면 안되므로 right의 숫자를 left로 넘김
        heapq.heappush(left, -heapq.heappop(right))

    print(-left[0])