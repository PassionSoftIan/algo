import sys
sys.stdin = open('sdoku_input.txt')

def sdoku(arr):
    for x in arr:
        if len(set(x)) != 9:
            return 0
    arr_y = list(zip(*arr))
    for y in arr_y:
        if len(set(y)) != 9:
            return 0
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = set()
            for k in range(3):
                for n in range(3):
                    check.add(arr[i+k][j+n])
            if len(check) != 9:
                return 0
    return 1

Test_case = int(input())

for tc in range(Test_case):
    arr = [list(map(int, input().split())) for _ in range(9)]


    ans = sdoku(arr)
    print(f'#{tc+1} {ans}')