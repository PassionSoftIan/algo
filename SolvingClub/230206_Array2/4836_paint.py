import sys
sys.stdin = open('paint_input.txt')


Test_case = int(input())

sheet = int(input())

for tc in range(Test_case):
    for pp in range(sheet):
        Array = [list(map(int, input().split())) for _ in range(10)]