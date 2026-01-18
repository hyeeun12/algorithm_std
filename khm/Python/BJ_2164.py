from collections import deque

N = int(input())
Queue = deque()

for i in range(1, N + 1):
    Queue.append(i)

while len(Queue) > 1:
    # 카드가 1장 남을 때까지 맨 위의 카드 버리고 그 카드를 가장 아래 카드 밑으로 이동
    Queue.popleft()
    Queue.append(Queue.popleft())

print(Queue[0])