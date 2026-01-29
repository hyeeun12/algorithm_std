#네트워크 연결

import sys
input = sys.stdin.readline

n = int(input())  # 컴퓨터의 수
m = int(input())  # 간선의 수
edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

def make_set(n):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    return parent, rank

def find_set(x, parent):
    if parent[x] != x:
        parent[x] = find_set(parent[x], parent)
    return parent[x]

def union(a, b, parent, rank):
    ref_a = find_set(a, parent)
    ref_b = find_set(b, parent)
    if ref_a == ref_b:  # 이미 같은 집합
        return False
    # 랭크가 더 높은 쪽으로 합치기
    if rank[ref_a] < rank[ref_b]:
        parent[ref_a] = ref_b
    elif rank[ref_a] > rank[ref_b]:
        parent[ref_b] = ref_a
    else:
        parent[ref_b] = ref_a
        rank[ref_a] += 1
    return True

def kruskal(n, edges):
    # edges: (w, u, v) 리스트
    edges.sort()  # 가중치 오름차순
    parent, rank = make_set(n)

    mst_weight = 0
    picked = 0

    for w, u, v in edges:
        if union(u, v, parent, rank):
            mst_weight += w
            picked += 1

            if picked == n-1:
                break

    return mst_weight

total_weight = kruskal(n, edges)
print(total_weight)