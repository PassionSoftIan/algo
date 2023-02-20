import sys
sys.stdin = open('1225_password_input.txt')

for tc in range(10):
    Test_case = int(input())

    data = list(map(int, input().split()))

    while data[-1] > 0:
        for i in range(1, 6):
            A = data.pop(0) - i
            data.append(A)
            if data[-1] <= 0:
                data[-1] = 0
                break
    print(f'#{Test_case}', *data)