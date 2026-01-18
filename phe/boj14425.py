#문자열 집합
#해시셋
N, M = map(int, input().split())
s = set(input() for _ in range(N))

cnt = 0

for _ in range(M):
    word = input()
    if word in s:
        cnt += 1

print(cnt)