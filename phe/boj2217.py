#로프

N = int(input())
arr = [int(input()) for _ in range(N)]
arr = sorted(arr)
max_v = 0
for i in range(N):
    if max_v < arr[i] * (N - i):
        max_v = arr[i] * (N - i)

print(max_v)
