import sys
sys.stdin = open('simple_zip_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N = int(input())
    print(f'#{tc}')
    arr = []
    num = []
    result = 0
    for nc in range(N):
        char = input().split()
        result += int(char[1])
        arr.append(char[0] * int(char[1]))
    num.append(result)
    # print(arr)
    # print(num)
    # print(len(arr[0]))
    count = 0
    idx = 0
    # while idx != num[0]:
    for i in range(len(arr)):
        for j in range(len(arr[i])-1):
            if idx == len(arr[i]):
                break
            if count <= 8:
                print(arr[i][j], end='')
                count += 1
                idx += 1
            if count == 9:
                print(arr[i][j])
                count = 0
                idx += 1
    print()
    # for i in range(num[0]):
    #     for j in range(len(N)):
    #         if i <= i % 10:



        # print(f'{char[0] * int(char[1])}')


    #     num = []
    # for ch in range(1):
    #     num.append(int(char[1]))
    # for i in range(num[0]):
    #     print(f'#{tc} {char[0]}')