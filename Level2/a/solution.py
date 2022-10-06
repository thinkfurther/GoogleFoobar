def solution(xs):
    result = 1
    negatives = 1
    max_neg = -float('inf')
    count = 0
    for n in xs:
        if n > 0:
            result *= n
        elif n < 0:
            negatives *= n
            max_neg = max(max_neg, n)
            count += 1

    result *= negatives
    if count % 2 == 1:
        result //= max_neg

    if result == 1:
        if len(xs) > 1:
            result = 0
        else:
            result = negatives
    return str(result)
