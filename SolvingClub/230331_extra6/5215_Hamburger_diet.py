import sys
sys.stdin = open('5215_Hamburger_diet_input.txt')

Test_case = int(input())

for tc in range(1, Test_case+1):
    N, L = map(int, input().split())
    ingredient = [list(map(int, input().split())) for _ in range(N)]

    DP_lst = [[0 for _ in range(L+1)] for _ in range(N+1)]

    for i in range(N+1):
        for j in range(L+1):

            if ingredient[i-1][1] <= j:
                DP_lst[i][j] = max(ingredient[i-1][0] + DP_lst[i-1][j-ingredient[i-1][1]], DP_lst[i-1][j])

            else:
                DP_lst[i][j] = DP_lst[i-1][j]

    print(f'#{tc}', DP_lst[N][L])





















# def backtracking(depth, s, num):
#     global result_score, max_result, result_cal
#
#     if depth == num:
#         for n in mixed:
#             result_score += ingredient[n][0]
#             result_cal += ingredient[n][1]
#             # print(ingredient[n][0])
#         # print(mixed)
#         # print(result)
#         # print('----')
#         if result_cal < L:
#             if max_result < result_score:
#                 max_result = result_score
#         result_score = 0
#         result_cal = 0
#         return
#
#     for i in range(s, N):
#         if visited[i] == 0:
#             mixed.append(ingredient_lst[i])
#             visited[i] = 1
#             backtracking(depth+1, i, num)
#             visited[i] = 0
#             mixed.pop()
#
# Test_case = int(input())
#
# for tc in range(1, Test_case+1):
#     N, L = map(int, input().split())
#     ingredient = [] # 평점 - 칼로리
#
#     ingredient_lst = list(range(N))
#
#     mixed = []
#
#     visited = [0] * N
#
#     result_score = 0
#     result_cal = 0
#
#     max_result = 0
#     for nc in range(N):
#         ingredient.append(list(map(int, input().split())))
#
#     for i in range(1, N+1):
#         backtracking(0, 0, i)
#
#     # print(ingredient)
#     # print(ingredient_lst)
#
#     print(f'#{tc}', max_result)