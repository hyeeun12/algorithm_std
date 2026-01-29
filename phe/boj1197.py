#최소 스패닝 트리
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]  # 인접리스트로 구현

for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))  # (인접 노드, 가중치)
    graph[b].append((a, w))

import heapq

def prim():
    pq = [(0, 1)]   # 시작 가중치 = 0, 시작 노드
    visited = [0] * (v + 1)
    min_weight = 0  # 가중치 총합
    picked = 0      # 방문한 정점의 수

    while pq and picked < v:
        weight, node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = 1
        min_weight += weight
        picked += 1

        # 인접한 정점들을 후보에 넣기
        for next_node, weight in graph[node]:
            if visited[next_node]:  # 이미 방문한 노드는 패스
                continue
            heapq.heappush(pq, (weight, next_node))

    return min_weight

print(prim())