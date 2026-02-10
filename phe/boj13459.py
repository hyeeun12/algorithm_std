#구슬 탈출
import sys
input = sys.stdin.readline
from collections import deque

#n, m은 행길이, 열길이
N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
# 빨간 공과 파란 공의 상태를 저장하기 위해 4차원 visited 배열 사용
# visited[rr][rc][br][bc]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def move(r, c, dir):
    cnt = 0  # 이동한 거리
    while arr[r + dr[dir]][c + dc[dir]] != '#':
        r += dr[dir]
        c += dc[dir]
        cnt += 1

        if arr[r][c] == 'O':
            return r, c, cnt

    return r, c, cnt

def bfs(rr, rc, br, bc, cnt):
    q = deque([(rr, rc, br, bc, cnt)])
    visited[rr][rc][br][bc] = True

    while q:
        rr, rc, br, bc, cnt = q.popleft()

        if cnt == 10:
            continue

        for dir in range(4):
            nr1, nc1, cnt1 = move(rr, rc, dir)
            nr2, nc2, cnt2 = move(br, bc, dir)
            
            # A, B가 둘다 구멍에 들어갈 수 있으면 탈락
            # B가 구멍에 들어갔다면 탈락
            if arr[nr2][nc2] == 'O':
                continue

            # 만약 빨간 공의 위치가 'O'이라면 return True
            if arr[nr1][nc1] == 'O':
                return 1

            # 만약 두 공의 위치가 겹친다면 더많이 이동한 공을 한 칸 뒤로 보내기
            if nr1 == nr2 and nc1 == nc2:
                if cnt1 > cnt2:
                    nr1 -= dr[dir]
                    nc1 -= dc[dir]
                else:
                    nr2 -= dr[dir]
                    nc2 -= dc[dir]

            # 이미 방문한 상태라면 continue
            if visited[nr1][nc1][nr2][nc2]:
                continue

            q.append((nr1, nc1, nr2, nc2, cnt + 1))
            visited[nr1][nc1][nr2][nc2] = True

    return 0

for i in range(N):
    if 'R' in arr[i]:
        rr = i
        rc = arr[i].index('R')
    if 'B' in arr[i]:
        br = i
        bc = arr[i].index('B')

print(bfs(rr, rc, br, bc, 0))