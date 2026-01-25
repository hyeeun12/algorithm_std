N = int(input())
adj = [0] * (N + 1)

for i in range(1, N + 1):
    n = int(input())
    adj[i] = n

# 방문기록
visited = [False] * (N + 1)
answer = []

for i in range(1, N + 1):
    # 해당 번호(인덱스)를 방문한 적이 있나
    if not visited[i]:
        stack = []  # 경로 저장용
        current = i # 시작 번호

        while True:
            if not visited[current]:
                visited[current] = True
                stack.append(current)
                # 다음 위치 이동
                current = adj[current]
            else:
                if current in stack:    # 번호가 경로에 있으면 사이클을 돌았다는 의미
                    # stack 내에 current가 처음 등장하는 위치 찾기
                    idx = stack.index(current)
                    # 사이클에 해당하는 부분만 추출
                    cycle = stack[idx:]
                    # 사이클을 돈 결과 숫자들을 answer에 append
                    for j in cycle:
                        answer.append(j)
                break

answer.sort()
print(len(answer))
print(*answer, sep='\n')