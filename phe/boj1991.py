#트리 순회
import sys
input = sys.stdin.readline

def preorder(T):
    if T and T!= '.':
        print(T, end="")
        preorder(left[T])
        preorder(right[T])

def inorder(T):
    if T and T != '.':
        inorder(left[T])
        print(T, end="")
        inorder(right[T])

def postorder(T):
    if T and T != '.':
        postorder(left[T])
        postorder(right[T])
        print(T, end="")


n = int(input())
left = {}
right = {}

for _ in range(n):
    p, c1, c2 = input().split()
    left[p] = c1
    right[p] = c2

preorder('A')
print()
inorder('A')
print()
postorder('A')
