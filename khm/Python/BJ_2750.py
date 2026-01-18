N = int(input())

# 숫자를 저장할 리스트
numbers = [0] * N

for a in range(N):
    numbers[a] = int(input())

# 1. sort() 함수 사용
# numbers.sort()
#
# for n in numbers:
#     print(n)

# 버블 정렬
for i in range(N-1):
    for j in range(N-1-i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

for n in numbers:
    print(n)