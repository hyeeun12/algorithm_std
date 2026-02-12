#트리
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = list(map(int, input().split()))
children = [[] for _ in range(N)]

for c, p in enumerate(arr):
    if p == -1:
        root = c
    else:
        children[p].append(c)

num = int(input())  # 지울 노드
visited = [False] * N
cnt = 0

def bfs(start):
    q = deque([start])
    global cnt

    while q:
        cur = q.popleft()

        if not children[cur]:
            cnt += 1
            continue

        for next in children[cur]:

            if next == num:
                if len(children[cur]) == 1:
                    cnt += 1  # 부모가 새로운 리프 노드가 되는 경우
                continue

            if visited[next]:
                continue

            visited[next] = True
            q.append(next)


if num == root:
    print(0)
else:
    bfs(root)
    print(cnt)