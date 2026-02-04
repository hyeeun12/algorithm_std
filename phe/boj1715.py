#카드 정렬하기
import sys
input = sys.stdin.readline
from heapq import heappush, heappop, heapify

n = int(input())
nums = [int(input()) for _ in range(n)]
heapify(nums)

total = 0
while len(nums) != 1:
    a = heappop(nums)
    b = heappop(nums)

    s = a + b
    total += s

    heappush(nums, s)

print(total)