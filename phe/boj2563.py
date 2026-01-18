#색종이

T = int(input())
visited = [[0] * 100 for _ in range(100)]
size = 0

for _ in range(T):
    a, b = map(int, input().split())

    for x in range(a, 10 + a):
        for y in range(b, 10 + b):

            if visited[x][y]:
                continue

            visited[x][y] = 1
            size += 1

print(size)