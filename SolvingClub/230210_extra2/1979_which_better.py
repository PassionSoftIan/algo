# import sys
# sys.stdin = open('which_input.txt')
#
# Test_case = int(input())
#
# for tc in range(Test_case):
#     num = list(map(int, input().split()))
#     arr = [list(map(int, input().split())) for _ in range(num[0])]
#     # result = 0
#     count = 0
#     for i in range(num[0]):
#         # result = 0
#         for j in range(num[0] - num[1]):
#             result = 0
#             for k in range(num[1]):
#                     result += arr[i][j + k]
#
#             if result == num[1]:
#                 if j == 0:
#
#                     if arr[i][j+num[1]] == 0:
#                         count += 1
#                 elif j == num[0] - num[1] - 1:
#                     if arr[i][j-1] == 0:
#                         count += 1
#                 else:
#                     if arr[i][j-1] == 0 and arr[i][j+num[1]+1] == 0:
#                         count += 1
#
#
#     print(f'#{tc + 1} {count}')
#
#
#
#
#
#
#
#     #         if result == num[1]:
#     #             count + 1
#     # print(count)
#
#     #         result = arr[i][j]
#     #         if arr[i][j] == 1 and arr[i][j + 1] == 1:
#     #             result += arr[i][j + 1]
#     #             if result == num[1]:
#     #                 count += 1
#     # print(count)
#
#
#
#
#
#
#
#
#     TC = int(input())
#     for T in range(1, TC + 1):
#         N, K = map(int, input().split())
#         mat = []
#
#         result = []
#         cnt = 0
#         for i in range(N):
#             ls = list(map(int, input().split()))
#             mat.append(ls)
#         for i in range(N):
#             cnt = 0
#             for j in range(N):
#                 if mat[i][j] == 1:
#                     cnt += 1
#                 else:
#                     result.append(cnt)
#                     cnt = 0
#             result.append(cnt)
#         cnt = 0
#
#         for i in range(N):
#             cnt = 0
#             for j in range(N):
#                 if mat[j][i] == 1:
#                     cnt += 1
#                 else:
#                     result.append(cnt)
#                     cnt = 0
#             result.append(cnt)
#         res = 0
#         for i in result:
#             if i == K:
#                 res += 1
#         print(f"#{T}", res)
# 4
# 0 1 2 3 4
for i in range(5):
    if i%2 == 1:
        print(i,1)
    else:
        pass