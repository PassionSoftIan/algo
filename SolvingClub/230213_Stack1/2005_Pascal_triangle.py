import sys
sys.stdin = open('2005_Pascal_triangle_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    arr[0][0] = 1
    for k in range(N):
        arr[k][0] = 1
    for i in range(N-1):
        for j in range(N-1):
            arr[i+1][j+1] = arr[i][j] + arr[i][j+1]
    print(f'#{tc}')
    # print(arr)
    for n in range(len(arr)):
        print(*arr[n][0:n+1])