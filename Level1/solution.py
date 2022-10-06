def solution(x):
    result = []
    for c in x:
        if c.islower():
            result.append(chr( ord('a') + ord('z') - ord(c)))
        else:
            result.append(c)
    return ''.join(result)
