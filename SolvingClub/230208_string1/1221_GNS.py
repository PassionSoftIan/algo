import sys
sys.stdin = open('GNS_test_input.txt')


A = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOR' : 4,
     'FIV' : 5, 'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}

B = {0 : 'ZRO', 1 : 'ONE' , 2 : 'TWO', 3 : 'THR', 4 : 'FOR',
     5 : 'FIV', 6 : 'SIX', 7 : 'SVN', 8 : 'EGT', 9 : 'NIN'}


Test_case = int(input())
for tc in range(Test_case):
    tc_number = input().split()
    line = list(map(str, input().split()))
    C = []
    for i in line:
        C.append(A[i])
        C.sort()
    D = []
    for i in C:
        D.append(B[i])
    print(f'{tc_number[0]}')
    print(*D)