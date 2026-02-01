#트리 순회
import sys
input = sys.stdin.readline

def preorder(node):
    if node:  # if node is not None
        print(dic2[node], end="")
        preorder(c1[node])
        preorder(c2[node])

def inorder(node):
    if node:
        inorder(c1[node])
        print(dic2[node], end="")
        inorder(c2[node])

def postorder(node):
    if node:
        postorder(c1[node])
        postorder(c2[node])
        print(dic2[node], end="")


n = int(input())
dic1 = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
    'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
    'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
    'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
    'Y': 25, 'Z': 26
}
dic2 = {v:k for k, v in dic1.items()}  # 키, 값 쌍을 뒤집어 저장 (value로 key를 찾기위해)
c1 = [0] * (n + 1)
c2 = [0] * (n + 1)

for _ in range(n):
    p, lc, rc = input().split()
    if lc != '.':
        c1[dic1[p]] = dic1[lc]
    if rc != '.':
        c2[dic1[p]] = dic1[rc]

preorder(1)
print("")
inorder(1)
print("")
postorder(1)

