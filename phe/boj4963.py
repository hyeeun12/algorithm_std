# 섬의 개수
import sys
input = sys.stdin.readline

def dfs(r, c):
    stack = [(r, c)]
    visited[r][c] = 1

    while stack:
        cr, cc = stack.pop()
        visited[cr][cc] = 1

        for k in range(8):
            nr, nc = cr + dr[k], cc + dc[k]

            if not (0 <= nr < h and 0 <= nc < w):
                continue

            if visited[nr][nc]:
                continue

            if not arr[nr][nc]:
                continue

            stack.append((nr, nc))


while True:
    w, h = map(int, input().split())  # 열길이, 행길이

    if w == h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]

    visited = [[0] * w for _ in range(h)]
    # 상하좌우 대각선4방향
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, 1, -1]

    cnt = 0

    for i in range(h):
        for j in range(w):

            if arr[i][j] and not visited[i][j]:
                dfs(i, j)
                cnt += 1

    print(cnt)