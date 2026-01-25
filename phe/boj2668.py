#숫자고르기

# dfs는 스택으로 하기.. 재귀는 시간초과 많이 됨
# dfs 가  bfs보다 나음 (둘다쓸수이슨 문제면. 메모리 문제 등)

N = int(input())
nums = [0] + [int(input()) for _ in range(N)]
in_cycle = set()  # 정답이 들어갈 set (set인 이유는 중복 방지하려고.)

def trace(start):  # 변수이름 짓는거 어렵다..
    path = []
    visited = [0] * (N + 1)

    path.append(start)
    visited[start] = 1
    cur = nums[start]

    while True:
        if visited[cur]:
            break

        path.append(cur)
        visited[cur] = 1

        cur = nums[cur]

    in_cycle.update(path[path.index(cur):])

for i in range(1, N + 1):
    trace(i)

# set는 순서가 없으므로 정렬이 필수이다!
print(len(in_cycle), *sorted(in_cycle), sep="\n")