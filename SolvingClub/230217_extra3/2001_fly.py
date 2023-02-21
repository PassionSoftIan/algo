import sys
sys.stdin = open('2001_fly_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result_max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            result = 0
            for k in range(M):
                for n in range(M):
                    result += arr[i+k][j+n]
            if result > result_max:
                result_max = result
    print(f'#{tc} {result_max}')