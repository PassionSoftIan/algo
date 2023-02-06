import sys
sys.stdin = open('Sum_input.txt')



for tc in range(10):
    input()
    Array = [list(map(int, input().split())) for i in range(100)]
    my_max = 0
    for j in range(100):
        mys = 0
        for k in range(100):
            mys += Array[j][k]
        my_max = max(my_max, mys)

    for j in range(100):
        mys = 0
        for k in range(100):
            mys += Array[k][j]
        my_max = max(my_max, mys)

    mys = 0
    for j in range(100):
        mys += Array[j][j]
    my_max = max(my_max, mys)

    mys = 0
    for j in range(100):
        mys += Array[j][-j-1]
    my_max = max(my_max, mys)

    print(f'#{tc+1} {my_max}')