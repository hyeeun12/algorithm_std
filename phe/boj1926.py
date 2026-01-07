#그림
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 0
max_width = 0

def dfs(r, c):
  stack = [(r, c)]
  visited[r][c] = 1
  width = 0

  while stack:
    cr, cc = stack.pop()
    width += 1

    for dr, dc in dir:
      nr, nc = cr + dr, cc + dc

      if not (0 <= nr < N and 0 <= nc < M):
        continue

      if visited[nr][nc] or not paper[nr][nc]:
        continue
      
      stack.append((nr, nc))
      visited[nr][nc] = 1
  
  return width

for i in range(N):
  for j in range(M):
    if paper[i][j] == 1 and not visited[i][j]:
      w = dfs(i, j)
      if max_width < w:
        max_width = w
      cnt += 1

print(cnt,max_width, sep='\n')
