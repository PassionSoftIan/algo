import sys
sys.stdin = open('palindrome.txt')

for _ in range(10):
    t = int(input())
    arr = [list(map(str, input())) for _ in range(8)]
    B = []
    for i in range(8):
        for j in range(9-t):
            if arr[i][j:j+t] == arr[i][j:j+t][::-1]:
                B.append(arr[i][j:j+t])

    for i in range(8):
        for j in range(8):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    A = []
    for i in range(8):
        for j in range(9-t):
            if arr[i][j:j+t] == arr[i][j:j+t][::-1]:
                A.append(arr[i][j:j+t])

    print(f'#{_+1} {len(A) + len(B)}')