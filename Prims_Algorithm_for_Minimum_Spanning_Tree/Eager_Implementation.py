import heapq

class IndexedMinHeap:
    def __init__(self):
        self.heap = []
        self.key_index = {}  # Tracks node positions in heap
    
    def push(self, key, value):
        heapq.heappush(self.heap, (value, key))
        self.key_index[key] = len(self.heap) - 1
    
    def pop(self):
        value, key = heapq.heappop(self.heap)
        del self.key_index[key]
        return key, value
    
    def decrease_key(self, key, new_value):
        idx = self.key_index[key]
        self.heap[idx] = (new_value, key)
        heapq._siftdown(self.heap, 0, idx)
    
    def __contains__(self, key):
        return key in self.key_index
    
    def __len__(self):
        return len(self.heap)

def eager_prim_mst(graph):
    n = len(graph)
    mst_edges = []
    visited = [False] * n
    ipq = IndexedMinHeap()
    
    # Initialize with node 0
    ipq.push(0, 0)  # (node, key=weight)
    
    while ipq and len(mst_edges) < n - 1:
        u, min_weight = ipq.pop()
        visited[u] = True
        
        if u != 0:  # Skip for the first node
            mst_edges.append((u, min_weight))  # (to_node, weight)
        
        for v, weight in graph[u]:
            if not visited[v]:
                if v not in ipq:
                    ipq.push(v, weight)
                elif weight < ipq.heap[ipq.key_index[v]][0]:
                    ipq.decrease_key(v, weight)
    
    return mst_edges

# Example Usage:
graph = [
    [(1, 2), (2, 3)],       # Node 0
    [(0, 2), (2, 1), (3, 4)], # Node 1
    [(0, 3), (1, 1), (3, 5)], # Node 2
    [(1, 4), (2, 5)]         # Node 3
]
print("Eager Prim's MST:", eager_prim_mst(graph))