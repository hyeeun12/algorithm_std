N = list(map(int, input())) # 입력받은 숫자를 리스트로 변환
L = len(N)
for i in range(L):
    max_index = i   # 최대값을 N[i]로 먼저 설정
    for j in range(i+1, L):
        if N[j] > N[max_index]:
            # N[i+1] ~ N[L-1] 까지 값을 N[max_index]와 비교했을 때
            # 전자가 더 크면 max_index를 교체
            max_index = j
    if N[i] < N[max_index]: # 최대수 자리 교체
        N[i], N[max_index] = N[max_index], N[i]

for n in N:
    print(n, end="")