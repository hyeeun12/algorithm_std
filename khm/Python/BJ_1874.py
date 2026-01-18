# 숫자 개수
N = int(input())

numbers = [0] * N

for i in range(N):
    numbers[i] = int(input())

# stack
stack = []

# 답 리스트
answer = []

# 시작 숫자
n = 1

# numbers index
index = 0

# pop이 가능하기 전까지 push
# 1 ~ N 까지의 숫자만 사용하므로 그 안에서만 while로 반복
while n <= N:
    stack.append(n)
    n += 1
    answer.append('+')
    
    # pop이 가능할 경우
    # stack 안에 숫자가 있고 stack의 top이 numbers의 index와 같으면
    while stack and stack[-1] == numbers[index]:
        stack.pop()
        index += 1
        answer.append('-')
        
        # index가 N과 같아지면 다 꺼낸것이므로 종료
        if index == N:
            break
        
# stack에 숫자가 남아있지만 pop이 불가능한 경우
if index < N:
    print("NO")
else:
    print("\n".join(answer))

