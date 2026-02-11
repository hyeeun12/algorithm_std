#구슬탈출 2
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
visited = set()
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def move(r, c, dir):
    cnt = 0
    while arr[r + dr[dir]][c + dc[dir]] != '#':
        # '#'이나 'O'이 나올때까지 이동
        r += dr[dir]
        c += dc[dir]
        cnt += 1

        if arr[r][c] == 'O':
            return r, c, cnt

    return r, c, cnt


def bfs(rr, rc, br, bc, cnt):
    visited.add((rr, rc, br, bc))
    q = deque([(rr, rc, br, bc, cnt)])

    while q:
        rr, rc, br, bc, cnt = q.popleft()

        if cnt == 10:
            continue

        for dir in range(4):
            nrr, nrc, cnt1 = move(rr, rc, dir)
            nbr, nbc, cnt2 = move(br, bc, dir)

            if arr[nbr][nbc] == 'O':
                continue

            if arr[nrr][nrc] == 'O':
                return cnt + 1

            if nbr == nrr and nbc == nrc:
                if cnt1 < cnt2:
                    nbr -= dr[dir]
                    nbc -= dc[dir]
                else:
                    nrr -= dr[dir]
                    nrc -= dc[dir]

            if (nrr, nrc, nbr, nbc) in visited:
                continue

            visited.add((nrr, nrc, nbr, nbc))
            q.append((nrr, nrc, nbr, nbc, cnt + 1))

    return -1

rr = rc = br = bc = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            rr, rc = i, j
        elif arr[i][j] == 'B':
            br, bc = i, j

print(bfs(rr, rc, br, bc, 0))