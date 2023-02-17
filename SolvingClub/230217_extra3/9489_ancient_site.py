import sys
sys.stdin = open('9489_ancient_site_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N,M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    result_max = 0
    for i in range(N):
        result = 0
        for j in range(M):
            if arr[i][j] == 0:
                if result >= 1:
                    if result_max < result:
                        result_max = result
                result = 0
            result += arr[i][j]
            if j == M - 1:
                if result >= 1:
                    if result_max < result:
                        result_max = result
    for i in range(M):
        result_2 = 0
        for j in range(N):
            if arr[j][i] == 0:
                if result_2 >= 1:
                    if result_max < result_2:
                        result_max = result_2
                result_2 = 0
            result_2 += arr[j][i]
            if j == N - 1:
                if result_2 >= 1:
                    if result_max < result_2:
                        result_max = result_2
    print(f'#{tc} {result_max}')