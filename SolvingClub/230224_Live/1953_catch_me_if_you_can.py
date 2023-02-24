import sys
sys.stdin = open('1953_catch_me_if_you_can_input.txt')

def BFS(start, L):
    q = [start]
    count = 1
    time = L
    while q:
        i, j, t = q.pop(0)
        if t >= time:
            continue
        for k in ctrl[arr[i][j]]:
            nx, ny = j+dx[k], i+dy[k]
            if 0 <= nx < M and 0 <= ny < N:
                if visited[ny][nx] == 0 and arr[ny][nx] > 0 and checker[k] in ctrl[arr[ny][nx]]:
                    q.append([ny, nx, t + 1])
                    visited[ny][nx] = 1
                    count += 1
    return count

Test_case = int(input())

for tc in range(1, Test_case + 1):
    # 터널의 세로크기 N, 가로크기 M,
    # 맨홀뚜껑 세로 위치 R, 가로 위치 C
    # 탈출 이후 경과 시간 L
    N, M, R, C, L = map(int, input().split())
    # print(N, M, R, C, L)
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, 0, -1, 0] # 우 하 좌 상
    dy = [0, 1, 0, -1]
    ctrl = [[], [0, 1, 2, 3], [3, 1], [2, 0], [3, 0], [1, 0], [1, 2], [3, 2]]
    visited = [[0] * (M+1) for _ in range(N+1)]
    visited[R][C] = 1
    # checker = {0:2, 2:0, 3:1, 1:3}
    checker = [2, 3, 0, 1]

    print(f'#{tc} {BFS([R,C,1], L)}')