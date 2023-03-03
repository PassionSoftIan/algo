import sys
sys.stdin = open('12712_kill_the_fly3_input.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

tx = [1, -1, -1, 1]
ty = [1, 1, -1, -1]

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            count_ten = arr[i][j]
            count_x = arr[i][j]
            for k in range(4):
                for p in range(1, M):
                    ny, nx = i + p*dy[k], j + p*dx[k]
                    zy, zx = i + p*ty[k], j + p*tx[k]
                    if 0 <= ny < N and 0 <= nx < N:
                        count_ten += arr[ny][nx]
                    if 0 <= zy < N and 0 <= zx < N:
                        count_x += arr[zy][zx]
            result.append(count_ten)
            result.append(count_x)

    print(f'#{tc} {max(result)}')