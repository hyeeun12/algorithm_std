#연결 요소의 개수

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(node):
    stack = [node]

    while stack:
        t = stack.pop()

        for i in range(len(adj[t])):
            new_node = adj[t][i]

            if visited[new_node]:
                continue

            stack.append(new_node)
            visited[new_node] = 1

cnt = 0
for i in range(1, N+1):

    if visited[i]:
        continue

    dfs(i)
    cnt += 1

print(cnt)