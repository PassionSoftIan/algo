import sys
sys.stdin = open('1945_simple_decomposition_of_prime_factorization.txt')

Test_case = int(input())

for i in range(Test_case):
    N = int(input())
    prime = [2, 3, 5, 7, 11]
    count = [0] * 12
    for j in prime:
        while N % j == 0:
            N = N / j
            count[j] += 1
    count_fin = []
    for k in prime:
        count_fin.append(count[k])
    print(f'#{i+1}', *count_fin)




# for i in range(Test_case):
#     N = int(input())
#     count_2 = 0
#     count_3 = 0
#     count_5 = 0
#     count_7 = 0
#     count_11 = 0
#     while N % 2 == 0:
#         N = N / 2
#         count_2 += 1
#     while N % 3 == 0:
#         N = N / 3
#         count_3 += 1
#     while N % 5 == 0:
#         N = N / 5
#         count_5 += 1
#     while N % 7 == 0:
#         N = N / 7
#         count_7 += 1
#     while N % 11 == 0:
#         N = N / 11
#         count_11 += 1
#
#     count_fin = [count_2, count_3, count_5, count_7, count_11]
#     print(count_fin)
#
#     print(f'#{i+1}', *count_fin)