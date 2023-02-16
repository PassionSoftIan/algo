import sys
sys.stdin = open('4881_min_sum_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)

    for i in range(N):
        for j in range(N):
            arr[i][j]