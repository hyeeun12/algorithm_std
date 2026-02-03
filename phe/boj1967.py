#트리의 지름

import sys
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]

for _ in range(n-1):
    u, v, w = map(int, input().split())

    adj[u].append((w, v))
    adj[v].append((w, u))


def dfs(T):
    visited = [False] * (n + 1)
    stack = [(T, 0)]  # (시작 노드, 누적 거리)
    visited[T] = True

    max_dist = 0
    far_node = T

    while stack:
        cur, dist = stack.pop()

        if dist > max_dist:
            max_dist = dist
            far_node = cur

        for w, next in adj[cur]:
            if visited[next]:
                continue

            stack.append((next, dist + w))
            visited[next] = True

    return far_node, max_dist

# 루트 노드에서 가장 먼 노드 찾기
A, _ = dfs(1)
# A에서 가장 먼 거리 = 트리의 지름
_, diameter = dfs(A)

print(diameter)