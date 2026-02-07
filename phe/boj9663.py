#N-Queen
import sys
input = sys.stdin.readline

def dfs(row):
    global answer

    if row == N:
        answer += 1
        return

    for col in range(N):

        if c[col] or diag1[row - col + N - 1] or diag2[row + col]:
            continue

        visited[row][col] = c[col] = diag1[row - col + N - 1] = diag2[row + col] = True
        dfs(row + 1)
        visited[row][col] = c[col] = diag1[row - col + N - 1] = diag2[row + col] = False


N = int(input())
visited = [[False] * N for _ in range(N)]
answer = 0  # 가능한 방법의 수
c = [False] * N
diag1 = [False] * (2 * N - 1)
diag2 = [False] * (2 * N - 1)

dfs(0)
print(answer)
