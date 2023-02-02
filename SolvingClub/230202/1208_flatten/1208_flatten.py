import sys
sys.stdin = open('input.txt')

for k in range(1, 11):
    flatten_try = int(input())
    height = list(map(int, input().split()))

    idx_max = 0
    idx_min = 0
    for i in range(flatten_try):
        result_max = height[0]
        for num in range(1, len(height)):
            if result_max < height[num]:
                result_max = height[num]
                idx_max = num
        height[idx_max] -= 1

        result_min = height[0]
        for num in range(1, len(height)):
            if result_min > height[num]:
                result_min = height[num]
                idx_min = num
        height[idx_min] += 1
    print(result_min)
    print(result_max)

    # result_max_final = 0
    # result_min_final = 100
    # for n in height:
    #     if n > result_max_final:
    #         result_max_final = n
    #     if n < result_min_final:
    #         result_min_final = n



    # print(result_max - result_min)

