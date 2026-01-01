#소트인사이드

N = int(input())

numbers = list(map(int, str(N)))

numbers.sort(reverse=True)

print(*numbers, sep='')