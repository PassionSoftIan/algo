import sys
sys.stdin = open('balloon2_input.txt')

Test_case = int(input())

for tc in range(Test_case):
    NM = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(NM[0])]
    # print(arr)
    di = [0, 1, 0, -1] # 우 하 좌 상
    dj = [1, 0, -1, 0]
    N = NM[0]
    P = NM[1]
    # print(P)
    max_result = 0
    for i in range(N):
        for j in range(P):
            result = arr[i][j]
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < P:
                    print(i, j, ni, nj)


                    result += arr[ni][nj]
                    if max_result < result:
                        max_result = result