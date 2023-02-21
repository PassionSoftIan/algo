import sys
sys.stdin = open('5099_pizza_input.txt')
from collections import deque

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, M = map(int, input().split())
    data = deque(list(enumerate(map(int, input().split()))))
    print(data)
    fire = []
    for i in range(N):
        idx, p = data.popleft()
        print(idx, p)
        fire.append(p)
    while len(fire) > 1:
        B = fire.pop(0)
        if B//2 != 0:
            fire.append(B//2)
        if B//2 == 0:
            if data:
                A = data.pop(0)
                fire.append(A)
            else:
                continue
    print(fire[0])