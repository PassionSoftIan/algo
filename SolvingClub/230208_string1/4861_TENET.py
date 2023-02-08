import sys
sys.stdin = open('TENET_input.txt')

Test_case = int(input())

for tc in range(Test_case):
    N = list(map(int, input().split()))
    stn_P = [list(input()) for _ in range(N[0])]
    if N[0] == N[1]:
        # print(f'#{tc + 1} {stn_P}')

        result_1 = []
        for i in range(len(stn_P)):
            for j in range(len(stn_P)):
                if stn_P[i][:] == stn_P[i][::-1]:
                    result_1 = ''.join(stn_P[i][:])
        print(result_1)

        result_2 = []
        for i in range(len(stn_P)):
            for j in range(len(stn_P)):
                if i < j:
                    stn_P[i][j], stn_P[j][i] = stn_P[j][i], stn_P[i][j]
                    if stn_P[i][:] == stn_P[i][::-1]:
                        result_2 = ''.join(stn_P[i][:])

        # print(result_2)

    # if N[0] == N[1]:




                # elif stn_P[:][j] == stn_P[::-1][j]:
                #     print(''.join(stn_P[:][j]))

    # if N[0] != N[1]:
    #     stn_O = [list(input()) for _ in range(N[0])]
    #     print(f'#{tc + 1} {stn_P}')
    #     for i in range(len(stn_P)):
    #         for j in range(len(stn_P)):
    #             if stn_P[i][:]




        # for i in range(N[0]):
        #     for j in range(N[0]):
        #         stn_L = stn_P[1][2]
        #         print(stn_L)

            # if stn_P[:] == stn_P[::-1]:
            #     print(''.join(stn_P[:]))


        # for i in range(N[])






            # print(stn_P[i])
            # print(stn_P[-i-1])
            # A = []
            # if stn_P[i] == stn_P[-i-1]:
            #     A.append(stn_P[i])
                # print(A)


        # A = []
        # if stn_P[M] == stn_P[-(M+1)]:
        #     A.append(stn_P[M])
        #     print(A)




        # stn_L = []
        # for i in range(len(stn_P)):
        #     stn_L.append(stn_P[i][M])
        # print(stn_L)