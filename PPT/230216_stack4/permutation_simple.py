def f(i, k): # i는 시작점, k는 순열 대상의 개수
    if i == k:
        print(p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            # p[i]결정, p[i]와 관련된 작업 가능
            f(i+1, k)
            p[i], p[j] = p[j], p[i]

p = [1,2,3]
N = len(p)
f(0, N)