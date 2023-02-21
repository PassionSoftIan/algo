import sys
sys.stdin = open('10760_space_ship_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    result = 0
    for i in range(N):
        for j in range(M):
            count = 0
            for k in range(8):
                nx, ny = j + dx[k], i + dy[k]
                if 0 <= nx < M and 0 <= ny < N:
                    if arr[ny][nx] < arr[i][j]:
                        count += 1
            if count >= 4:
                result += 1
    print(f'#{tc} {result}')