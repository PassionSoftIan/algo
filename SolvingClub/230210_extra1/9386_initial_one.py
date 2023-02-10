import sys
sys.stdin = open('one_input.txt')

Test_case = int(input())

for _ in range(Test_case):
    number = int(input())
    num_list = list(map(int, input()))
    max = 1
    count = 0
    for i in range(len(num_list)-1):
        if num_list[i] == 1 and num_list[i+1] == 1:
            count += 1
            if max < count:
                max = count
        else:
            count = 1
    print(f'#{_+1} {max}')