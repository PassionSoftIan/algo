import sys
sys.stdin = open('1232_binary_tree_calculation_input.txt')

def postorder(node):
    if type(arr[node][1]) == int:
        return arr[node][1]
    else:
        left = postorder(arr[node][2])
        right = postorder(arr[node][3])
        if arr[node][1] == '+':
            return left + right
        elif arr[node][1] == '-':
            return left - right
        elif arr[node][1] == '*':
            return left * right
        elif arr[node][1] == '/':
            return left // right

for tc in range(1, 11):
    V = int(input())
    E = V-1
    arr = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(V)]
    arr.insert(0, [0, 0, 0, 0])
    print(arr)
    print(f'#{tc} {postorder(1)}')

