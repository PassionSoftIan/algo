import sys
sys.stdin = open('5356_euseok_row_talk_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    arr = [list(map(str, input())) for _ in range(5)]

    max_len = 0
    for i in range(5):
        if max_len < len(arr[i]):
            max_len = len(arr[i])

    char = ''
    for i in range(max_len):
        for j in range(5):
            if i > len(arr[j])-1:
                continue
            else:
                char += arr[j][i]

    print(f'#{tc} {char}')