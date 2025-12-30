# 백준 크리스마스 파티
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
target_list = list(map(int, input().split()))
scores = [0] * N

for i in range(M):
    game = list(map(int, input().split()))
    target = target_list[i]
    for j in range(N):
        if game[j] == target:
            scores[j] += 1
        else:
            scores[target - 1] += 1

for i in range(N):
    print(scores[i])