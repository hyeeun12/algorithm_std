#녹색 옷 입은 애가 젤다지?

import heapq
import sys
input = sys.stdin.readline
INF = int(21e8)
start = (0,0)
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dijkstra(i, j):
    pq = [(cave[i][j], i, j)]  # (누적 거리, 노드 위치(행, 열))
    dists = [[INF] * N for _ in range(N)]  # 각 정점까지의 최단거리를 저장할 리스트
    dists[i][j] = cave[i][j]  # 시작 노드 최단 거리 = 0

    while pq:
        dist, cr, cc = heapq.heappop(pq)

        if dists[cr][cc] < dist:
            continue

        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if not (0 <= nr < N and 0 <= nc < N):
                continue

            next_dist = cave[nr][nc]
            new_dist = dist + next_dist

            if dists[nr][nc] <= new_dist:
                continue

            dists[nr][nc] = new_dist
            heapq.heappush(pq, (new_dist, nr, nc))

    return dists

test_case = 1
while True:

    N = int(input())
    if not N:
        break

    cave = [list(map(int, input().split())) for _ in range(N)]

    result = dijkstra(*start)[N-1][N-1]
    print(f'Problem {test_case}: {result}')

    test_case += 1


