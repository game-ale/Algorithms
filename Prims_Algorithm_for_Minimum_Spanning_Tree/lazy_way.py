import heapq

def lazy_prim_mst(graph):
    n = len(graph)
    mst_edges = []
    visited = [False] * n
    min_heap = []
    
    # Start from node 0 (arbitrary)
    start_node = 0
    visited[start_node] = True
    
    # Add all edges from start_node to the heap
    for neighbor, weight in graph[start_node]:
        heapq.heappush(min_heap, (weight, start_node, neighbor))
    
    while min_heap and len(mst_edges) < n - 1:
        weight, u, v = heapq.heappop(min_heap)
        
        if visited[v]:
            continue  # Skip if already in MST
        
        visited[v] = True
        mst_edges.append((u, v, weight))
        
        # Add all edges from v to the heap
        for neighbor, weight in graph[v]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (weight, v, neighbor))
    
    return mst_edges

# Example Usage:
graph = [
    [(1, 2), (2, 3)],       # Node 0
    [(0, 2), (2, 1), (3, 4)], # Node 1
    [(0, 3), (1, 1), (3, 5)], # Node 2
    [(1, 4), (2, 5)]         # Node 3
]
print("Lazy Prim's MST:", lazy_prim_mst(graph))