import sys
sys.stdin = open('bio_isolation_input.txt')


dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]


def experiment(stack, second):
    global result

    bio_hazard = stack

    if second == 0:
        while bio_hazard:
            n, m, bio, direction = bio_hazard.pop()
            arr[n][m] = bio
            result += bio
            bio_lst_1.append([n, m, bio, direction])

    if second % 2 == 0:
        while bio_hazard:
            n, m, bio, direction = bio_hazard.pop()
            ny, nx = n + dy[direction], m + dx[direction]
            if visited[ny][nx] < final_arr[n][m]:
                if ny == 0 or nx == 0 or ny == N - 1 or nx == N - 1:
                    arr[ny][nx] += int(final_arr[n][m]/2)
                    result += int(final_arr[n][m]/2)
                    visited[ny][nx] = final_arr[n][m]
                    final_arr[n][m] = 0
                    info[n][m] = 0
                    info[ny][nx] = direction
                    if direction % 2 == 0:
                        bio_lst_1.append([ny, nx, arr[ny][nx], info[ny][nx]-1])
                    else:
                        bio_lst_1.append([ny, nx, arr[ny][nx], info[ny][nx]+1])
                else:
                    arr[ny][nx] += final_arr[n][m]
                    result += final_arr[n][m]
                    visited[ny][nx] = final_arr[n][m]
                    final_arr[n][m] = 0
                    info[n][m] = 0
                    info[ny][nx] = direction
                    bio_lst_1.append([ny, nx, arr[ny][nx], info[ny][nx]])
            else:
                if ny == 0 or nx == 0 or ny == N - 1 or nx == N - 1:
                    arr[ny][nx] += int(final_arr[n][m]/2)
                    result += int(final_arr[n][m]/2)
                    final_arr[n][m] = 0

                else:
                    arr[ny][nx] += final_arr[n][m]
                    result += final_arr[n][m]
                    final_arr[n][m] = 0

    if second % 2 == 1:
        while bio_hazard:
            n, m, bio, direction = bio_hazard.pop()
            ny, nx = n + dy[direction], m + dx[direction]
            if visited[ny][nx] < arr[n][m]:
                if ny == 0 or nx == 0 or ny == N - 1 or nx == N - 1:
                    final_arr[ny][nx] += int(arr[n][m]/2)
                    result += int(arr[n][m]/2)
                    visited[ny][nx] = arr[n][m]
                    arr[n][m] = 0
                    info[n][m] = 0
                    info[ny][nx] = direction
                    if direction % 2 == 0:
                        bio_lst_0.append([ny, nx, final_arr[ny][nx], info[ny][nx]-1])
                    else:
                        bio_lst_0.append([ny, nx, final_arr[ny][nx], info[ny][nx]+1])
                else:
                    final_arr[ny][nx] += arr[n][m]
                    result += arr[n][m]
                    visited[ny][nx] = arr[n][m]
                    arr[n][m] = 0
                    info[n][m] = 0
                    info[ny][nx] = direction
                    bio_lst_0.append([ny, nx, final_arr[ny][nx], info[ny][nx]])
            else:
                if ny == 0 or nx == 0 or ny == N - 1 or nx == N - 1:
                    final_arr[ny][nx] += int(arr[n][m]/2)
                    result += int(arr[n][m]/2)
                    arr[n][m] = 0

                else:
                    final_arr[ny][nx] += arr[n][m]
                    result += arr[n][m]
                    arr[n][m] = 0


Test_case = int(input())

for tc in range(1, Test_case+1):
    N, M, K = map(int, input().split())
    # N 셀의 개수, M 격리 시간, K 미생물 군집 개수
    global result

    bio_lst_0 = []
    bio_lst_1 = []
    count = 0
    for kc in range(K):
        bio_lst_0.append(list(map(int, input().split()))) # 세로 가로 미생물 수 위치

    arr = [[0]*N for _ in range(N)]
    final_arr = [[0]*N for _ in range(N)]
    info = [[0]*N for _ in range(N)]

    for i in range(M+1):
        result = 0
        visited = [[0] * N for _ in range(N)]
        if i % 2 == 0:
            experiment(bio_lst_0, i)
        else:
            experiment(bio_lst_1, i)

    # print(bio_lst_1)
    #
    # print('---------------arr')
    #
    # for i in arr:
    #     print(i)
    #
    # print('---------------final_arr')
    #
    # for i in final_arr:
    #     print(i)
    #
    # print('---------------visited')
    #
    # for i in visited:
    #     print(i)
    #
    # print('---------------info')
    #
    # for i in info:
    #     print(i)

    print(f'#{tc} {result}')