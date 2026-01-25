#수 찾기
#1 set로 탐색
import sys
input = sys.stdin.readline

# N = int(input())
# a = set(map(int, input().split()))
# M = int(input())
# b = list(map(int, input().split()))
#
# for num in b:
#     if num in a:
#         print(1)
#     else:
#         print(0)

#2 이진검색
def binary_search(target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == arr[mid]:
            return 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return 0

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

arr.sort()  # 이진 검색은 항상 정렬된 데이터에 적용해야함
for target in targets:
    print(binary_search(target))
