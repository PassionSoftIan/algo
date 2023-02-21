import sys
sys.stdin = open('1859_milionare_input.txt')
Test_case = int(input())

for tc in range(1, Test_case + 1):
    N = int(input())
    for nc in range(N):
        M = list(map(int, input().split()))
        result = 0
        for i in range(N-1):
            for j in range(1, N):
                if M[i] < M[i+j]:
                    result += M[i+j] - M[i]
                    break
        print(result)