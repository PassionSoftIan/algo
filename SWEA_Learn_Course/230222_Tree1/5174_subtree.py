import sys
sys.stdin = open('5174_subtree_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    E, N = map(int(input().split()))