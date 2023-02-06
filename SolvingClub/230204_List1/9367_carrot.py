import sys
sys.stdin = open('carrot_input.txt')

Test_case = int(input())

for i in range(Test_case):
    carrot = int(input())
    carrot_list = list(map(int, input().split()))
    count = 0
    count_carrot = 1
    count_carrot_list = []
    for l in range(0, len(carrot_list) - 1):
        count += 1
        if carrot_list[l] < carrot_list[count]:
            count_carrot += 1
            count_carrot_list.append(count_carrot)
        else :
            count_carrot = 1
            count_carrot_list.append(count_carrot)

    result_max = 0
    for num in range(1, len(count_carrot_list)):
        if result_max < count_carrot_list[num]:
            result_max = count_carrot_list[num]


    print(f'#{i + 1} {result_max}')