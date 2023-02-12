import sys
sys.stdin = open('samsung_bus_line_input.txt')

Test_case = int(input())

for tc in range(Test_case):
    N = int(input())
    num = [0] * 5001
    for nc in range(N):
        Ai, Bi = map(int, input().split())
        for i in range(Ai, Bi+1):
            num[i] += 1

    P = int(input())
    result = [num[int(input())] for pc in range(P)]
    print(f'#{tc+1}', *result)