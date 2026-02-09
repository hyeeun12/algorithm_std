# 파티
import sys
input = sys.stdin.readline
import heapq

n, m, x = map(int, input().split())
adj = [[] for _ in range(n + 1) for _ in range(n + 1)]
INF = int(21e8)

def dijkstra(start):
    dists = [INF] * (n + 1)
    dists[start] = 0  # 자기 자신까지의 최단거리는 0
    q = [(0, start)]  # 누적 거리, 시작 노드

    while q:
        w, cur = heapq.heappop(q)

        for next_info in adj[cur]:
            next_w, next_node = next_info

            new_w = w + next_w

            if dists[next_node] <= new_w:
                continue

            dists[next_node] = new_w
            heapq.heappush(q, (new_w, next_node))

    return dists


for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))  # 단방향

max_v = 0
fromX = dijkstra(x)
for i in range(1, n + 1):
    t = dijkstra(i)[x] + fromX[i]
    if max_v < t:
        max_v = t

print(max_v)