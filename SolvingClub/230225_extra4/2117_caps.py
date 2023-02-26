import sys
sys.stdin = open('2117_caps_input.txt')

Test_case = int(input())
for tc in range(1, Test_case + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0
    for k in range(1, N):
        for n in range(N):
            for m in range(N):
                tem_count = 0
                for i in range(-(k - 1), k):
                    for j in range(-(k - 1) + abs(i), k - abs(i)):
                        if 0 <= n + i < N and 0 <= m + j < N:
                            if arr[n + i][m + j] == 1:
                                tem_count += 1
                            if tem_count > max_count:
                                max_count = tem_count

    # max_count = 0
    # for n in range(N):
    #     for m in range(N):
    #         checker(N)
    # if max_count < checker(N):
    #     max_count = checker(N)

    print(max_count)