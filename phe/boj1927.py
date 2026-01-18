#최소힙
import sys
input = sys.stdin.readline

N = int(input())
heap = [0] * (N + 1)  # 0번 인덱스는 쓰지 않음 (0번 인덱스 == 루트의 부모 -> while 조건에서 사용)
last = 0  # 현재 힙의 마지막 원소 위치 (힙 크기)

def enq(n):
    global last
    last += 1  # 힙 크기를 1 늘리고
    heap[last] = n  # 맨 끝 자리에 새 값을 넣기
    c = last  # 자식 노드 인덱스 (현재 노드)
    p = c // 2  # 부모 노드 인덱스
    while p!=0 and heap[p] > heap[c]:  # 새로 들어간 값과 부모 노드 값 비교
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


for _ in range(N):
    num = int(input())
    if num:
        enq(num)
    else:
        if not last:
            print(0)
        else:
            print(heap[1])
            heap[1] = heap[last]
            heap[last] = 0
            last -= 1
            p = 1 # 현재 노드=부모 노드 인덱스
            while True:
                c = p * 2
                # 만약 c가 last보다 크다면 break
                if c > last:
                    break

                # 만약 왼쪽 자식보다 오른쪽 자식이 더 작으면 오른쪽과 스왑
                if c + 1 <= last and heap[c] > heap[c + 1]:
                    c += 1

                # 부모와 자식 값 비교
                if heap[p] <= heap[c]:
                    break

                heap[p], heap[c] = heap[c], heap[p]
                p = c
