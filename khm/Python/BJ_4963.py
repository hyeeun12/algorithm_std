# BFS
from collections import deque
import sys
input = sys.stdin.readline

# delta
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                count += 1
                queue = deque()
                queue.append((i, j))
                graph[i][j] = 0  # 방문 처리

                while queue:
                    x, y = queue.popleft()
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                            graph[nx][ny] = 0
                            queue.append((nx, ny))

    print(count)
