import sys
sys.stdin = open('tree_input.txt')


def preorder(node):
    if node != 0:
        # 전위 순회기 떄문에
        # 내가 할일 먼저 한다.
        # 지금 문제에서 할일은? 나를 출력
        print(node, end=' ')
        # 왼쪽 자식을 조사
        preorder(left[node])
        # 오른쪽 자식을 조사
        preorder(right[node])

def inorder(node):
    if node != 0:
        # 왼쪽 자식을 조사
        inorder(left[node])
        # 중위 순회
        print(node, end=' ')
        # 오른쪽 자식을 조사
        inorder(right[node])

def postorder(node):
    if node != 0:
        # 왼쪽 자식을 조사
        postorder(left[node])
        # 오른쪽 자식을 조사
        postorder(right[node])
        # 후위 순회
        print(node, end=' ')

V = int(input())    # 노드의 개수
E = V -1            # 간선의 개수
edge = list(map(int, input().split()))
print(edge)

# 인덱스를 활용할 것이기 때문에 노드의 개수 +1
# 0번 노드는 없음
parent = [0] * (V+1)    # 부모의 정보
left = [0] * (V+1)      # 왼쪽 자식 정보
right = [0] * (V+1)     # 오른쪽 자식 정보

tree = [[0] * 3 for _ in range(V+1)]

for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    print(p, c)
    if left[p] == 0:    # 아직 왼쪽 자식이 없으면
        left[p] = c     # p번의 왼쪽 자식 c

    else:               #왼쪽에 자식이 있으면
        right[p] = c
    parent[c] = p

    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c
    tree[c][2] = p
    # print(left, right, parent)
print(tree)

root = 0
for i in range(1, V+1):     # 모든노드를 순회
    if parent[i] == 0: # 부모정보를 담았는데, 부모가 없으면 root
        root = i
        break
# 조사를 시작 root 노드부터
print('---전위 순회')
preorder(root)
print()

print('---중위 순회')
inorder(root)
print()
print('---후위 순회')
postorder(root)
