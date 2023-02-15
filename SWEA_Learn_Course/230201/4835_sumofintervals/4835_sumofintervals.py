import sys
sys.stdin = open('sample_input.txt')

Test_case = int(input())

for i in range(0, Test_case):
    Test_case_num = list(map(int, input().split()))

    number = list(map(int, input().split()))
