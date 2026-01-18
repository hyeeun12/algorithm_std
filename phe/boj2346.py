#풍선터뜨리기

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, idx, move):
        self.idx = idx    # 풍선 번호
        self.move = move  # 안에 적혀있는 숫자
        self.prev = None
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, idx, data):
        new_node = Node(idx, data)

        if self.head is None:
            # 첫 노드: head=tail=prev=next=자신
            self.head = new_node
            self.tail = new_node
            new_node.prev = new_node
            new_node.next = new_node
        else:
            # 처음이 아니라면 tail 뒤에 붙이기
            new_node.prev = self.tail
            new_node.next = self.head

            self.tail.next = new_node
            self.head.prev = new_node

            self.tail = new_node


    def remove(self, node):
    # 이 문제는 list length가 1일 때 경우는 고려 안해도 되서 생략함
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        if node == self.head:
            self.head = next_node
        if node == self.tail:
            self.tail = prev_node


N = int(input())
nums = list(map(int, input().split()))

balloons = CircularLinkedList()
for i, num in enumerate(nums):
    balloons.append(i + 1, num)

answer = []
cur = balloons.head

for _ in range(N):
    answer.append(cur.idx)
    k = cur.move

    balloons.remove(cur)

    if k > 0:
        for _ in range(k):
            cur = cur.next
    else:
        for _ in range(-k):
            cur = cur.prev


print(*answer)
