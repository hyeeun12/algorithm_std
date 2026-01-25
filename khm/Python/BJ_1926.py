# 도화지 세로 n, 도화지 가로 m
n, m = map(int,input().split())

paper = [list(map(int, input().split())) for _ in range(n)]

# 그림의 개수, 가장 큰 그림의 크기 출력
# 그림 개수 count
count = 0

# 가장 큰 그림 크기 max_size
max_size = 0

# delta
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 방문 기록
visited = [[False] * m for _ in range(n)]

# DFS 스택
stack = []

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and not visited[i][j]:
            count += 1

            # 그림 정보
            stack = [(i, j)]
            visited[i][j] = True
            size = 1

            while stack:
                # 현재 위치
                (cx, cy) = stack.pop()

                # 현재 위치에서 상하좌우 확인
                for d in range(4):
                    nx = cx + dx[d]
                    ny = cy + dy[d]

                    if 0 <= nx < n and 0 <= ny < m:
                        if paper[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            size += 1
                            stack.append((nx, ny))

            # 최대 사이즈 비교
            max_size = max(max_size, size)


print(count)
print(max_size)