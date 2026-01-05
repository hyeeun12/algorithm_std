import heapq

# heapq는 최소힙처럼 동작
heap = []

N = int(input())
input_data = [int(input()) for _ in range(N)]

result = []

for i in input_data:
    if i == 0:
        if not heap:    # heap이 비어있는 경우
            result.append(0)
        else:
            result.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap, i)

for r in result:
    print(r)