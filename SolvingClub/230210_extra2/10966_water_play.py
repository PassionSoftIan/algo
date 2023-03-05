import sys
sys.stdin = open('10966_water_play_input.txt')
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M):
            a = 0
            if arr[i][j] == 'L':
                a += 1
                q = deque()
                q.appendleft((i, j, a))
                flag = True
                while flag:
                    m, n, c = q.popleft()
                    for k in range(4):
                        ny, nx = m + dy[k], n + dx[k]
                        if 0 <= ny < N and 0 <= nx < M:
                            if arr[ny][nx] == 'L':
                                q.appendleft((ny, nx, c + 1))

                            if arr[ny][nx] == 'W':
                                flag = False
                                break
                result += c

    print(f'#{tc} {result}')