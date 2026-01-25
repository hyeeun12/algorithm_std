#최단경로
import heapq
import sys
input = sys.stdin.readline
INF = int(21e8)

V, E = map(int, input().split())
start_node = int(input())
graph = [[] for _ in range(V + 1)]

def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [INF] * (V + 1)
    dists[start_node] = 0  # 시작 노드까지의 최단거리는 0

    while pq:
        dist, node = heapq.heappop(pq)

        if dists[node] < dist:
            continue

        for next_info in graph[node]:
            next_dist = next_info[0]
            next_node = next_info[1]

            new_dist = dist + next_dist

            if dists[next_node] <= new_dist:
                continue

            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return dists

for _ in range(E):
    u, v, w = map(int, input().split())  # 각 간선을 나타내는 노드와 가중치
    # u와 v는 서로 다르며 w는 10 이하의 자연수
    # 두 노드 사이에 여러 개의 간선이 있을 가능성
    graph[u].append((w, v))

result = dijkstra(start_node)
for i in range(1, V + 1):
    if result[i] == INF:
        print('INF')
    else:
        print(result[i])