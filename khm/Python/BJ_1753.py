# 정점의 개수 V와 간선의 개수 E
import heapq
import sys

input = sys.stdin.readline

V, E = map(int,input().split())
start = int(input())

graph = [[] for _ in range(V + 1)]
for i in range(E):
    # u : 시작점, v : 도작점, w : 가중치
    u, v, w = map(int,input().split())
    graph[u].append((v, w))

# 거리 체크 리스트
INF = 10**9
distance = [INF] * (V + 1)
queue = []

def dijkstra(start):
    # 시작지점 초기화
    # 시작지점 거리는 0
    distance[start] = 0
    heapq.heappush(queue, (0, start))   # 거리, 정점을 queue에 삽입

    while queue:
        dist, now = heapq.heappop(queue)

        # 현재 노드와 연결된 정점들 찾기
        for next, weight in graph[now]:
            # 방문한 적이 없다면 거리 계산해서 갱신하기
            # 이때, 기존 distance 값과 비교해서 최소값을 넣기
            new_dist = dist + weight
            if new_dist < distance[next]:
                distance[next] = new_dist
                heapq.heappush(queue, (new_dist, next))

dijkstra(start)
for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])