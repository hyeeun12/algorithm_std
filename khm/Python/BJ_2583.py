from collections import deque
import sys

input = sys.stdin.readline

M, N, K = map(int, input().split())

# 종이 초기화 (0: 빈 칸, 1: 칠해진 칸)
paper = [[0] * N for _ in range(M)]

# 직사각형 칠하기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = 1

# 이동 방향 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))
    paper[start_x][start_y] = 1  # 방문 처리
    area = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < M and 0 <= ny < N and paper[nx][ny] == 0:
                paper[nx][ny] = 1
                q.append((nx, ny))
                area += 1
    return area

areas = []

# 전체 탐색
for i in range(M):
    for j in range(N):
        if paper[i][j] == 0:
            areas.append(bfs(i, j))

areas.sort()

print(len(areas))
print(*areas)
