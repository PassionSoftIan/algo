import sys
sys.stdin = open('5097_rotation_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    for j in range(M):
        A = data.pop(0)
        data.append(A)
    print(f'#{tc} {data[0]}')