import sys
sys.stdin = open('number_spin_input.txt')

Test_case = int(input())
for tc in range(1, Test_case+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    nin_degrees = []
    oez_degrees = []
    tsz_degrees = []
    # print(arr[-3][0])

    for i in range(0, N):
        tmp = ''
        for j in range(1, N+1):
            tmp += arr[-j][i]
        nin_degrees.append(tmp)
    for i in range(1, N + 1):
        tmp = ''
        for j in range(1, N + 1):
            tmp += arr[-i][-j]
        oez_degrees.append(tmp)
    for i in range(1, N + 1):
        tmp = ''
        for j in range(N):
            tmp += arr[j][-i]
        tsz_degrees.append(tmp)

    print(f'#{tc}')
    for i in range(N):
        print(nin_degrees[i], oez_degrees[i], tsz_degrees[i])