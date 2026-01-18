#최대힙

import sys
from heapq import heappush, heappop

heap = []
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

for num in nums:
    if not num:
        if heap:
            print(heappop(heap)[1])  # 튜플에서 index 1에 있는 값을 읽어옴
        else:
            print(0)
    else:
        heappush(heap, (-num, num))  # (우선순위, 값)


