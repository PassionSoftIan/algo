import sys
sys.stdin = open('Ladder_input.txt')


for tc in range(10):
    Test_case = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if ladder[i][j] == 2:
                x = j

    y = 99
    while y != 0:
        #오른쪽이 1인경우
        if x < 99 and ladder[y][x+1] == 1:
            while x < 99 and ladder[y][x+1] == 1:
                x += 1
            else:
                y -= 1

        #왼쪽이 1인경우
        elif x > 0 and ladder[y][x-1] == 1:
            while x > 0 and ladder[y][x-1] == 1:
                x -= 1
            else:
                y -= 1

        #둘 다 0인경우
        else:
            y -= 1


    print(f'#{tc+1} {x}')

