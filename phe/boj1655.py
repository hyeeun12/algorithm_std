#가운데를 말해요
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

N = int(input())

left = []  # 최대힙
right = [] # 최소힙

for _ in range(N):
    num = int(input())

    # 첫번째 값이거나 중간값보다 작은 경우
    if not left or num <= -left[0]:
        heappush(left, -num)
    else:
        heappush(right, num)

    # 왼쪽과 오른쪽 개수 맞춰주기 (항상 왼쪽이 1만큼 더 크거나 같게)
    if len(left) > len(right) + 1:
        heappush(right, -heappop(left))
    elif len(left) < len(right):
        heappush(left, -heappop(right))

    print(-left[0])

