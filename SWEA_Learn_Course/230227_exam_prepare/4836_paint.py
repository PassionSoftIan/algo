import sys
sys.stdin = open('4836_paint.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    result = 0
    for nc in range(N):
        mat = list(map(int, input().split()))
        n,m = mat[0], mat[1]
        for i in range(abs(mat[0] - mat[2]) + 1):
            for j in range(abs(mat[1] - mat[3]) + 1):
                arr[n+i][m+j] += mat[4]
                if arr[n+i][m+j] == 3:
                    result += 1
    print(f'#{tc} {result}')