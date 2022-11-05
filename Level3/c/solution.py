def solution(map):
    import collections
    m = len(map)
    n = len(map[0])
    visited = set()
    q = collections.deque()
    q.append((0, 0, 1, 1))

    while q:
        x, y, wall, path = q.popleft()
        if x == m - 1 and y == n - 1:
            return path
        if (x, y, wall) in visited or (map[x][y] == 1 and wall == 0):
            continue
        
        visited.add((x, y, wall))
        if map[x][y] == 1:
            wall -= 1

        if x - 1 >= 0 and (x - 1, y, wall) not in visited:
            q.append((x - 1, y, wall, path + 1))
        if x + 1 < m and (x + 1, y, wall) not in visited:
            q.append((x + 1, y, wall, path + 1))
        if y - 1 >= 0 and (x, y - 1, wall) not in visited:
            q.append((x, y - 1, wall, path + 1))
        if y + 1 < n and (x, y + 1, wall) not in visited:
            q.append((x, y + 1, wall, path + 1))

    return -1
