import sys
sys.stdin = open('balloon2_input.txt')

Test_case = int(input())

for tc in range(Test_case):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    print(arr)
    max_result = 0
    for i in range(N):
        for j in range(M):
            result = arr[i][j]
            for k in range(4):
                nx, ny = j+dx[k], i+dy[k]
                if 0 <= nx < M and 0 <= ny < N:
                    result += arr[ny][nx]
                if result > max_result:
                    max_result = result
    print(f'#{tc+1} {max_result}')










    # max_result = 0
    # for i in range(N):
    #     for j in range(M):
    #         result = arr[i][j]
    #         for k in range(4):
    #             nx, ny = j+dx[k], i+dy[k]
    #             if 0<= nx <M and 0<= ny <N:
    #                 result += arr[ny][nx]
    #             if max_result < result:
    #                 max_result = result
    # print(f'#{tc+1} {max_result}')












# for tc in range(Test_case):
#     NM = list(map(int, input().split()))
#     arr = [list(map(int, input().split())) for _ in range(NM[0])]
#     # print(arr)
#     di = [0, 1, 0, -1] # 우 하 좌 상
#     dj = [1, 0, -1, 0]
#     N = NM[0]
#     P = NM[1]
#     # print(P)
#     max_result = 0
#     for i in range(N):
#         for j in range(P):
#             result = arr[i][j]
#             for k in range(4):
#                 ni, nj = i+di[k], j+dj[k]
#                 if 0 <= ni < N and 0 <= nj < P:
#                     result += arr[ni][nj]
#                     if max_result < result:
#                         max_result = result
#
#
#     print(f'#{tc + 1} {max_result}')