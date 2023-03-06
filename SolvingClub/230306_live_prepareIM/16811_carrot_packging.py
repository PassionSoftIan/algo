import sys
sys.stdin = open('16811_carrot_packging_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N = int(input())
    S = N//2

    small = []
    medium = []
    large = []

    carrot = list(map(int, input().split()))

    for i in range(N):
        count = 0
        for j in range(N):
            if carrot[i] <= carrot[j]:
                count += 1
        if 2 * S <= count:
            small.append(carrot[i])
        if S < count < N - S:
            medium.append(carrot[i])
        if count <= S:
            large.append(carrot[i])
    print(small, medium, large)