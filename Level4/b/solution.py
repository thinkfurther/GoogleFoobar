import collections


def BFS(graph, s, t, parent):
    q = collections.deque()
    q.append(s)
    visited = set()
    visited.add(s)
    while q:
        u = q.popleft()
        for ind, val in enumerate(graph[u]):
            if ind in visited or val <= 0:
                continue
            q.append(ind)
            visited.add(ind)
            parent[ind] = u
            if ind == t:
                return True
    return False


def solution(entrances, exits, path):
    n = len(path) + 2
    graph = [[0 for _ in range(n)] for _ in range(n)]
    source = 0
    sink = n - 1
    for each_entrance in entrances:
        graph[source][each_entrance + 1] = float('inf')
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            graph[i][j] = path[i - 1][j - 1]
    for each_exit in exits:
        graph[each_exit + 1][sink] = float('inf')

    max_flow = 0
    parent = [-1] * n
    while BFS(graph, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow
