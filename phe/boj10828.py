# 스택

import sys
input = sys.stdin.readline

N = int(input())
stack = [0] * N
top = -1

def push(item):
    global top
    top += 1
    stack[top] = item
    return

def pop():
    global top
    if top == -1:
        return -1
    else:
        top -= 1
        return stack[top + 1]


for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        push(int(command[1]))
    elif command[0] == 'pop':
        print(pop())
    elif command[0] == 'size':
        print(top + 1)
    elif command[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])

