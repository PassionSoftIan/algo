import sys
sys.stdin = open('4615_funny_othello_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    arr[N // 2 - 1][N // 2 - 1] = 2
    arr[N // 2 - 1][N // 2] = 1
    arr[N // 2][N // 2] = 2
    arr[N // 2][N // 2 - 1] = 1
    dx = [1, 1, 0, -1, -1, -1, 0, 1,]
    dy = [0, 1, 1, 1, 0, -1, -1, -1,]
    # for nc in range(len(arr)):
    #     print(arr[nc])
    for mc in range(M):
        C = list(map(int, input().split()))
        y,x,z = C[1]-1,C[0]-1,C[2]
        arr[y][x] = z
        # for nc in range(len(arr)):
        #     print(f'#{tc} {arr[nc]}')
        # print()
        for k in range(8):
            temp = []
            for n in range(1, N):
                nx = x + n * (dx[k])
                ny = y + n * (dy[k])
                if 0 <= nx < N and 0 <= ny < N:
                    if arr[ny][nx] == 0:
                        break
                    if arr[ny][nx] != z:
                        temp.append(ny)
                        temp.append(nx)
                        # print(temp)
                    else:
                        while temp:
                            tx = temp.pop()
                            ty = temp.pop()
                            arr[ty][tx] = z
                        break
        count_1 = 0
        count_2 = 0
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 1:
                    count_1 += 1
                if arr[i][j] == 2:
                    count_2 += 1
        # for i in arr:
            # print(f'#{tc} {i}')
    print(f'#{tc} {count_1} {count_2}')
        # print()
