def XOR(n):
    if n % 4 == 0:
        return 0
    elif n % 4 == 1:
        return n - 1
    elif n % 4 == 2:
        return 1
    elif n % 4 == 3:
        return n
        
def solution(start, length):
    result = 0
    for i in range(length, 0, -1):
        result ^= XOR(start + (length - i) * length) ^ XOR(start + (length - i) * length + i)
    return result
