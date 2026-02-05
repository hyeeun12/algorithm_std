#치즈
import sys

input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    visited = [[False] * M for _ in range(N)]
    q = deque([(r, c)])

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]

            if not (0 <= nr < N and 0 <= nc < M):
                continue

            if visited[nr][nc]:
                continue

                visited[nr][nc] = True

        if arr[nr][nc]:  # 치즈 표면 -> 리스트에 추가
            cheese.append((nr, nc))
        else:  # 공기
            q.append((nr, nc))


cnt = 0
size = 0
while True:
    cheese = []
    bfs(0, 0)
    for r, c in cheese:  # 치즈 표면 좌표를 0으로 설정
        arr[r][c] = 0

    if not cheese:
        print(cnt, size, sep="\n")
        break

    cnt += 1
    size = len(cheese)