x = list(map(int, input().split()))

result_time = x[0]
result_min = x[1] - 45
if result_time == 0:
    result_time = 24
else:
    result_time = x[0]
if result_min < 0:
    result_min = 60 + result_min
    result_time -= 1
else:
    result_min = x[1] - 45
print(result_time, result_min)