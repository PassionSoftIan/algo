import sys
sys.stdin = open('5176_binary_search_input.txt')

# def inorder(node):
#     for i in range(1, V+1):
#         inorder(tree[node][0])
#         tree[node][0] = i
#         inorder(tree[node][1])
#     return tree


Test_case = int(input())

for tc in range(1, Test_case + 1):
    V = int(input())
    E = V - 1
    tree = [[0] * 3 for i in range(V+1)]
    edge = [0] * ((V - 1) * 2)
    while 0 in edge:
        for i in range(V//2):
            if 2*i < V:
                edge[2*i] = i
                edge[2*i + 2] = i
        for i in range((V-1)*2):
            if 2*i < V:
                edge[2*i + 1] = i+2


    print(edge)


    # tree[]
# inorder(1)

# 0 0 0
# 2 3 0
# 4 5 1
# 6 0 1
# 0 0 2
# 0 0 2
# 0 0 3