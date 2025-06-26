def dfs_recursive(graph , start, visited= None):
    if visited is None:
        visited = set()
    if start not in visited:
       return 
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        dfs_recursive(graph, neighbor, visited)
    return visited
graph = {
    0: [1, 2],1: [0, 3, 4],2: [0],3: [1],4: [1, 5],5: [4]}
print("DFS Traversal:",dfs_recursive(graph, 0))