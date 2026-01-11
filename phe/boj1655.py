#가운데를 말해요 ( 아직 못품)

from heapq import heappush, heappop
import sys

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    num = int(input())
    heappush(heap, num)

    M = len(heap)
    print(heap)

    if M % 2 == 0:
        print(min(heap[M//2], heap[M//2-1]))
    else:
        print(heap[M//2])