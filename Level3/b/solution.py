def solution(l: List):
    n = len(l)
    count = [0] * n
    for i in range(1, n):
        for j in range(0, i):
            if l[i] % l[j] == 0:
                count[i] += 1
    result = 0
    for i in range(2, n):
        for j in range(1, i):
            if l[i] % l[j] == 0:
                result += count[j]
    return result
