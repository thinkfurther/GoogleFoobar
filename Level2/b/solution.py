import collections
def solution(src, dest):
    src_x = src % 8
    src_y = src //8
    dest_x = dest % 8
    dest_y = dest // 8
    visited = [[False for _ in range(8)]for _ in range(8)]

    q = collections.deque()
    min_step = 0
    q.append((src_x, src_y))

    while q:
        n = len(q)
        for _ in range(n):
            cur_x, cur_y = q.popleft()
            if (cur_x, cur_y) == (dest_x, dest_y):
                return min_step
            if cur_x >= 8 or cur_x < 0 or cur_y >= 8 or cur_y < 0:
                continue
            if visited[cur_x][cur_y]:
                continue
            visited[cur_x][cur_y] = True
            q.append((cur_x - 2, cur_y - 1))
            q.append((cur_x + 2, cur_y - 1))
            q.append((cur_x - 2, cur_y + 1))
            q.append((cur_x + 2, cur_y + 1))
            q.append((cur_x - 1, cur_y - 2))
            q.append((cur_x + 1, cur_y - 2))
            q.append((cur_x - 1, cur_y + 2))
            q.append((cur_x + 1, cur_y + 2))
        min_step += 1
