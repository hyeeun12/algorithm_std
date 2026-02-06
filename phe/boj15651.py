#N과 M (3)
n, m = map(int, input().split())
arr = [num for num in range(1, n+1)]
path = []

def recur(cnt, start):

    if cnt == m:
        print(*path)
        return

    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(cnt + 1, 0)
        path.pop()

recur(0, 0)