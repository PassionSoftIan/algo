import sys
sys.stdin = open('4880_card_input.txt')

ls = [0,3,1,2]
def result(start,end):                          ## 두 점의 가위바위보를 구하는 함수
    if ls[rsp[end]] == rsp[start]:
        return end
    else:
        return start


def r(start,end):
    if start == end:                ## 만약에 시작과 끝이 같다면
        return start                ## start 를 리턴
    else:
        return result(r(start,(start+end)//2),r((start+end)//2+1,end))  ## 아니라면 다른 두 그룹에서 이기고 올라온 애들을 싸움시킨애를 리턴



TC = int(input())
for T in range(1,TC+1):
    N = int(input())
    rsp = list(map(int,input().split()))
    print(f"#{T}", r(0,N-1)+1)




# def check(divied):
#     winner = []
#     for i in range(len(divied)):
#         for j in range(1):
#             if divied[i][j] == 1 and divied[i][j+1] == 3:
#                 winner.append(divied[i][j])
#
#             elif divied[i][j] == 2 and divied[i][j+1] == 1:
#                 winner.append(divied[i][j])
#
#             elif divied[i][j] == 3 and divied[i][j+1] == 2:
#                 winner.append(divied[i][j])
#
#             else:
#                 winner.append(divied[i][j + 1])
#     print(winner)
#
# def Power(Base):
#     result = []
#     for i in Base:
#         result.append(i)
#     return result
#
# Test_case = int(input())
#
# for tc in range(1, Test_case+1):
#     N = int(input())
#     card = list(map(int, input().split()))
#     card_divied = []
#
#
#     if N % 2 == 0:
#         for i in range(N//2 - 1):
#             card_divied.append([card[i], card[i+1]])
#         for j in range(N//2, N - 1):
#             card_divied.append([card[j], card[j+1]])
#     # print(card_divied)
#     print(Power(card))
#     # check(card_divied)











    # N_bit = [[0] * N for i in range(N)]
    # print(N_bit)
    # for i in N:
    #     for j in range(len(N)):
    #         for k in range(len(N)-1):
    #             if i == 1:
    #                 if i+k == 3:
    #                     N_bit[j][k] += 1
    #                 if i+k == 1:
    #                     if i > i+k:
    #                         N_bit[j][k] += 1
    #                     else:
    #                         N_bit[j][j] += 1
    #             else:
    #                 break


