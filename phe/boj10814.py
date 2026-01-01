import sys
input = sys.stdin.read

_, *lst = input().splitlines()

lst.sort(key=lambda x : int(x.split()[0]))

print(*lst, end="\n")