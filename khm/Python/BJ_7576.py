from collections import deque

def bfs(q):
    # q = queue
    # delta
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        cx, cy = q.popleft()

        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                # 안 익은 토마토가 있으면
                if tomatoes[nx][ny] == 0:
                    tomatoes[nx][ny] = tomatoes[cx][cy] + 1
                    q.append((nx, ny))

    max_day = 1
    for x in range(N):
        for y in range(M):
            max_day = max(max_day, tomatoes[x][y])
            if tomatoes[x][y] == 0:
                print(-1)
                return
    print(max_day - 1)


M, N = map(int, input().split())

tomatoes = [list(map(int,input().split())) for _ in range(N)]

queue = deque()

# 익은 토마토 좌표 찾기
for r in range(N):
    for c in range(M):
        if tomatoes[r][c] == 1:
            queue.append((r, c))

bfs(queue)


