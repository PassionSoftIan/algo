import sys
sys.stdin = open('1244_on_off_input.txt')

N = int(input())
status = list(map(int, input().split()))
S = int(input())
for sc in range(S):
    student = list(map(int,input().split()))