#뭉쳐야 산다

import sys
input = sys.stdin.readline

# def make_set(size):
#     parent = list(range(size + 1))
#     return parent

def find_set(x, parent):
    if parent[x] != x:
        parent[x] = find_set(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    ref_a = find_set(a, parent)
    ref_b = find_set(b, parent)

    parent[ref_b] = ref_a



n, q = map(int, input().split())
parent = list(range(n + 1))
sets = [set() for _ in range(n + 1)]

for i in range(1, n + 1):
    size, *s = map(int, input().split())
    sets[i].update(s)

for _ in range(q):
    command, *nums = map(int, input().split())

    if command == 1:
        a, b = nums
        union(a, b, parent)  # a번 집합과 b번 집합을 합치기

    if command == 2:
        a = nums[0]
        # a번 집합에 속하는 애들을 모두 출력.
        # 이때, 1번 집합과 2번 집합의 루트가 모두 1이라면
        # sets[1]과 sets[2]를 합쳐서 출력




