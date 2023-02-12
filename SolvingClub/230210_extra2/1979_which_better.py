import sys
sys.stdin = open('which_input.txt')

Test_case = int(input())

for tc in range(Test_case):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N-K+1):
            result = arr[i][j]
            if j == 0 and arr[i][j] == 1 and arr[i][j+K] == 0:
                for k in range(1, K):
                    result += arr[i][j+k]
                if result == K:
                    count += 1
            if 0 < j < N - K and arr[i][j] == 1 and arr[i][j+K] == 0 and arr[i][j-1] == 0:
                for k in range(1, K):
                    result += arr[i][j+k]
                if result == K:
                    count += 1
            if j == N - K and arr[i][j] == 1 and arr[i][j-1] == 0:
                for k in range(1, K):
                    result += arr[i][j+k]
                if result == K:
                    count += 1
    for i in range(N):
        for j in range(N-k+1):
            result = arr[j][i]
            if j == 0 and arr[j][i] == 1 and arr[j+K][i] == 0:
                for k in range(1, K):
                    result += arr[j+k][i]
                if result == K:
                    count += 1
            if 0 < j < N - K and arr[j][i] == 1 and arr[j+K][i] == 0 and arr[j-1][i] == 0:
                for k in range(1, K):
                    result += arr[j+k][i]
                if result == K:
                    count += 1
            if j == N - K and arr[j][i] == 1 and arr[j-1][i] == 0:
                for k in range(1, K):
                    result += arr[j+k][i]
                if result == K:
                    count += 1



    print(f'#{tc+1} {count}')