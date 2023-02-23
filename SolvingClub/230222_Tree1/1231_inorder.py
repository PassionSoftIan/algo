import sys
sys.stdin = open('1231_inorder_input.txt')

def inorder(node):
    if node <= V:
        inorder(node*2)
        print(str[node], end='')
        inorder(node*2+1)

for tc in range(1, 11):
    str = [0]
    V = int(input())
    for vc in range(V):
        arr = list(input().split())
        str.append(arr[1])
    print(f'#{tc} ', end = ''), inorder(1)
    print()