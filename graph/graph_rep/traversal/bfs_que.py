from collections import deque
def bfs(graph, start):
    visited = set()
    que = deque([start])
    visited.add(start)
    traversal_order = []    
    while que:
        node = que.popleft()
        traversal_order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                que.append(neighbor)
    return traversal_order

