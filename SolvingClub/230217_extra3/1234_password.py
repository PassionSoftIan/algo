import sys
sys.stdin = open('1234_password_input.txt')

for tc in range(10):
    N, word = map(int,input().split())
    for i in range(N):
        for j in range