def powerset(arr, K, result):
    global count
    if sum(result) > 10:
        return
    count += 1
    # 언제까지 함수 호출할 것인가
    if K == len(arr):
        # 모든 result를 반환 하진 않을 것이다.
        if sum(result) == 10:
            print(result)
        return
    # K는 어찌되었든 증가 하는데,
    # 그 K 번째 쓴 경우,
    powerset(arr, K + 1, result + [arr[K]])
    # 그 K 번째 쓰지 않은 경우,
    powerset(arr, K + 1, result)

arr = list(range(1,11))
count = 0
# 원본 배열, 사용한 원소 수, 총 합 리스트(사용할 원소 리스트)
powerset(arr, 0, [])
print(count)