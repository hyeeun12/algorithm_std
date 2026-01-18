N = int(input())

# 나이 범위(1 ~ 200)
age_range = [[] for _ in range(201)]

# 카운트 정렬
# 해당하는 나이 index에 이름 추가
# 나이 순서대로 출력하면 끝
for _ in range(N):
    age, name = input().split()
    age = int(age)
    age_range[age].append(name)

for age in range(201):
    for name in age_range[age]:
        print(age, name)
        