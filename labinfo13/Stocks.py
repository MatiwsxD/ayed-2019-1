def f(A):
    li = [0]
    for i in range(1, len(A)):
        for _ in range(len(li) - 1, -1, -1):
            if (A[li[-1]] <= A[i]):
                li.pop()
            else:
                li.append(i)
                break
        else:
            li.append(i)
    res = 0
    for i in range(li[0]):
        res += A[li[0]] - A[i]
    for i in range(1, len(li)):
        for j in range(li[i - 1] + 1, li[i]):
            res += A[li[i]] - A[j]
    return res


for _ in range(int(input())):
    input()
    print(f([int(i) for i in input().split()]))