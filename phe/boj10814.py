N = int(input())

lst = []
idx = 0
for i in range(N):
    age, name = input().split()
    lst.append((int(age), name, idx))

    idx += 1

lst.sort(key=lambda x: (x[0], x[2]))

for i in lst:
    print(f'{i[0]} {i[1]}')